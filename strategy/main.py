#-*- coding: utf-8 -*-
# Creation Date : 2016-10-18
# Created by : Antoine LeBel
import archive
import intranet_copy
import local_copy
import web_copy

print("Le programme démarre")
archive = archive.Archive()

try:
    print("Tentative de copy")
    archive.perform_location_copy()
except AttributeError:
    print("Le programme n'a pas encore définit son comportement de copie")

print("Le programme définit sa location")

if archive.get_location() == "web" :
    archive.set_location_copy_process(web_copy.WebCopy())
elif archive.get_location() == "intranet":
    archive.set_location_copy_process(intranet_copy.IntranetCopy())
else:
    archive.set_location_copy_process(local_copy.LocalCopy())

print("Le programme a définit son comportement selon son endroit")
archive.perform_location_copy()
