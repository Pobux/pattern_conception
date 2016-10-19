#-*- coding: utf-8 -*-
# Creation Date : 2016-10-18
# Created by : Antoine LeBel
from program import Program

class Archive(Program):
    """
    On ne sait pas à quelle location le programme Archive sera appelé.
    Ce sera déterminé dynamiquement.
    """
    def __init__(self):
        self.location_copy_process = None
