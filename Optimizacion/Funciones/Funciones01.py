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
    df = df.astype('int32').to_numpy()
    return n,c,z,df

def vectorprobabilidades(tau,n,dtype=float):
    vec = np.arange(0,n,dtype=float)
    for i in range (n):
        vec[i]=(i+1)**tau
    return vec

def vectorproporcion(vecprob,n):
    vecp = np.arange(0,n,dtype=float)
    total = vecprob.sum()
    for i in range(n):
        vecp[i]=vecprob[i]/total
    return vecp

def calcularcostos(vecs,mdatos,n):
    
    pes = (mdatos[:,2]*vecs).sum()
    return pes

def calcularvalor(vecs,mdatos,n):
    val = (mdatos[:,1]*vecs).sum()
    return val
def calcularfitness(mdatos,n):
    vecf = np.arange(0,n,dtype=float)
    vecf = (mdatos[:,1]/mdatos[:,2]).transpose()
    return vecf