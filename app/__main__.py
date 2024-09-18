
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

#server address vars
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

    # #open socket (AF_INET, AF_BLUETOOTH, idk) (SOCK_DGRAM because I want a what real-time feedback and packet loss is okay)
    client_socket = socket.socket( socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (ADDRESS,PORT)
    #initalize controller
    controller = pygame.joystick.Joystick(0)
    controller.init()
    print("CONTROLLER HAS BEEN CONNECTED")
    
    
    ##Settings vars##
    
    STATIONARY = 128
    last_A_command = ''
    last_D_command = ''

    count  = 0
    slow = 20
    medium = 64
    fast = 127
    speeds = [slow, medium, fast]
    speed_labels = ["Slow", "Medium", "Fast"]
    speedMode  = speeds[count]
    #if left bumper is pressed
    dpad_throttle_mode = False

    #milliseconds delay betwwen loops (50 = 20htz refresh rate)
    MILLISECONDS = 50

    

    #main loop (IMPORTANT THAT THE PACKETS ARE EVENT DRIVEN TO REDUCE REDUNANCY)
    running = True
    while running:

        ##VARIABLES PWM##
        #WHEELS
        rightWheel1 = rightWheel2 = rightWheel3 = STATIONARY
        leftWheel1  = leftWheel2  = leftWheel3  = STATIONARY

        #ARM
        elbow       = STATIONARY
        wristright  = STATIONARY
        wristleft   = STATIONARY
        claw        = STATIONARY
        gantry      = STATIONARY
        shoulder    = STATIONARY

        #TRIGGER THROTTLE
        l2Throttle  = (controller.get_axis(4)+1)/2    
        r2Throttle  = (controller.get_axis(5)+1)/2
        total_throttle = r2Throttle - l2Throttle


        ##DRIVE FUNCTIONS##

        ##event update wheel motor right side##
        rightstick = controller.get_axis(3)
        #check if right bumper for gas
        if controller.get_button(10) != 0:
            #giving a lil deadzone to account for stickdrift
            #forward (CW)(0 to -1)
            if rightstick < -0.05:
                speed = STATIONARY - (127 * rightstick)
                rightWheel1 = rightWheel2 = rightWheel3 = speed
            #backward (CCW)(0 to 1)
            elif rightstick > 0.05:
                speed = STATIONARY - (128 * rightstick)
                rightWheel1 = rightWheel2 = rightWheel3 = speed

        ##event update wheel motor left side##
        leftstick = controller.get_axis(1)
        #check if right bumper for gas
        if controller.get_button(10) != 0:
            #giving a lil deadzone to account for stickdrift
            #forward (CCW)(0 to -1)
            if leftstick < -0.05:
                speed = STATIONARY + (128 * leftstick)
                leftWheel1 = leftWheel2 = leftWheel3 = speed
            #backward (CW)(0 to 1)
            elif leftstick > 0.05:
                speed = STATIONARY + (127 * leftstick)
                leftWheel1 = leftWheel2 = leftWheel3 = speed





        ##ARM FUNCTIONS## 

        # Cross Button    - Button 0
        # Circle Button   - Button 1
        # Square Button   - Button 2
        # Triangle Button - Button 3    

        ##event update gantry motor##
        if controller.get_button(3) == 1 and dpad_throttle_mode == False:
            if total_throttle > 0:
                gantry = gantry + (127 * total_throttle)
            if total_throttle < 0:
                gantry = gantry + (128 * total_throttle)
            #print("Gantry: ", gantry)

        ##event update elbow motor##
        if controller.get_button(0) == 1 and dpad_throttle_mode == False:
            if total_throttle > 0:
                elbow = elbow + (127 * total_throttle)
            if total_throttle < 0:
                elbow = elbow + (128 * total_throttle)
            #print("Elbow: ", elbow)

        ##event update shoulder motor##
        if controller.get_button(1) == 1 and dpad_throttle_mode == False:
            if total_throttle > 0:
                shoulder = shoulder + (127 * total_throttle)
            if total_throttle < 0:
                shoulder = shoulder + (128 * total_throttle)
            #print("Shoulder: ", shoulder)
        
        ##event update claw motor##
        if controller.get_button(2) == 1 and dpad_throttle_mode == False :
            if total_throttle > 0:
                claw = claw + (127 * total_throttle)
            if total_throttle < 0:
                claw = claw + (128 * total_throttle)
            #print("claw: ", claw)





        ##wrist functions##

        #  128 - 255 PWM Wristright and Wristleft -> Spins the claw clockwise
        #  128 - 255 PWM Wristleft and 128 - 0 PWM Wristright -> claw moves up
        # D-pad Up        - Button 11
        # D-pad Down      - Button 12
        # D-pad Left      - Button 13
        # D-pad Right     - Button 14

        # move claw upwards
        if controller.get_button(11) == 1:
            if dpad_throttle_mode:
                if r2Throttle > 0:
                    wristleft = wristleft + (127 * r2Throttle)
                    wristright = wristright - (128 * r2Throttle)
            else:
                wristleft = STATIONARY + speedMode
                wristright = 127 - speedMode

        # move claw downwards
        if controller.get_button(12) == 1:
            if dpad_throttle_mode:
                if r2Throttle > 0:
                    wristleft = wristleft - (128 * r2Throttle)
                    wristright = wristright + (127 * r2Throttle)
            else:
                wristleft = 127 - speedMode
                wristright = STATIONARY + speedMode

        # spin claw CCW
        if controller.get_button(13) == 1:
            if dpad_throttle_mode:
                if r2Throttle > 0:
                    wristleft = wristleft - (128 * r2Throttle)
                    wristright = wristright - (128 * r2Throttle)
            else:
                wristleft = 127 - speedMode
                wristright = 127 - speedMode

        # spin claw CW
        if controller.get_button(14) == 1:
            if dpad_throttle_mode:
                if r2Throttle > 0:
                    wristleft = wristleft + (127 * r2Throttle)
                    wristright = wristright + (127 * r2Throttle)
            else:
                wristleft = STATIONARY + speedMode
                wristright = STATIONARY + speedMode





        ##PACKET ASSEMBLY AND SHIPMENT##

        #“A_elbow_wristright_wristleft_claw_gantry_shoulder”
        arm_command = f"A_{elbow}_{wristright}_{wristleft}_{claw}_{gantry}_{shoulder}"

        #“D_rightWheel1_rightWheel2_rightWheel3_leftWheel1_leftWheel2_leftWheel3”  
        wheels_command = f"D_{rightWheel1}_{rightWheel2}_{rightWheel3}_{leftWheel1}_{leftWheel2}_{leftWheel3}"
        
        ##print outgoing commands
        #reduce redundant commands by storing last command
        if last_A_command != arm_command:
            print(arm_command)
            try:
                client_socket.sendto(arm_command.encode(), server_address)
            except:
                # print("ERROR CONNECTION TO SERVER INVALID PLEASE CONFIRM ADDRESS")
                None
        last_A_command = arm_command

        if last_D_command != wheels_command:
            print(wheels_command)
            try:
                client_socket.sendto(wheels_command.encode(), server_address)
            except:
                # print("ERROR CONNECTION TO SERVER INVALID PLEASE CONFIRM ADDRESS")
                None
        last_D_command = wheels_command


        for event in pygame.event.get():

            #quit program function
            if event.type == quit:
                running = False
            elif event.type == pygame.JOYBUTTONUP and event.button == 5:
                running = False 

            if event.type == pygame.JOYBUTTONUP and event.button == 8:
                count += 1
                if count > 2:
                    count = 0
                speedMode = speeds[count]
                print(speed_labels[count],": ", speedMode)
                

            if event.type == pygame.JOYBUTTONUP and event.button == 7:
                count -= 1
                if count <= -1:
                    count = 2
                speedMode = speeds[count]
                print(speed_labels[count],": ", speedMode)

                

            if event.type == pygame.JOYBUTTONDOWN and event.button == 9:
                dpad_throttle_mode = True
                print("D-PAD THROTTLE MODE : ON")
            
            if event.type == pygame.JOYBUTTONUP and event.button == 9:
                dpad_throttle_mode = False
                print("D-PAD THROTTLE MODE : OFF")

        #sets the while loop to occur every N milliseconds
        pygame.time.delay(MILLISECONDS)



#start program
if __name__ == "__main__":
    send_controller_input()