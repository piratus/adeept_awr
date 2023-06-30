#!/usr/bin/env python3
import time
import RPi.GPIO as GPIO

# motor_EN_A: Pin7  |  motor_EN_B: Pin11
# motor_A:  Pin8,Pin10    |  motor_B: Pin13,Pin12

Motor_A_EN = 4
Motor_B_EN = 17

Motor_A_Pin1 = 26
Motor_A_Pin2 = 21
Motor_B_Pin1 = 27
Motor_B_Pin2 = 18

DIR_FORWARD = 1
DIR_BACKWARD = 0

LEFT_FORWARD = 1
LEFT_BACKWARD = 0

RIGHT_FORWARD = 0
RIGHT_BACKWARD = 1

pwm_A = None
pwm_B = None


def motor_stop():
    """Motor stops"""
    GPIO.output(Motor_A_Pin1, GPIO.LOW)
    GPIO.output(Motor_A_Pin2, GPIO.LOW)
    GPIO.output(Motor_A_EN, GPIO.LOW)

    GPIO.output(Motor_B_Pin1, GPIO.LOW)
    GPIO.output(Motor_B_Pin2, GPIO.LOW)
    GPIO.output(Motor_B_EN, GPIO.LOW)


def setup():
    """Motor initialization"""
    global pwm_A, pwm_B
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Motor_A_EN, GPIO.OUT)
    GPIO.setup(Motor_B_EN, GPIO.OUT)
    GPIO.setup(Motor_A_Pin1, GPIO.OUT)
    GPIO.setup(Motor_A_Pin2, GPIO.OUT)
    GPIO.setup(Motor_B_Pin1, GPIO.OUT)
    GPIO.setup(Motor_B_Pin2, GPIO.OUT)

    motor_stop()
    try:
        pwm_A = GPIO.PWM(Motor_A_EN, 1000)
        pwm_B = GPIO.PWM(Motor_B_EN, 1000)
    except:
        print("Failed to init motors")
        pass


def motor_left(status, direction, speed):
    """Motor 2 positive and negative rotation"""
    global pwm_B
    if status == 0:  # stop
        GPIO.output(Motor_B_Pin1, GPIO.LOW)
        GPIO.output(Motor_B_Pin2, GPIO.LOW)
        GPIO.output(Motor_B_EN, GPIO.LOW)
    else:
        if direction == DIR_BACKWARD:
            GPIO.output(Motor_B_Pin1, GPIO.HIGH)
            GPIO.output(Motor_B_Pin2, GPIO.LOW)
            pwm_B.start(100)
            pwm_B.ChangeDutyCycle(speed)
        elif direction == DIR_FORWARD:
            GPIO.output(Motor_B_Pin1, GPIO.LOW)
            GPIO.output(Motor_B_Pin2, GPIO.HIGH)
            pwm_B.start(0)
            pwm_B.ChangeDutyCycle(speed)


def motor_right(status, direction, speed):
    """Motor 1 positive and negative rotation"""
    global pwm_A
    if status == 0:  # stop
        GPIO.output(Motor_A_Pin1, GPIO.LOW)
        GPIO.output(Motor_A_Pin2, GPIO.LOW)
        GPIO.output(Motor_A_EN, GPIO.LOW)
    else:
        if direction == DIR_FORWARD:  #
            GPIO.output(Motor_A_Pin1, GPIO.HIGH)
            GPIO.output(Motor_A_Pin2, GPIO.LOW)
            pwm_A.start(100)
            pwm_A.ChangeDutyCycle(speed)
        elif direction == DIR_BACKWARD:
            GPIO.output(Motor_A_Pin1, GPIO.LOW)
            GPIO.output(Motor_A_Pin2, GPIO.HIGH)
            pwm_A.start(0)
            pwm_A.ChangeDutyCycle(speed)
    return direction


def move(speed, direction, turn, radius=0.6):  # 0 < radius <= 1
    # speed = 100
    if direction == "forward":
        if turn == "right":
            motor_left(0, LEFT_BACKWARD, int(speed * radius))
            motor_right(1, RIGHT_FORWARD, speed)
        elif turn == "left":
            motor_left(1, LEFT_FORWARD, speed)
            motor_right(0, RIGHT_BACKWARD, int(speed * radius))
        else:
            motor_left(1, LEFT_FORWARD, speed)
            motor_right(1, RIGHT_FORWARD, speed)
    elif direction == "backward":
        if turn == "right":
            motor_left(0, LEFT_FORWARD, int(speed * radius))
            motor_right(1, RIGHT_BACKWARD, speed)
        elif turn == "left":
            motor_left(1, LEFT_BACKWARD, speed)
            motor_right(0, RIGHT_FORWARD, int(speed * radius))
        else:
            motor_left(1, LEFT_BACKWARD, speed)
            motor_right(1, RIGHT_BACKWARD, speed)
    else:
        if turn == "right":
            motor_left(1, LEFT_BACKWARD, speed)
            motor_right(1, RIGHT_FORWARD, speed)
        elif turn == "left":
            motor_left(1, LEFT_FORWARD, speed)
            motor_right(1, RIGHT_BACKWARD, speed)
        else:
            motor_stop()


def destroy():
    """Release resources"""
    motor_stop()
    GPIO.cleanup()


if __name__ == "__main__":
    try:
        speed_set = 75
        setup()
        motor_left(1, 1, speed_set)
        motor_right(1, 1, speed_set)
        time.sleep(1)
        motor_left(1, 0, speed_set)
        motor_right(1, 0, speed_set)
        time.sleep(1)
        motor_left(1, 1, speed_set)
        motor_right(1, 1, speed_set)
        time.sleep(1)
        motor_left(1, 0, speed_set)
        motor_right(1, 0, speed_set)
        time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        destroy()
