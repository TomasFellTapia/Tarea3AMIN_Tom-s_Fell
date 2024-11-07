import sys
import numpy as np # type: ignore
import pandas as pd # type: ignore
import time 
from Funciones.Funciones01 import *
if len(sys.argv)== 5:
    nom = str(sys.argv[1])
    sem = int(sys.argv[2])
    numit = int(sys.argv[3])
    tau = float(sys.argv[4])
    np.random.seed(sem)
    nom = "./Entradas/"+nom+".csv"
    n = 50
    print(nom)

    vectini = np.random.randint(2,size=n)
    valores(nom)
    print (vectini)

else: 
    print("Error en el ingreso de datos")