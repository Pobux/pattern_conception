#-*- coding: utf-8 -*-
# Creation Date : 2016-10-21
# Created by : Antoine LeBel
class Observer():
    """
    Interface
    """
    def update(self, subject):
        NotImplementedError("La classe %s doit implémenter :".format(self.__class__.__name__))
