#-*- coding: utf-8 -*-
# Creation Date : 2016-10-21
# Created by : Antoine LeBel
import observer

class WaterMecanism(observer.Observer):

    DESIRED_HUMIDITY = 20

    def __init__(self):
        self.sensor = None
        watering = False

    def update(self, HumiditySensor):
        """
        Ici on peut choisir, en temps fixe ou en appel constant sur le sujet
        push VS pull
        """
        self.sensor = HumiditySensor
        #push
        if HumiditySensor.humidity <= self.DESIRED_HUMIDITY:
            self.give_water()

        # pull
        # while HumiditySensor.humidity <= self.DESIRED_HUMIDITY :
            # HumiditySensor.get_state() 
            # Démarre un nouveau processus qui s'arrête seulement si watering est à False

    def give_water(self):
        print("Nom Nom de l'eau pour les plantes. Taux dangereux : " + str(self.sensor.humidity))
