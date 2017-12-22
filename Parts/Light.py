import RPi.GPIO as GPIO

class Light:
    freq = 1
    duty = 0.5
    def __init__(self,pin1,pin2,pin3):
        self.channels = [17,22,27]
        GPIO.setup(self.channels,GPIO.OUT)
        pwm_left = GPIO.PWM(pin1,self.freq)
        pwm_right = GPIO.PWM(pin3,self.freq)

    def __setup(self):
        GPIO.setup(self.channels,GPIO.OUT)
        pwm_left = GPIO.pwm(self.channels[0],freq)
        pwm_right = GPIO.pwm(self.channels[2],freq)
        
    def headLampOn(self):
        GPIO.output(self.channels[1],GPIO.HIGH)
    def headLampOff(self):
        GPIO.output(self.channels[1],GPIO.LOW)
        
    def leftWinkerOn(self):
        self.pwm_left.start(self.duty)
    def leftWinkerOff(self):
        self.pwm_left.stop()

    def rightWinkerOn(self):
        self.pwm_right.start(self.duty)
    def rightWinkerOff(self):
        self.pwm_right.stop() 

    def clean(self):
        GPIO.cleanup(channels)
        
