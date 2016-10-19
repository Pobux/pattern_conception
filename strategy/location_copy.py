#-*- coding: utf-8 -*-
# Creation Date : 2016-10-18
# Created by : Antoine LeBel
class LocationCopy():
    """
    Interface
    """
    def location_copy_process(self):
        """
        Cette méthode est celle utilisé dans la classe Program
        """
        NotImplementedError("La classe %s doit implémenter :".format(self.__class__.__name__))
