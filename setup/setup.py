''' 
setup v0.1 
qui affiche le setup de la machine  python
changelog:
dec 17 : initialisation
'''

import sys 
import os
import datetime


def printseparator():
    """ fonction qui affiche la séparation"""
    print('-' * 50)


printseparator()
a = 'bonjour monde'
print(a)   # j'affiche l'objet a

printseparator()
print(sys.executable)
print(sys.platform)
print(sys.path)

print(sys.version_info)

v = sys.version_info

# print(type(v)) # type de sys

# print(dir(v))  # introspectin de sys

print(f"Python version {v.major}.{v.minor}.{v.micro}")
print("Python version {}.{}.{}".format(v.major,v.minor,v.micro))

print("Python version %s.%s.%s" % (v.major,v.minor,v.micro))  # Version 2.7 déprécié
print("Environnement PythonPath :" + os.getenv("PYTHONPATH", "vide"))

print(datetime)
print(datetime.__file__)

dt = datetime.datetime.now()
print(f"Date et heure {dt} - Année {dt.year}")

printseparator()


help(printseparator)
