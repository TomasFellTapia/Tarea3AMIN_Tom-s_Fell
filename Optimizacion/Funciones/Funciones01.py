import pandas as pd # type: ignore
import numpy as np # type: ignore
def valores(archivo):
    
    df = pd.read_table(archivo, header=None)
    n = int(df[0][1].split()[1])
    c = int(df[0][2].split()[1])
    z = int(df[0][3].split()[1])
    df.drop(df.index[0:5],axis=0,inplace=True)
    df.drop(df.tail(1).index,axis=0,inplace=True)
    df = df[0].str.split(",",expand=True)
    df = df.astype('int64').to_numpy()
    print(df)
   
    
    return n,c,z

