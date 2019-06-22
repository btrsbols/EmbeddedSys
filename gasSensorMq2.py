import math
import sys
import time
from adc import ADC


class GroveGasSensorMQ2:

    def __init__(self, channel):
        self.channel = channel
        self.adc = ADC()

    @property
    def MQ2(self):
        value = self.adc.read(self.channel)
        return value

Grove = GroveGasSensorMQ2


def main():

    sensor = GroveGasSensorMQ2(1)

    print('Detecting...')
    while True:
        print('Gas value: {0}'.format(sensor.MQ2))
        time.sleep(.2)

if __name__ == '__main__':
    main()