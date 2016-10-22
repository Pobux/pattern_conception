#-*- coding: utf-8 -*-
# Creation Date : 2016-10-21
# Created by : Antoine LeBel
import observer

class WebsiteNotifier(observer.Observer):

    def update(self, HumidititySensor):
        self._connect()
        self._update_humidity(HumidititySensor.humidity)

    def _connect(self):
        #connection à la base de données du siteweb
        pass

    def _update_humidity(self, humidity):
        print("Le siteweb a été mis à jour.")
