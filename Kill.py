import time

from Adafruit_PWM_Servo_Driver import PWM
from Servo import Servo


if __name__ == '__main__':
    pwm = PWM(0x40)
    pwm.setPWMFreq(50)
    pwm.softwareReset()
    print('done')
