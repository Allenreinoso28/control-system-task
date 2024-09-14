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


import socket
import pygame





