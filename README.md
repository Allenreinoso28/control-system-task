# control-system-task
Software for my 2024 Robotics team application. This python program take PS4 controller input sending out data packets to be used to control the robot.

Controll Layout

# Exit
PS button - exit

# Test Mode
Options   - toggle program sending packets

# Drive System:
R1        - holding allows for control of drive system
R Stick   - controls right set of wheels with foward and back inputs
L Stick   - controls left set of wheels with foward and back inputs

# Arm System:
R2        - throttle select motor clockwise
L2        - throttle select motor counterclockwise
△        - holding selects gantry (R2 up / L2 down)
𐤏        - holding selects shoulder (R2 CW / L2 CCW)
X         - holding selects elbow (R2 up / L2 down)
□         - holding selects claw (R2 open / L2 close)

# Wrist System
R3/L3     - toggle through preset speeds (slow, medium, fast)
L1        - holding enables throttle control (deactivate arm system when on)
R2        - (when holding L1) throttle select wrist action

(preset or throttle speed) 
up        - move wrist up
down      - move wrist down
left      - spin wrist counterclockwise
right     - spin wrist clockwise

