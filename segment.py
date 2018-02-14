import time

from neopixel import *
from random import randint

LEDS        = 12     # Aantel LEDS
PIN         = 18     # GPIO 18 / PIN 12
BRIGHTNESS  = 55     # min 0 / max 255

def resetLeds(wait_ms=10):
        for i in range(ring.numPixels()):
                ring.setPixelColor(i, Color(0,0,0))
                ring.show()

def showLeds():
    ring.show()

ring = Adafruit_NeoPixel(LEDS, PIN, 800000, 5, False, BRIGHTNESS)
ring.begin()
resetLeds()

# Segmenten
class Segment():
    segment = 0
    startLed = 0

    def __init__(self, segment):
        self.segment = segment
        self.startLed = segment * 3

    def ledsOn(self):
        print("rock of roll koekoek")
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
