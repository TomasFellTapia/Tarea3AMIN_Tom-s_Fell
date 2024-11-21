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
        vectini = np.random.randint(0,2,n)
        
        while calcularcostos(vectini,mdatos,n)>c:
            aux = vectini*mdatos[:,2].transpose()
            ind = np.argmax(aux)
            vectini[ind]=0
        msol = vectini
        vefitnes = calcularfitness(mdatos,n)
        
        vefi01 = np.sort(vefitnes)
        vefi02 = np.argsort(vefitnes)
        vectra = np.random.randint(0,2,n)
        

        
        vecprob=vectorprobabilidades(tau*-1,n)
        pos = n-1
        for j in range(numit):
            
            vecprop=vectorproporcion(vecprob,(n-j)) 
            raux = np.random.rand()
            print("Numero Aleatoreo: ",raux)
            for jj in range(n):
                print(vecprop[jj])
                if raux<=vecprop[jj]:
                    print("\n----En este lugar estamos----\n")
                    ter = vefi02[jj]
                    print(ter)


            
        sem +=1

else: 
    print("Error en el ingreso de datos")