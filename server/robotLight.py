import time
from rpi_ws281x import Adafruit_NeoPixel, Color
import threading


class RobotLight(threading.Thread):
    def __init__(self, *args, **kwargs):
        self.LED_COUNT = 6  # Number of LED pixels.
        self.LED_PIN = 12  # GPIO pin connected to the pixels (18 uses PWM!).
        self.LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
        self.LED_DMA = 10  # DMA channel to use for generating signal (try 10)
        self.LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
        self.LED_INVERT = (
            False  # True to invert the signal (when using NPN transistor level shift)
        )
        self.LED_CHANNEL = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53

        self.colorBreathR = 0
        self.colorBreathG = 0
        self.colorBreathB = 0
        self.breathSteps = 10

        self.lightMode = "none"  # 'none' 'police' 'breath'

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

        super(RobotLight, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()
        self.__flag.clear()

    def setColor(self, R, G, B):
        """Wipe color across display a pixel at a time."""
        color = Color(int(R), int(G), int(B))
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, color)
            self.strip.show()

    def setSomeColor(self, R, G, B, ID):
        color = Color(int(R), int(G), int(B))
        # print(int(R),'  ',int(G),'  ',int(B))
        for i in ID:
            self.strip.setPixelColor(i, color)
            self.strip.show()

    def pause(self):
        self.lightMode = "none"
        self.setColor(0, 0, 0)
        self.__flag.clear()

    def resume(self):
        self.__flag.set()

    def police(self):
        self.lightMode = "police"
        self.resume()

    def policeProcessing(self):
        while self.lightMode == "police":
            for i in range(0, 3):
                self.setSomeColor(0, 0, 255, [0, 1, 2, 3, 4, 5])
                time.sleep(0.05)
                self.setSomeColor(0, 0, 0, [0, 1, 2, 3, 4, 5])
                time.sleep(0.05)
            if self.lightMode != "police":
                break
            time.sleep(0.1)
            for i in range(0, 3):
                self.setSomeColor(255, 0, 0, [0, 1, 2, 3, 4, 5])
                time.sleep(0.05)
                self.setSomeColor(0, 0, 0, [0, 1, 2, 3, 4, 5])
                time.sleep(0.05)
            time.sleep(0.1)

    def breath(self, R_input, G_input, B_input):
        self.lightMode = "breath"
        self.colorBreathR = R_input
        self.colorBreathG = G_input
        self.colorBreathB = B_input
        self.resume()

    def breathProcessing(self):
        while self.lightMode == "breath":
            for i in range(0, self.breathSteps):
                if self.lightMode != "breath":
                    break
                self.setColor(
                    self.colorBreathR * i / self.breathSteps,
                    self.colorBreathG * i / self.breathSteps,
                    self.colorBreathB * i / self.breathSteps,
                )
                time.sleep(0.03)
            for i in range(0, self.breathSteps):
                if self.lightMode != "breath":
                    break
                self.setColor(
                    self.colorBreathR - (self.colorBreathR * i / self.breathSteps),
                    self.colorBreathG - (self.colorBreathG * i / self.breathSteps),
                    self.colorBreathB - (self.colorBreathB * i / self.breathSteps),
                )
                time.sleep(0.03)

    def lightChange(self):
        if self.lightMode == "none":
            self.pause()
        elif self.lightMode == "police":
            self.policeProcessing()
        elif self.lightMode == "breath":
            self.breathProcessing()

    def run(self):
        while 1:
            self.__flag.wait()
            self.lightChange()
            pass


if __name__ == "__main__":
    RL = RobotLight()
    try:
        RL.start()
        RL.breath(70, 70, 0)
        RL.pause()
        # time.sleep(2)
        # RL.police()
        time.sleep(1)
    except:
        RL.setColor(0, 0, 0)
    finally:
        print("Exiting...")
        RL.setColor(0, 0, 0)
