# RoboMentor AI – Technical Report

## 1. Abstract
RoboMentor AI is an offline-first educational software prototype for introducing engineering students to robot-arm kinematics, simple obstacle geometry and robotics fundamentals. It combines a Streamlit interface, numerical calculations, Plotly visualization and a local topic-based mentor.

## 2. Problem statement
Students beginning robotics often need to connect mathematical equations with robot movement. Physical robot kits can be expensive or unavailable. This prototype provides an interactive, low-cost learning environment for foundational concepts.

## 3. Objectives
- Visualize a planar two-link manipulator.
- Calculate end-effector coordinates from joint angles.
- Solve inverse kinematics for reachable targets.
- Demonstrate a basic obstacle collision check.
- Provide accessible offline explanations and guided experiments.

## 4. Methodology
The application accepts user inputs through Streamlit controls. The kinematics module calculates positions and joint angles. Plotly displays the manipulator and obstacle scenario. A local knowledge base maps common topic keywords to curated explanations. Pytest validates mathematical and geometric functions.

## 5. Mathematical model
For link lengths L1 and L2 and joint angles θ1 and θ2:
x = L1 cos(θ1) + L2 cos(θ1 + θ2)
y = L1 sin(θ1) + L2 sin(θ1 + θ2)

The inverse solver derives cos(θ2) using the cosine rule and obtains θ1 using two-argument arctangent functions. Two elbow configurations are possible for most interior reachable targets.

## 6. Software architecture
- Presentation: Streamlit.
- Visualization: Plotly.
- Numerical operations: NumPy and Python math.
- Kinematics: `robomentor/kinematics.py`.
- Obstacle geometry: `robomentor/safety.py`.
- Offline explanations: `robomentor/mentor.py`.
- Verification: pytest unit tests.

## 7. Test plan
Test straight-arm forward kinematics, inverse/forward round trips for both elbow branches, unreachable targets, path interpolation endpoints, clear paths, blocked paths, tangency and invalid negative obstacle radius. Record the actual local test output before publication.

## 8. Limitations and safety
This is a software-only educational model. It is not an industrial robot controller or a safety-rated system. The obstacle checker treats the robot as a line segment between start and goal and checks one circular obstacle; it does not model the links' full swept volume. No physical actuation is provided. Results should not be used to command real machinery.

## 9. Future development
Add joint constraints, robust collision checking for the full arm geometry, grid-based A* planning, 3D modelling, perception, ROS 2 connectivity and systematic usability evaluation.

## 10. Conclusion
The prototype demonstrates how fundamental mechanical engineering mathematics and software tools can be integrated into an accessible robotics learning application. Further validation and feature development are required before describing it as a complete robotics platform.
