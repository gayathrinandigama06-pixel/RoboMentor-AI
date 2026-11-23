import streamlit as st
import numpy as np
import plotly.graph_objects as go
from robomentor.kinematics import forward_kinematics, inverse_kinematics, interpolate_path
from robomentor.mentor import answer_question
from robomentor.safety import point_is_clear, path_is_clear

st.set_page_config(page_title="RoboMentor AI", page_icon="🤖", layout="wide")
st.title("🤖 RoboMentor AI")
st.caption("An offline-first virtual robotics laboratory for engineering students")

with st.sidebar:
    st.header("Laboratory settings")
    l1 = st.slider("Link 1 length (units)", 1.0, 10.0, 5.0, 0.5)
    l2 = st.slider("Link 2 length (units)", 1.0, 10.0, 4.0, 0.5)
    st.divider()
    st.caption("Runs locally on your laptop. No API key or paid service is required.")
    st.success("Offline core: available")

tabs = st.tabs(["2D Arm Simulator", "Inverse Kinematics", "AI Mentor", "Obstacle Lab", "Experiments", "About"])

with tabs[0]:
    st.subheader("Two-link planar robotic arm")
    c1, c2 = st.columns([1, 1])
    with c1:
        theta1 = st.slider("Shoulder angle (degrees)", -180, 180, 35, key="fk1")
        theta2 = st.slider("Elbow angle (degrees)", -180, 180, 55, key="fk2")
        result = forward_kinematics(l1, l2, np.radians(theta1), np.radians(theta2))
        st.metric("End-effector X", f"{result[0]:.3f}")
        st.metric("End-effector Y", f"{result[1]:.3f}")
        st.info("Change the joint angles and observe how the end-effector position changes.")
    with c2:
        p0 = np.array([0.0, 0.0])
        p1 = np.array([l1*np.cos(np.radians(theta1)), l1*np.sin(np.radians(theta1))])
        p2 = np.array(result)
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=[p0[0],p1[0],p2[0]], y=[p0[1],p1[1],p2[1]],
                                 mode="lines+markers+text", text=["Base","Joint 2","Tool"],
                                 line=dict(width=8), marker=dict(size=13), name="Robot arm"))
        fig.add_shape(type="circle", x0=-0.15, y0=-0.15, x1=0.15, y1=0.15,
                      line=dict(width=2))
        fig.update_layout(title="Top-view kinematic model", xaxis_title="X", yaxis_title="Y",
                          yaxis_scaleanchor="x", height=430, margin=dict(l=10,r=10,t=45,b=10))
        st.plotly_chart(fig, use_container_width=True)

with tabs[1]:
    st.subheader("Inverse kinematics: reach a target")
    st.write("Enter a target coordinate. The solver calculates possible joint configurations.")
    a, b = st.columns(2)
    with a:
        tx = st.number_input("Target X", value=5.0, step=0.5)
        ty = st.number_input("Target Y", value=4.0, step=0.5)
        elbow = st.selectbox("Elbow configuration", ["down", "up"])
        if st.button("Solve inverse kinematics", type="primary"):
            solution = inverse_kinematics(l1, l2, tx, ty, elbow)
            if solution is None:
                st.error("Target is unreachable for the current link lengths.")
            else:
                q1, q2 = solution
                st.success("A valid mathematical solution was found.")
                st.metric("Shoulder angle", f"{np.degrees(q1):.2f}°")
                st.metric("Elbow angle", f"{np.degrees(q2):.2f}°")
                check = forward_kinematics(l1, l2, q1, q2)
                st.write(f"Forward-check endpoint: ({check[0]:.3f}, {check[1]:.3f})")
    with b:
        st.markdown("**Engineering principle**")
        st.latex(r"x=L_1\\cos(\\theta_1)+L_2\\cos(\\theta_1+\\theta_2)")
        st.latex(r"y=L_1\\sin(\\theta_1)+L_2\\sin(\\theta_1+\\theta_2)")
        st.latex(r"\\cos(\\theta_2)=\\frac{x^2+y^2-L_1^2-L_2^2}{2L_1L_2}")
        st.caption("This is a planar 2-DOF model. Real robots require calibration, joint limits and physical safety validation.")

