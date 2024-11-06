import sys
import numpy as np # type: ignore
import pandas as pd # type: ignore
import time 

if len(sys.argv)== 5:
    sem = int(sys.argv[1])


else: 
    print("Error en el ingreso de datos")