# Setup and testing record

## Environment
- OS: Windows 11
- CPU: Intel Core 5
- Python version: record with `python --version`
- Dependency versions: record with `pip freeze`

## Installation
Use `run_windows.bat`, or follow the PowerShell commands in the README.

## Automated tests
Run:
```powershell
python -m pytest -q
```
Copy the actual terminal output here after running tests. Do not claim tests passed until they have been run on your laptop.

## Manual test cases
1. Forward kinematics: set both angles to 0 degrees. Expected endpoint X = L1 + L2 and Y = 0.
2. IK reachable: default lengths, target (5, 4). Expected: a valid solution for each elbow branch.
3. IK unreachable: target (100, 100). Expected: unreachable message.
4. Mentor offline: disconnect internet after installation and ask “What is a sensor?” Expected: local explanation.
5. Obstacle blocked: start (0,0), goal (8,6), obstacle near the segment. Expected: blocked warning.
6. Obstacle clear: move obstacle far from the segment. Expected: clear message.

## Evidence to capture
- Main simulator with arm and coordinate readouts.
- Inverse kinematics solution.
- Offline mentor response.
- Obstacle clear and blocked examples.
- Passing pytest terminal output.
