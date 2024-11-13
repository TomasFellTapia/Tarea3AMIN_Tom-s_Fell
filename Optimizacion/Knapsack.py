import sys
import numpy as np # type: ignore
import pandas as pd # type: ignore
import time 
import os
from Funciones.Funciones01 import *
sep = os.path.sep
if len(sys.argv)== 6:
    nom = str(sys.argv[1])
    sem = int(sys.argv[2])
    numit = int(sys.argv[3])
    prue = int(sys.argv[4])
    tau = float(sys.argv[5])
    nom = "Entradas"+sep+nom+".csv"
    n,c,z = valores(nom)
    for i in range(prue):
        np.random.seed(sem)
        print(n," ",type(n),"  ",c,"  ",type(c)," ",z," ",type(z),".")
       
        print("Semilla: ",sem," ",type(sem))

        vectini = np.random.randint(2,size=n)
        valores(nom)
        print (vectini)
        sem +=1

else: 
    print("Error en el ingreso de datos")