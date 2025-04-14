import re

def separar (valores):
    if valores == None:
        return []
    else:
        bloque = re.split(r'(\+|\-|\*|\/)', valores)
        return bloque

def numeros(bloque):
    segmento= []
    for bloques in bloque:
        if bloques.isnumeric():
            segmento.append(int(bloques))
        else:
            segmento.append(bloques)
    return segmento


def operar(bloque):
    if not isinstance(bloque, list):
        raise typeError("El argumento debe ser una lista")

    i = 0
    while i < len (bloque):
        if bloque[i] == "*":
            resultado = bloque[i - 1] * bloque[i + 1]
            bloque[i - 1:i + 2] = [resultado]
            i -= 1
        elif bloque[i] == "/":
            resultado = bloque[i - 1] / bloque[i + 1]
            bloque[i - 1:i + 2] = [resultado]
            i -= 1
        elif bloque[i] == "+":
            resultado = bloque[i - 1] + bloque[i + 1]
            bloque[i - 1:i + 2] = [resultado]
            i -= 1
        elif bloque[i] == "-":
            resultado = bloque[i - 1] - bloque[i + 1]
            bloque[i - 1:i + 2] = [resultado]
            i -= 1
        i += 1
      
    return bloque
