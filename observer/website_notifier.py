#-*- coding: utf-8 -*-
# Creation Date : 2016-10-21
# Created by : Antoine LeBel
import observer

class WebsiteNotifier(observer.Observer):

    def __init__(self):
        self.sensor = None

    def update(self, HumidititySensor):
        self.sensor = HumidititySensor
        self._connect()
        self._update_humidity()

    def _connect(self):
        #connection à la base de données du siteweb
        pass

    def _update_humidity(self):
        print("Le siteweb a été mis à jour " + str(self.sensor.humidity) + ".")
