#-*- coding: utf-8 -*-
# Creation Date : 2016-10-21
# Created by : Antoine LeBel
import observer

class MailingService(observer.Observer):
    MIN_HUMIDITY = 20
    def __init__(self):
        self.sensor = None

    def update(self, HumiditySensor):
        self.sensor = HumiditySensor

        if HumiditySensor.humidity < self.MIN_HUMIDITY:
            self._send_humidity_warning()

    def _send_humidity_warning(self):
        print("Un message courriel a été envoyé pour avertir que les plantes sont sèches!")
