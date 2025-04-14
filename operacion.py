import re

def separar (valores):
    if valores == None:
        return 0
    else:
        bloque = re.split(r'(\+|\-|\*|\/)', valores)
        return bloque

def numeros(bloque):
    segmento= []
    for bloques in bloque:
        if bloques.isnumeric():
            segmento.append(int(bloques))
            print("es un numero")
        else:
            segmento.append(bloques)
            print("es un operador")
    return segmento


def operar(bloque):
    i = 0
    while i < len(bloque):
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
    print("resultado", bloque[0])
    return bloque[0]
