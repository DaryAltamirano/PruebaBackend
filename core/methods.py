"""
Módulo de methods.

@author: DaryPte

NOTA IMPORTANTE PARA TENER EN CUENTA EN TODAS LAS FUNCIONES DE ESTE MODULO:
        Todas las funciones son usadas en main.py:
"""

SONGS = [
    "brr, fiu, cric-cric, brrah",
    "pep, birip, trri-trri, croac",
    "bri-bri, plop, cric-cric, brrah"
    ]


def isValid(sound:str)->bool:
    """Valida la existencia del tono musical en alguna cancion 
    Parámetros:
        sound (str): tono.
    Retorna:
        bool: Existencia del tono musical
    """    
    unique=''
    result=[]
    for i, v in enumerate(SONGS):
        unique+= "," + v    
    
    for v in list(set(unique.split(","))):
        if(v !=''):
            result.append(v.strip())

    return sound in result if True else False


def sound_missing(sound:str)->str:
    """Obtiene el resto de la cancion a partir del tono musical elegido:
        sound (str): tono.
    Retorna:
        str: La continuacion del tono musical
    """
    for v in SONGS:
        index = v.find(sound)
        if(index>=0 and (index + len(sound) !=len(v)) ):
            return v[v.find(sound)+len(sound): ].strip(",").strip(" ")
    return ''
            