import time

from Adafruit_PWM_Servo_Driver import PWM
from Servo import Servo


if __name__ == '__main__':
    # mg995
    servo2 = Servo(channel=0, min=150, max=530, freq=100) # mg995

    # sg90
    # Servo pan
    # servo2 = Servo(channel=2, min=250, max=380, freq=50)

    # sg90 2
    # servo tilt
    # servo3 = Servo(channel=1, min=240, max=327, freq=50)

    time.sleep(4)
    servo2.move_to(0)
    # # servo3.move_to(0)
    # #
    time.sleep(4)
    servo2.move_to(1)
    #
    # time.sleep(0.1)
    # servo2.move_to(0)
    # # servo3.move_to(1)
    #
    # #
    time.sleep(4)
    # servo2.move_to(0.5)
    # time.sleep(1)
    # servo3.move_to(0.5)
    pwm = PWM(0x40)
    pwm.setPWMFreq(50)
    pwm.softwareReset()
    print('done')
