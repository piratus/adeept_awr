#!/usr/bin/python3
import time
from rpi_ws281x import *

# LED strip configuration:
LED_COUNT = 6  # Number of LED pixels.
LED_PIN = 12  # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10  # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53


class LED:
    def __init__(self):
        self.LED_COUNT = LED_COUNT  # Number of LED pixels.
        self.LED_PIN = LED_PIN  # GPIO pin connected to the pixels (18 uses PWM!).
        self.LED_FREQ_HZ = LED_FREQ_HZ  # LED signal frequency in hertz (usually 800khz)
        self.LED_DMA = LED_DMA  # DMA channel to use for generating signal (try 10)
        self.LED_BRIGHTNESS = (
            LED_BRIGHTNESS  # Set to 0 for darkest and 255 for brightest
        )
        self.LED_INVERT = LED_INVERT  # True to invert the signal (when using NPN transistor level shift)
        self.LED_CHANNEL = LED_CHANNEL  # set to '1' for GPIOs 13, 19, 41, 45 or 53

        # Create NeoPixel object with appropriate configuration.
        self.strip = Adafruit_NeoPixel(
            self.LED_COUNT,
            self.LED_PIN,
            self.LED_FREQ_HZ,
            self.LED_DMA,
            self.LED_INVERT,
            self.LED_BRIGHTNESS,
            self.LED_CHANNEL,
        )

        # Initialize the library (must be called once before other functions).
        self.strip.begin()

    def colorWipe(self, color, wait_ms=0):
        """Wipe color across display a pixel at a time."""
        for i in range(self.strip.numPixels()):
            self.set_color(i, color)
            if wait_ms:
                time.sleep(wait_ms / 1000.0)

    def set_color(self, pixel, color):
        self.strip.setPixelColor(pixel, color)
        self.strip.show()


if __name__ == "__main__":
    led = LED()
    try:
        while True:
            led.colorWipe(Color(255, 0, 0), 25)
            led.colorWipe(Color(0, 255, 0), 25)
            led.colorWipe(Color(0, 0, 255), 25)
    finally:
        led.colorWipe(Color(0, 0, 0))
