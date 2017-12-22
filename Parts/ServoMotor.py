import RPi.GPIO as GPIO

class ServoMotor:
    '''PWM period may be 50Hz(20ms) 
       Duty Cycle is 0.5~2.4ms ~0.5ms is -90deg /~2.4ms +90deg'''
    #pulsetime
    highest, lowest = 2.4, 0.5
    middle =  (highest+lowest)/2
    
    def __init__(self,pin):
        self.freq = 50.0
        self.period = 1000.0/self.freq
        self.pin = pin
        GPIO.setup(pin,GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin,self.freq)
        #duty ratio
        self.right = self.highest/ self.period * 100
        self.left = self.lowest / self.period * 100
        self.straight = self.middle/ self.period * 100
        self.pwm.start(self.straight)

    def __steeringControl(self,percentage):
        n = (self.right - self.straight)/100
        return percentage * n  

    def steeringControl(self,percentage):
        self.pwm.start(self.straight + self.__steeringControl(percentage))
        
    def servoControl(self,dir):
        if dir == "left":
            self.pwm.start(self.left)
        elif dir == "right":
            self.pwm.start(self.right)
        else:
            self.pwm.start(self.straight)

    def servoReset(self):
        self.pwm.start(self.straight)

    def clean(self):
        GPIO.cleanup(self.pin)
    
        
def test():
    import time
    GPIO.setmode(GPIO.BCM)
    servo = ServoMotor(4)
    print("middle")
    time.sleep(3)
    print("left")
    servo.steeringControl(-100)
    time.sleep(3)
    servo.steeringControl(-50)
    time.sleep(3)
    print("right")
    servo.steeringControl(100)
    time.sleep(3)
    servo.steeringControl(50)
    time.sleep(3)
    servo.reset()

if __name__ == "__main__":
    test()
