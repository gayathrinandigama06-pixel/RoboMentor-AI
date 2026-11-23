# RoboMentor AI
### Offline-first virtual robotics laboratory for engineering students

RoboMentor AI is a free, Python-based educational prototype that helps engineering students explore planar robot-arm kinematics, inverse kinematics, basic obstacle geometry and robotics fundamentals through an interactive web interface.

> **Honest scope statement:** The current mentor is a local rule-based educational assistant, not a trained generative AI model. The obstacle module checks a straight-line segment against one circular obstacle; it is not a complete collision-free motion planner. The robot is simulated only and does not control physical hardware.

## Features
- Interactive two-link planar robot arm.
- Forward kinematics from joint angles to end-effector coordinates.
- Analytical inverse kinematics with elbow-up and elbow-down solutions.
- 2D visualization using Plotly.
- Straight-line versus circular-obstacle geometry check.
- Offline topic-based robotics mentor.
- Five guided engineering experiments.
- Automated unit tests.

## System requirements
- Windows 11
- Python 3.10 or newer (64-bit recommended)
- Intel Core 5 or equivalent; 8 GB RAM recommended for a comfortable experience
- Internet only for the first dependency installation; after installation, the core app runs locally.
- No API key, paid API or physical robot is required.

## Install and run (Windows 11)
1. Install Python from https://www.python.org/downloads/ and enable **Add Python to PATH**.
2. Extract this repository folder.
3. Double-click `run_windows.bat`.
4. Wait for dependencies to install. Your browser should open the local Streamlit app.
5. If it does not open automatically, visit `http://localhost:8501`.

Manual installation in PowerShell:
```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m streamlit run app.py
```
If PowerShell blocks activation, use Command Prompt and run:
```cmd
.venv\Scripts\activate.bat
```

## Run tests
Open a terminal in the project folder:
```powershell
.\.venv\Scripts\Activate.ps1
python -m pytest -q
```

## Engineering model
For link lengths `L1`, `L2` and joint angles `theta1`, `theta2`:

```text
x = L1*cos(theta1) + L2*cos(theta1 + theta2)
y = L1*sin(theta1) + L2*sin(theta1 + theta2)
```

Inverse kinematics uses:
```text
cos(theta2) = (x*x + y*y - L1*L1 - L2*L2) / (2*L1*L2)
theta1 = atan2(y,x) - atan2(L2*sin(theta2), L1 + L2*cos(theta2))
```
A target is reachable only when the computed cosine lies in [-1, 1], subject to numerical tolerance.

## Architecture
```text
Browser
  |
  v
Streamlit UI (app.py)
  |-------------------|
  v                   v
Kinematics module     Local Mentor
  |                   |
  v                   v
Forward / inverse     Curated offline topic
kinematics            explanations
  |
  v
Obstacle geometry module
  |
  v
Plotly visualizations
```

## Suggested project demonstration
1. Open the 2D Arm Simulator tab (the arm model is a 2D planar arm displayed in an interactive chart).
2. Move the shoulder and elbow sliders; note endpoint coordinates.
3. Open Inverse Kinematics and solve for a reachable target such as (5, 4) with the default link lengths.
4. Ask the mentor: “What is inverse kinematics?”
5. Open Obstacle Lab and move the obstacle into and out of the proposed line segment.
6. Run tests and include the actual test output in your project report.

## Validation checklist
- [ ] App launches successfully on Windows 11.
- [ ] Both elbow configurations reproduce the requested target within numerical tolerance.
- [ ] Unreachable targets are reported.
- [ ] Obstacle test cases pass.
- [ ] Offline mentor responds without an API key.
- [ ] `pytest -q` passes.
- [ ] Capture screenshots of the running app for the portfolio.

## Roadmap
- Add joint limits and singularity warnings.
- Add a true 3D multi-link model.
- Add grid-based A* route planning and robot-footprint collision checking.
- Add camera-based object detection using an optional local model.
- Add ROS 2 integration and hardware-in-the-loop testing.
- Add a documented evaluation dataset and benchmark metrics.

## Portfolio description
**RoboMentor AI – Offline-First Virtual Robotics Laboratory**

Built a Python and Streamlit educational robotics simulator featuring forward and inverse kinematics for a two-link planar manipulator, interactive visualization, circular-obstacle path checking, and a local robotics learning assistant. Designed to make core robotics concepts accessible to engineering students without requiring physical hardware or paid APIs.

## Repository structure
```text
RoboMentor_AI/
├── app.py
├── requirements.txt
├── run_windows.bat
├── robomentor/
│   ├── __init__.py
│   ├── kinematics.py
│   ├── mentor.py
│   └── safety.py
├── tests/
│   ├── test_kinematics.py
│   └── test_safety.py
├── docs/
│   ├── TECHNICAL_REPORT.md
│   └── LINKEDIN_POST.md
├── LICENSE
└── README.md
```

## License
MIT. See `LICENSE`.
