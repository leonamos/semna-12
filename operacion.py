import re

def separar (valores):
    if valores == None:
        return 0
    else:
        bloque = re.split(r'(\+|\-|\*|\/)', valores)
        return bloque

def numeros(valores):
    bloques= []
    