import sys
import numpy as np # type: ignore
import pandas as pd # type: ignore
import time 
import os
import gc
from Funciones.Funciones01 import *
sep = os.path.sep
if len(sys.argv)== 6:
    nom = str(sys.argv[1])
    sem = int(sys.argv[2])
    numit = int(sys.argv[3])
    prue = int(sys.argv[4])
    tau = float(sys.argv[5])
    nom = "Entradas"+sep+nom+".csv"
    n,c,z,mdatos = valores(nom)
    for i in range(prue):
        np.random.seed(sem)
        vectini = np.random.randint(2,size=n)
        print("antes del cambio\n",vectini)
        aux = vectini*mdatos[:,2].transpose()
        ind=np.argmax(np.cumsum(aux)>c)
        vectini[ind:]=0
        print("Despues del cambio\n",vectini)
        print("Coste Maximo: ",c,"\nCoste de la Mochila: ",calcularcostos(vectini,mdatos,n))
        
        
        vecprob=vectorprobabilidades(tau*-1,n)
        print(vecprob)
        for j in range(numit):
            vecprop=vectorproporcion(vecprob,(n-j)) 
            print(vecprop)
            
        sem +=1

else: 
    print("Error en el ingreso de datos")