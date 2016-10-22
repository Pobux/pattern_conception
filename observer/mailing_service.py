#-*- coding: utf-8 -*-
# Creation Date : 2016-10-21
# Created by : Antoine LeBel
import observer

class MailingService(observer.Observer):
    MIN_HUMIDITY = 20

    def update(self, HumiditySensor):
        if HumiditySensor.humidity < self.MIN_HUMIDITY:
            self._send_humidity_warning(HumiditySensor.humidity)

    def _send_humidity_warning(self, humidity):
        print("Un message courriel a été envoyé pour avertir que les plantes sont sèches!")
