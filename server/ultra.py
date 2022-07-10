#!/usr/bin/python3
from gpiozero import DistanceSensor

TRIGGER_PIN = 11
ECHO_PIN = 8


def get_distance():
    sens = DistanceSensor(ECHO_PIN, TRIGGER_PIN)
    return sens.distance


if __name__ == '__main__':
    print('Scanning...')
    print('Distance', get_distance(), sep=': ')