with tabs[2]:
    st.subheader("RoboMentor – local engineering assistant")
    st.write("Ask about kinematics, motors, sensors, robotics, control systems or project concepts.")
    question = st.text_input("Your question", placeholder="What is inverse kinematics?")
    if st.button("Ask RoboMentor"):
        response = answer_question(question)
        st.markdown(response)
    st.caption("The assistant uses a curated local knowledge base and rule-based topic matching. Internet access is not needed.")

with tabs[3]:
    st.subheader("Obstacle awareness demonstration")
    st.write("A simple 2D point/path planner checks whether a straight-line route intersects a circular obstacle.")
    x0 = st.number_input("Start X", value=0.0, key="ox0")
    y0 = st.number_input("Start Y", value=0.0, key="oy0")
    xg = st.number_input("Goal X", value=8.0, key="ox1")
    yg = st.number_input("Goal Y", value=6.0, key="oy1")
    ox = st.number_input("Obstacle centre X", value=4.0)
    oy = st.number_input("Obstacle centre Y", value=3.0)
    radius = st.slider("Obstacle radius", 0.2, 3.0, 1.0)
    start, goal, center = (x0,y0), (xg,yg), (ox,oy)
    clear = path_is_clear(start, goal, center, radius)
    fig2 = go.Figure()
    fig2.add_shape(type="circle", x0=ox-radius, y0=oy-radius, x1=ox+radius, y1=oy+radius,
                   fillcolor="rgba(255,80,80,0.20)", line=dict(color="red"))
    fig2.add_trace(go.Scatter(x=[x0,xg], y=[y0,yg], mode="lines+markers",
                              name="Proposed route", line=dict(width=4)))
    fig2.add_trace(go.Scatter(x=[ox], y=[oy], mode="markers", marker=dict(size=8), name="Obstacle centre"))
    fig2.update_layout(xaxis_title="X", yaxis_title="Y", yaxis_scaleanchor="x", height=400)
    st.plotly_chart(fig2, use_container_width=True)
    if clear:
        st.success("The straight-line route clears the circular obstacle.")
    else:
        st.warning("The proposed straight-line route intersects or touches the obstacle. A detour planner is needed.")
    st.caption("Educational geometry demonstration only; not a certified robot safety system.")

with tabs[4]:
    st.subheader("Guided engineering experiments")
    experiments = {
        "Experiment 1 – Forward kinematics": "Change both joint angles. Record the endpoint coordinates. Explain how changing the elbow angle affects reach.",
        "Experiment 2 – Workspace": "Vary link lengths and map the farthest and nearest reachable points. Compare the theoretical reach L1+L2 with the plotted endpoint.",
        "Experiment 3 – Inverse kinematics": "Choose a reachable target, solve for elbow-up and elbow-down configurations, and compare the joint angles.",
        "Experiment 4 – Obstacle geometry": "Move the obstacle centre and radius. Identify when the straight-line path changes from clear to blocked.",
        "Experiment 5 – Sensitivity": "Increase one joint angle by 5 degrees. Measure the endpoint displacement and discuss why small joint changes can cause different tool motion."
    }
    for title, desc in experiments.items():
        with st.expander(title):
            st.write(desc)
            st.write("**Record:** input values, output values, observation, conclusion and limitations.")

with tabs[5]:
    st.subheader("Project information")
    st.markdown("""
**Purpose:** Make foundational robotics concepts interactive and accessible without buying robot hardware.

**Current prototype capabilities**
- Two-link planar forward kinematics
- Analytical inverse kinematics with elbow-up/down solutions
- Interactive arm visualization
- Circular-obstacle line-of-sight check
- Local topic-based engineering mentor
- Guided experiments

**Limitations**
- This is a 2D kinematic model displayed as a virtual laboratory, not a physical robot controller.
- The obstacle module checks a straight line only; it does not yet compute a complete collision-free route.
- The mentor is a local rule-based educational assistant, not a general-purpose trained AI model.
- No real-world robot, motor, camera or sensor is controlled.

**Suggested future work:** add joint limits, a 3D multi-link model, A* grid planning, camera-based object detection, ROS 2 integration and validated hardware testing.
""")
    st.markdown("""**Online learning resources**

- [ROS 2 documentation](https://docs.ros.org/)
- [Python documentation](https://docs.python.org/3/)
- [Streamlit documentation](https://docs.streamlit.io/)
- [NumPy documentation](https://numpy.org/doc/)

These links require internet access; the simulator and local mentor do not.

**Version:** 1.0.0 · **License:** MIT · **Cost:** Free/open-source dependencies""")
