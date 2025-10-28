"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

def pregunta_13():
    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """
    df=cargar_datos()[0]
    bd=cargar_datos()[1]
    # Unir las dos bases de datos por cada valor en C0
    # que es nuestra clave para ambas bases de datos
    # inner Esto mantiene solo las filas donde c0 está presente en ambos DataFrames
    bd_conjunta=pd.merge(df,bd,how="inner",on="c0")
    bd_conjunta=bd_conjunta.groupby("c1")["c5b"].sum()
    return bd_conjunta

def cargar_datos():
    df = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    bd= pd.read_csv("files/input/tbl2.tsv", sep="\t")
    return df, bd