from Archivos.Variables import *

print(aventures)

def formatText(text,lenLine,split):
    resultado = ""
    linia = ""
    palabras = text.split(split)
    for palabra in palabras:
        prevision = len(linia + palabra)
        if prevision > lenLine:

            if resultado != "":
                resultado += "\n" + linia
            else:
                resultado += linia
            linia = palabra + " "
        else:
            linia += palabra + " "
    
    resultado += "\n" + linia
    
    return resultado

def getHeader(text):
    resultado = 120*"*" + "\n" + text.center(120,"=") + "\n" + 120*"*"
    return resultado
 
    
def getFormatedBodyColumns(tupla_texts,tupla_sizes,margin=0):
    datos = {}
    max_lin = 0
    resultado = ""

    for i in range(len(tupla_texts)):
        datos[len(datos) + 1] = formatText(tupla_texts[i],tupla_sizes[i]-margin,split=" ")

        datos[i+1] = datos[i+1].split("\n")

        if len(datos[i+1]) > max_lin:
            max_lin = len(datos[i+1])

    for i in range(max_lin):
        for columna in datos:
            for fila in datos[columna]:
                if i < len(datos[columna]):
                    if datos[columna][i] == fila:
                        resultado += fila.ljust(tupla_sizes[columna-1])
            resultado += " "
        resultado += "\n" 

    return resultado



#-----------------PRUEBAS----------------------

#print(formatText(text1,20,split=" "))

#print(getHeader("text"))

#print(getFormatedBodyColumns((text1,text1,text1),(20,30,50),margin=2))


#-----------------PERSONALIZAR----------------------

def cifrar(linia):
    abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz1234567890°|!\"#$%&/()=?¡¿'´+*~{}[]¬\\,.;:-_<>@"
    resultado = ""
    linia = linia.replace(" ","")
    for caracter in linia:
        if caracter in abecedario:
            posicion = abecedario.index(caracter)
            nueva_posicion = (posicion + 13) % len(abecedario)
            resultado += abecedario[nueva_posicion]
        else:
            resultado += caracter
    return resultado

def descifrar(linia):
    abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz1234567890°|!\"#$%&/()=?¡¿'´+*~{}[]¬\\,.;:-_<>@"
    resultado = ""
    for caracter in linia:
        if caracter in abecedario:
            posicion = abecedario.index(caracter)
            nueva_posicion = (posicion - 13) % len(abecedario)
            resultado += abecedario[nueva_posicion]
        else:
            resultado += caracter
    return resultado
