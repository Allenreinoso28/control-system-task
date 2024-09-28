# ################## VENV ################## #

win       - $ myenv/Scripts/activate
mac       - $ source/bin/activate

start     - $ python app

# ################## control-system-task ################## #

Software for my 2024 Robotics team application. This python program take PS4 controller input sending out data packets to be used to control the robot.

Controll Layout 🙃

# ################## Exit ################## #

PS button - exit

# ################## Test Mode ################## #

Options   - toggle program sending packets

# ################## Speed Modes ################## #

R3/L3     - toggle through preset list of changes in speed [18, 36, 54, 72, 90, 108, 127]
L1        - holding enables throttle control (can only use 1 of Arm or Wrist Systems at a time)

# ################## Drive System ################## #

R Stick   - controls right set of wheels with foward and back inputs
L Stick   - controls left set of wheels with foward and back inputs

# ################## Arm System ################## #

R2        - throttle select motor clockwise
L2        - throttle select motor counterclockwise
△        - holding selects gantry (R2 up / L2 down)
𐤏        - holding selects shoulder (R2 CW / L2 CCW)
X         - holding selects elbow (R2 up / L2 down)
□         - holding selects claw (R2 open / L2 close)

# ################## Wrist System ################## #

R2        - (when holding L1) throttle select wrist action
up        - move wrist up
down      - move wrist down
left      - spin wrist counterclockwise
right     - spin wrist clockwise

# ################## PYGAME INPUT MAPPING ################## #


# Playstation 4 Controller (pygame 2.x)
# The PlayStation 4 controller mapping has 6 axes and 16 buttons. The controller is recognized as "PS4 Controller".

# Left Stick:
# Left -> Right   - Axis 0
# Up   -> Down    - Axis 1
# 
# Right Stick:
# Left -> Right   - Axis 2
# Up   -> Down    - Axis 3\

# Left Trigger:
# Out -> In       - Axis 4

# Right Trigger:
# Out -> In       - Axis 5

# Buttons:
# Cross Button    - Button 0
# Circle Button   - Button 1
# Square Button   - Button 2
# Triangle Button - Button 3
# Share Button    - Button 4
# PS Button       - Button 5
# Options Button  - Button 6
# L. Stick In     - Button 7
# R. Stick In     - Button 8
# Left Bumper     - Button 9
# Right Bumper    - Button 10
# D-pad Up        - Button 11
# D-pad Down      - Button 12
# D-pad Left      - Button 13
# D-pad Right     - Button 14
# Touch Pad Click - Button 15
