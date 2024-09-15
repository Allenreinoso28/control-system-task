#keep in mind that we will be sending sockets out in a continous flow of data

#open socket
#Connect the controller via Pygame
#initalize all the motor values to 128
    
#initalize joystick coords (0,0) (consider including a deadzone to account for stick drift)
#while loop (running)
    
    #on press of some button, update variables (const slow)
        # on press of left trigger adjust throttle (range 0-128)
    #on release of some button, return to "0" state

    #on press of trigger adjust throttle (range 0 - 128)
    #joystick coord to filter (will convert joystick axis to value ranging from -1 to 1 ) 
        #throttle and filter will be added to based 128 var to get new value

    #send socket (wheels)
    #send socket (arm)



#list of motors

#ARM
    # shoulder (bumpers)
    # wristright (pair with leftwrist on d-pad)
    # wristleft 
    # claw  (constant speed slow) (?)
    # gantry (constant speed slow-medium) (square)(triangle)
    # elbow ()

#WHEELS (speed controlled) (mapped to left-joysick)
    #rightWheel1
    #rightWheel2
    #rightWheel3
    #leftWheel1
    #leftWheel2
    #leftWheel3




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


import socket
import pygame

ADDRESS = 'localhost'
PORT = '12345'

def send_controller_input():

    #initialize pygame
    pygame.init()

    #initailize the controller module
    pygame.joystick.init()

    #check for controller
    controller_count = pygame.joystick.get_count()
    if controller_count == 0:
        print("CONTROLLER NOT FOUND")
        pygame.quit
        quit()

    # #open socket (AF_INET, AF_BLUETOOTH, idk) (SOCK_STREAM because I want a continous connection)
    # client_socket = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
    # client_socket.connect((ADDRESS, PORT))


    #initalize controller
    controller = pygame.joystick.Joystick(0)
    controller.init()
    print("CONTROLLER HAS BEEN CONNECTED")


    #main loop
    running = True
    while running:
        for event in pygame.event.get():

            #quit program function
            if event.type == quit:
                running = False
            elif event.type == pygame.JOYBUTTONUP and event.button == 6:
                running = False 


            ##VARIABLES PWM##
        STATIONARY = 128
        #WHEELS
        rightWheel1 = rightWheel2 = rightWheel3 = STATIONARY
        leftWheel1  = leftWheel2  = leftWheel2  = STATIONARY

        #ARM
        elbow       = STATIONARY
        wristright  = STATIONARY
        wristleft   = STATIONARY
        claw        = STATIONARY
        gantry      = STATIONARY
        shoulder    = STATIONARY

        #TRIGGER THROTTLE
        l2Throttle  = 0    
        r2Throttle  = 0

        #BUTTON SPEED MODIFIERS
        slow = 15
        medium = 64
        fast = 127
        SPEED = medium
    
        # Get controller state (TEST)
        # axes = [controller.get_axis(i) for i in range(controller.get_numaxes())]
        # buttons = [controller.get_button(i) for i in range(controller.get_numbuttons())]

        # print("Axes: ", axes)
        # print("Buttons: ", buttons)

        ##update wheel motor right side##
        rightstick = controller.get_axis(3)
        #check if right trigger for gas
        if controller.get_axis(5) != -1:
            #giving a lil deadzone to account for stickdrift
            #forward (CW)(0 to -1)
            if rightstick < -0.05:
                speed = STATIONARY - (127 * rightstick)
                rightWheel1 = rightWheel2 = rightWheel3 = speed
            #backward (CCW)(0 to 1)
            elif rightstick > 0.05:
                speed = STATIONARY - (128 * rightstick)
                rightWheel1 = rightWheel2 = rightWheel3 = speed
        
        ##update wheel motor right side##
        leftstick = controller.get_axis(1)
        #check if right trigger for gas
        if controller.get_axis(4) != -1:
            #giving a lil deadzone to account for stickdrift
            #forward (CCW)(0 to -1)
            if leftstick < -0.05:
                speed = STATIONARY + (128 * leftstick)
                leftWheel1 = leftWheel2 = leftWheel3 = speed
            #backward (CW)(0 to 1)
            elif leftstick > 0.05:
                speed = STATIONARY + (127 * leftstick)
                leftWheel1 = leftWheel2 = leftWheel3 = speed

        print(leftWheel1, " , ", rightWheel1)
        pygame.time.delay(1000)

        



#start program
if __name__ == "__main__":
    send_controller_input()