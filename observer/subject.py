#-*- coding: utf-8 -*-
# Creation Date : 2016-10-21
# Created by : Antoine LeBel
class Subject():
    """
    Ceci est une interface
    """
    def register_observer(self, observer):
        NotImplementedError("La classe %s doit implémenter :".format(self.__class__.__name__))

    def remove_observer(self, observer):
        NotImplementedError("La classe %s doit implémenter :".format(self.__class__.__name__))

    def notify_observer(self):
        NotImplementedError("La classe %s doit implémenter :".format(self.__class__.__name__))
