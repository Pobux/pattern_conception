#-*- coding: utf-8 -*-
# Creation Date : 2016-10-18
# Created by : Antoine LeBel
class Program():
    """
    Classe abstraite
    À noter que cette n'est pas obligé d'être abstraite.
    La délégation peut très bien ce faire sans celle-ci.
    """
    def __init__(self):
        self.location_copy_process = None

    def perform_location_copy(self):
        """
        C'est de cette manière qu'un programme délègue une tâche par composition.
        Le programme (Program) ne sait pas comment faire une copie
        """
        self.location_copy_process.copy()

    #On a besoin d'un setter pour que ce soit dynamique
    def set_location_copy_process(self, location_copy_process):
        """
        Ici on a le choix entre local, intranet et web.
        """
        self.location_copy_process = location_copy_process

    def get_location(self):
        """
        Default is web
        """
        return "web"
