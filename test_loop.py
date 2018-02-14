# Demoscript NeoPixel Ring (12 led)
# https://raspberrytips.nl

import time

from neopixel import *
from random import randint

LEDS        = 12     # Aantel LEDS
PIN         = 18     # GPIO 18 / PIN 12
BRIGHTNESS  = 55     # min 0 / max 255

ring = Adafruit_NeoPixel(LEDS, PIN, 800000, 5, False, BRIGHTNESS)

# Segmenten
class Segment():
    segment = 0
    startLed = 0

    def __init__(self, segment):
        self.segment = segment
        self.startLed = segment * 3

    def ledsOn(self):
        ring.setPixelColor(self.startLed, Color(255,0,0))
        ring.setPixelColor(self.startLed + 1, Color(255,0,0))
        ring.setPixelColor(self.startLed + 2, Color(255,0,0))

    def ledsOff(self):
        ring.setPixelColor(self.startLed, Color(0,0,0))
        ring.setPixelColor(self.startLed + 1, Color(0,0,0))
        ring.setPixelColor(self.startLed + 2, Color(0,0,0))

    def showProc(self, proc):
        kleur = Color(proc, 255-proc, 0);
        ring.setPixelColor(self.startLed, kleur)
        ring.setPixelColor(self.startLed + 1, kleur)
        ring.setPixelColor(self.startLed + 2, kleur)

# LEDS
# def loopLed(ledNr):
#     ring.setPixelColor(ledNr,Color(0,0,255))    # RGB
#     ring.show()
#
# def resetLeds(color, wait_ms=10):
#         for i in range(ring.numPixels()):
#                 ring.setPixelColor(i, Color(0,0,0))
#                 ring.show()
#




if __name__ == '__main__':
    ring.begin()

    seg0 = Segment(0)
    seg0.ledsOn()
    ring.show()
    channelIntensity = 0
    while channelIntensity < 255:
        time.sleep(0.1)
        channelIntensity = channelIntensity + 1
        seg0.showProc(channelIntensity)
        print(seg0, channelIntensity)
        ring.show()

    seg1 = Segment(1)
    seg1.ledsOn()
    ring.show()
    channelIntensity = 0
    while channelIntensity < 255:
        time.sleep(0.1)
        channelIntensity = channelIntensity + 1
        seg1.showProc(channelIntensity)
        print(seg1, channelIntensity)
        ring.show()

    print("happy Ending")





    # seg2 = Segment(1)
    # seg2.setLeds(2)

        # ring.begin()
        # resetLeds (ring)
        # ledNr = 0
        # while True:
        #     time.sleep(1)
        #     ledNr = ledNr % 12
        #     loopLed(ledNr)
        #     ledNr = ledNr + 1









        # for t in range (0, 5, 1):
        #         loopLed (ring,Color(KLEUR_G, KLEUR_R, KLEUR_B),100)
        #
        # resetLeds (ring,Color(0,0,0))
