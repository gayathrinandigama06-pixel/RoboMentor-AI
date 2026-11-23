"""Offline rule-based robotics learning assistant."""

KNOWLEDGE = [
    (("inverse kinematics", "ik"), """### Inverse kinematics
Inverse kinematics (IK) calculates the joint variables needed to place a robot end-effector at a desired position.

For a planar two-link arm, first calculate:
\\(c_2=(x^2+y^2-L_1^2-L_2^2)/(2L_1L_2)\\).
Then find two possible elbow configurations when the target is reachable.

**Use:** robot arm positioning, pick-and-place and motion planning.

**Limitation:** a mathematical solution does not automatically account for joint limits, collisions or motor capability."""),
    (("forward kinematics", "fk"), """### Forward kinematics
Forward kinematics calculates the end-effector position from known joint angles and link dimensions.

For a two-link planar arm:
\\(x=L_1\\cos\\theta_1+L_2\\cos(\\theta_1+\\theta_2)\\)
\\(y=L_1\\sin\\theta_1+L_2\\sin(\\theta_1+\\theta_2)\\)

**Use:** predicting where a robot tool will be after setting its joints."""),
    (("sensor", "ultrasonic", "lidar"), """### Robotics sensors
Sensors measure information about a robot or its environment. Examples include ultrasonic distance sensors, LiDAR, encoders, IMUs and cameras.

A sensor has a measurement range, resolution, update rate, uncertainty and interface. Sensor selection depends on the task and environment."""),
    (("motor", "servo", "stepper", "dc motor"), """### Motors in robotics
- **DC motor:** commonly used for continuous rotation; speed can be controlled with a driver.
- **Servo motor:** provides position control within its designed range.
- **Stepper motor:** moves in discrete steps and is useful when controlled positioning is needed.

Motor choice depends on torque, speed, precision, load, power and control requirements."""),
    (("pid", "control system"), """### PID control
A PID controller combines proportional, integral and derivative terms.

\\(u(t)=K_p e(t)+K_i\\int e(t)dt+K_d\\frac{de(t)}{dt}\\)

The proportional term responds to present error, integral addresses accumulated error, and derivative responds to the rate of change. Gains must be tuned and tested for the actual system."""),
    (("robotics", "robot", "robot arm"), """### Robotics fundamentals
A robot combines mechanical structure, actuators, sensors, control, computation and a task. Common study areas include kinematics, dynamics, perception, localization, planning and control.

Start by defining the task, workspace, degrees of freedom, payload, precision and safety requirements."""),
    (("obstacle", "collision", "path planning"), """### Obstacle avoidance
A robot planner searches for a route from a start state to a goal while avoiding obstacles. Methods include grid search (BFS/A*), sampling-based planners (RRT) and optimization-based methods.

A collision check must consider the robot's full geometry, not just its end-effector. This prototype currently checks a line segment against one circular obstacle only."""),
]

def answer_question(question: str) -> str:
    q = (question or "").strip().lower()
    if not q:
        return "Please enter a question about robotics, sensors, motors, kinematics, control or path planning."
    for keywords, response in KNOWLEDGE:
        if any(word in q for word in keywords):
            return response
    return ("I do not have a prepared explanation for that topic in the offline knowledge base yet. "
            "Try asking about forward kinematics, inverse kinematics, sensors, motors, PID control, "
            "robotics fundamentals or obstacle avoidance. You can extend `robomentor/mentor.py` with new verified topics.")
