import websockets
import asyncio
import pygame
from controller import Controller
from motors import WheelMotor, ArmMotor, WristMotors

#server address vars
ADDRESS = 'localhost'
PORT = '6789'

# Global Speed Setting
speed_levels = [18, 36, 54, 72, 90, 108, 127]
change_in_speed_count = 0
change_in_speed = speed_levels[change_in_speed_count]

def increase_change_in_speed():
    global change_in_speed_count, change_in_speed
    if change_in_speed_count < len(speed_levels) - 1:
        change_in_speed_count += 1
        change_in_speed = speed_levels[change_in_speed_count]
        print("Change in Speed: ", change_in_speed)

def decrease_change_in_speed():
    global change_in_speed_count, change_in_speed
    if change_in_speed_count > 0:
        change_in_speed_count -= 1
        change_in_speed = speed_levels[change_in_speed_count]
        print("Change in Speed: ", change_in_speed)

async def send_controller_input(websocket, path):
    
    print(f"Client connected: {path}")
    # # #open socket (AF_INET, AF_BLUETOOTH, idk) (SOCK_DGRAM because I want a what real-time feedback and packet loss is okay)
    # client_socket = socket.socket( socket.AF_INET, socket.SOCK_DGRAM)
    # server_address = (ADDRESS,PORT)

   

    # #initalize controller
    controller = Controller()
    
    ##CREATING MOTOR INSTANCES
    right_wheels = WheelMotor()
    left_wheels = WheelMotor()
    gantry = ArmMotor()
    shoulder = ArmMotor()
    elbow = ArmMotor()
    claw = ArmMotor()
    wrist = WristMotors()

    ##Settings vars##
    last_A_command = ''
    last_D_command = ''
    mode = "set"

    #milliseconds delay betwwen loops (50 = 20htz refresh rate)
    MILLISECONDS = 50

    #testmode toggles if packets are sent or not
    testmode = False

    
    #main loop (IMPORTANT THAT THE PACKETS ARE EVENT DRIVEN TO REDUCE REDUNANCY)
    running = True
    while running:

        pygame.event.pump()
        ##reset all motors to 128
        right_wheels.reset()
        left_wheels.reset()
        gantry.reset()
        shoulder.reset()
        elbow.reset()
        claw.reset()
        wrist.reset()

        #TRIGGER THROTTLE
        l2Throttle  = (controller.get_axis(4)+1)/2    
        r2Throttle  = (controller.get_axis(5)+1)/2
        total_throttle = r2Throttle - l2Throttle

        ##getting stick pos
        right_stick = controller.get_axis(3)
        left_stick = controller.get_axis(1)


##DRIVE FUNCTIONS##
        right_wheels.drive(right_stick, change_in_speed, mode)
        left_wheels.drive(left_stick, change_in_speed, mode)
        

# ##ARM FUNCTIONS##
    
        #check if using throttle for wrist
        using_wrist_throttle = (controller.get_button(9) == 1 and (controller.get_button(11) == 1 or controller.get_button(12) == 1 or controller.get_button(13) == 1 or controller.get_button(14) == 1))
        if not using_wrist_throttle:

            ##event update gantry motor##
            if controller.get_button(3) != 0:
                gantry.move(total_throttle, change_in_speed, mode)

            ##event update claw motor##
            if controller.get_button(2) != 0:
                claw.move(total_throttle, change_in_speed, mode)

            ##event update shoulder motor##
            if controller.get_button(1) != 0:
                shoulder.move(total_throttle, change_in_speed, mode)

            ##event update elbow motor##
            if controller.get_button(0) != 0:
                elbow.move(total_throttle, change_in_speed, mode)
        

##wrist functions##

        #check if using throttle for arm
        using_arm_throttle = (controller.get_button(9) == 1 and (controller.get_button(0) == 1 or controller.get_button(1) == 1 or controller.get_button(2) == 1 or controller.get_button(3) == 1))
        if not using_arm_throttle:

            ##event d-pad up
            if controller.get_button(11) != 0:
                wrist.move(r2Throttle, change_in_speed, 'up', mode)
            
            ##event d-pad down
            if controller.get_button(12) != 0:
                wrist.move(r2Throttle, change_in_speed, 'down', mode)

            ##event d-pad left
            if controller.get_button(13) != 0:
                wrist.move(r2Throttle, change_in_speed, 'left', mode)
            
            ##event d-pad right
            if controller.get_button(14) != 0:
                wrist.move(r2Throttle, change_in_speed, 'right', mode)
        

##PACKET ASSEMBLY AND SHIPMENT##

        #“A_elbow_wristright_wristleft_claw_gantry_shoulder”
        arm_command = f"A_{elbow.speed}_{wrist.wristright_speed}_{wrist.wristleft_speed}_{claw.speed}_{gantry.speed}_{shoulder.speed}"

        #“D_rightWheel1_rightWheel2_rightWheel3_leftWheel1_leftWheel2_leftWheel3”  
        wheels_command = f"D_{right_wheels.speed}_{right_wheels.speed}_{right_wheels.speed}_{left_wheels.speed}_{left_wheels.speed}_{left_wheels.speed}"
        
        ##print outgoing commands
        #reduce redundant commands by storing last command
        if last_A_command != arm_command:
            print(arm_command)
            await websocket.send(arm_command)      
        last_A_command = arm_command

        if last_D_command != wheels_command:
            print(wheels_command)
            await websocket.send(wheels_command)
        last_D_command = wheels_command

        for event in pygame.event.get():

            #quit program function
            if event.type == quit:
                running = False
            elif event.type == pygame.JOYBUTTONUP and event.button == 5:
                running = False 

            if event.type == pygame.JOYBUTTONUP and event.button == 8:
                if change_in_speed ==  127:
                    print("Max Speed")
                else:
                    increase_change_in_speed()
                    print(change_in_speed)
                

            if event.type == pygame.JOYBUTTONUP and event.button == 7:
                if change_in_speed == 18:
                    print('Min Speed')
                else:
                    decrease_change_in_speed()
                    print(change_in_speed)

            if event.type == pygame.JOYBUTTONUP and event.button == 6:
                if testmode == False:
                    testmode = True
                    print("Test Mode: ON")
                else:
                    testmode = False
                    print("Test Mode: OFF")

            
            if event.type == pygame.JOYBUTTONUP and event.button == 9:
                    mode = 'set'
                    print("SET SPEED MODE : ON")
            

            if event.type == pygame.JOYBUTTONDOWN and event.button == 9:
                    mode = 'throttle'
                    print("THROTTLE SPEED MODE : ON")
            

        #sets the while loop to occur every N milliseconds
        await asyncio.sleep(MILLISECONDS / 1000.0)  # Convert milliseconds to seconds for asyncio.sleep
    await websocket.close()
    print(f"Client disconnected: {path}")
    quit()

#start program
if __name__ == "__main__":
    # Start WebSocket server
    start_server = websockets.serve(send_controller_input, "localhost", 8765)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()