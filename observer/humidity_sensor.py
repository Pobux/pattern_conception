#-*- coding: utf-8 -*-
# Creation Date : 2016-10-21
# Created by : Antoine LeBel
import subject

class HumiditySensor(subject.Subject):

    def __init__(self):
        self.observer_list = []
        self.humidity = 0

    def register_observer(self, observer):
        self.observer_list.append(observer)

    def remove_observer(self, observer):
        self.observer_list.remove(observer)

    def notify_observer(self):
        """
        Peu importe le type d'observeur, on sait que celui-ci possède la méthode update.
        C'est ici que le pull VS push se décide.
        """
        for observer in self.observer_list:
            observer.update(self)
