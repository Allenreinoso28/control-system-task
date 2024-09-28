class Motor():
    def __init__(self):
        self.stationary = 128
        self.speed = self.stationary
    
    def update_speed(self, acceleration):
        self.speed = self.stationary + acceleration


class WheelMotor(Motor):
    def __init__(self):
        super().__init__()

    def drive(self, axis_value, change_in_speed, mode):
        if mode == 'throttle':
            #forward (CW)(0 to -1)
            if axis_value < -0.05:
                self.speed = round(self.stationary - (127 * axis_value))   
            #backward (CCW)(0 to 1)
            elif axis_value > 0.05:
                self.speed = round(self.stationary - (128 * axis_value))

        if mode == 'set':
            if axis_value > 0.3:
                self.speed = self.stationary - 1 - change_in_speed
            elif axis_value < -0.3:
                self.speed = self.stationary + change_in_speed

    def reset(self):
        self.speed = self.stationary


class ArmMotor(Motor):
    def __init__(self):
        super().__init__()

    def move(self, throttle, change_in_speed, mode):
        if mode == 'throttle':
            if throttle > 0:
                self.speed = round(self.stationary + (127 * throttle))
            if throttle < 0:
                self.speed = round(self.stationary + (128 * throttle))
        if mode == 'set':
            if throttle > 0: 
                self.speed = self.stationary + change_in_speed
            if throttle < 0:
                self.speed = self.stationary - 1 - change_in_speed

    def reset(self):
        self.speed = self.stationary


class WristMotors(Motor):
    def __init__(self):
        super().__init__()
        self.wristleft_speed = self.stationary
        self.wristright_speed = self.stationary

    def move(self, throttle, change_in_speed, direction, mode):
        if mode == 'throttle':
            if direction == 'up':
                # move claw upwards
                if throttle > 0:
                    self.wristleft_speed = round(self.stationary + (127 * throttle))
                    self.wristright_speed = round(self.stationary - (128 * throttle))

            elif direction == 'down':
                # move claw downwards
                if throttle > 0:
                    self.wristleft_speed = round(self.stationary - (128 * throttle))
                    self.wristright_speed = round(self.stationary + (127 * throttle))
            
            elif direction == 'left':
                # spin claw CCW
                if throttle > 0:
                    self.wristleft_speed = round(self.stationary - (128 * throttle))
                    self.wristright_speed = round(self.stationary - (128 * throttle))

            elif direction == 'right':
                # spin claw CW
                if throttle > 0:
                    self.wristleft_speed = round(self.stationary + (127 * throttle))
                    self.wristright_speed = round(self.stationary + (127 * throttle))
##SET SPEED MODE##
        if mode == 'set':
            if direction == 'up':
                # move claw upwards
                    self.wristleft_speed = self.stationary + change_in_speed
                    self.wristright_speed = self.stationary - 1 - change_in_speed

            elif direction == 'down':
                # move claw downwards
                    self.wristleft_speed = self.stationary - 1 - change_in_speed
                    self.wristright_speed = self.stationary + change_in_speed
            
            elif direction == 'left':
                # spin claw CCW
                    self.wristleft_speed = self.stationary - 1 - change_in_speed
                    self.wristright_speed = self.stationary - 1 - change_in_speed

            elif direction == 'right':
                # spin claw CW
                    self.wristleft_speed = self.stationary + change_in_speed
                    self.wristright_speed = self.stationary + change_in_speed

    def reset(self):
        self.wristleft_speed = self.stationary
        self.wristright_speed = self.stationary