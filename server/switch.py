from typing import Optional

from gpiozero import LEDBoard

PORT_0_PIN = 5
PORT_1_PIN = 6
PORT_2_PIN = 13


leds = LEDBoard(PORT_0_PIN, PORT_1_PIN, PORT_2_PIN)


def switch(port: int, status: Optional[bool] = None):
    """
    Set port status or toggle if status omitted
    :param port: Port from 0 to 2
    :param status: on if True, off if False, toggle if None
    """
    if status is None:
        leds.toggle(port)
    elif status:
        leds.on(port)
    else:
        leds.off(port)


def set_all_off():
    """Set all ports off"""
    leds.off()


def set_all_on():
    """Set all ports on"""
    leds.on()
