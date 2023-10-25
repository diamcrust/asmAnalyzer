'''Script que hace análisis por linea detectando data segment y codesegment, también es el main del
analisis PARSE'''

import re  # biblioteca regular expression
import syntan  # Importando syntax analysis

lineStates = []  # Lista para guardar (linea,estado)
state = False  # Variable solo para debugear en consola y ver si ya detecta como correcto las instrucciones

type_segment = 0  # Variable para detectar el tipo de segmento
lineNumber = 0  # Contador de linea


def show(linea):
    global type_segment
    global lineNumber
    '''# abrir archivo a analizar
    with open("practica.asm") as archivo:

        # Variable de estado para controlar si estamos dentro del segmento .data
        type_segment = 0  # Variable para detectar el tipo de segmento
        lineNumber = 0  # Contador de linea

        for linea in archivo:
            linea = linea.strip()  # Eliminar los saltos de linea
            lineNumber += 1  # Incrementando linea

            # busca si en la linea esta la etiqueta .data
            if re.findall(r'\.data', linea, re.IGNORECASE):
                type_segment = 1

            # busca si en la linea esta la etiqueta .code
            if re.findall(r'\.code', linea, re.IGNORECASE):
                type_segment = 2

            # determina si se ha encontrado .data y ya esta en la siguiente linea
            if type_segment == 1 and not re.findall(r'\.data', linea, re.IGNORECASE):
                getDataSegment(linea)  # Funcion para mostrar en ventana
                syntaxAnalysis(linea, type_segment, lineNumber)

            # determina si se ha encontrado .code y ya esta en la siguiente linea
            if type_segment == 2 and not re.findall(r'\.code', linea, re.IGNORECASE):
                getCodeSegment(linea)  # Funcion para mostrar en ventana
                syntaxAnalysis(linea, type_segment, lineNumber)
'''

    linea = linea.strip()  # Eliminar los saltos de linea
    lineNumber += 1  # Incrementando linea
    # busca si en la linea esta la etiqueta .data
    if re.findall(r'\.data', linea, re.IGNORECASE):
        type_segment = 1

    # busca si en la linea esta la etiqueta .code
    if re.findall(r'\.code', linea, re.IGNORECASE):
        type_segment = 2

    # determina si se ha encontrado .data y ya esta en la siguiente linea
    if type_segment == 1 and not re.findall(r'\.data', linea, re.IGNORECASE):
        getDataSegment(linea, type_segment)  # Funcion para mostrar en ventana
        syntaxAnalysis(linea, type_segment, lineNumber)

    # determina si se ha encontrado .code y ya esta en la siguiente linea
    if type_segment == 2 and not re.findall(r'\.code', linea, re.IGNORECASE):
        getCodeSegment(linea, type_segment)  # Funcion para mostrar en ventana
        syntaxAnalysis(linea, type_segment, lineNumber)

    return (linea, type_segment)


def getDataSegment(linea, type_segment):
    # print(linea, end="")  # sustuir para que se muestre en ventana
    return (linea, type_segment)


def getCodeSegment(linea, type_segment):
    # print(linea, end="")  # sustituir para que se muestre en ventana
    return (linea, type_segment)


# funcion donde se hará el analisis parse
def syntaxAnalysis(linea, type_segment, lineNumber):
    global lineStates
    global state

    if not linea:  # Si la línea está en blanco, ignora el análisis
        return

    if type_segment == 1:
        resultado = syntan.analizar_lineaDataSegment(linea)
        if resultado:
            instruccion, operando1, operando2 = resultado  # Desmpaquetado en variables
            lineStates.append((lineNumber, True))

            # borrar desde aquí en entrega final, solo con fines de comprbacion en consola
            state = True
            print(
                f'instruccion: {instruccion}, operando1: {operando1}, operando2: {operando2}')
            print(state)
            # ... hasta aquí

        else:
            lineStates.append((lineNumber, False))

            # borrar desde aquí en entrega final, solo con fines de comprbacion en consola
            state = False
            print(state)
            # ... hasta aquí

    if type_segment == 2:
        resultado = syntan.analizar_lineaCodeSegment(linea)
        if resultado:
            instruccion, operando1, operando2 = resultado  # Desepaquetado en variables
            lineStates.append((lineNumber, True))

            # desde aquí borrar en entrega final, solo con fines de comprbacion en consola
            state = True
            print(
                f'instruccion: {instruccion}, operando1: {operando1}, operando2: {operando2}')
            print(state)
            # ...hasta aqui

        else:
            lineStates.append((lineNumber, False))

            # borrar desde aquí en entrega final, solo con fines de comprbacion en consola
            state = False
            print(state)
            # ... hasta aquí


'''def main():
    global lineStates
    show()

    # implementar como indicador de errores en la GUI
    incorrectLines = [line for line, state in lineStates if not state]
    if not incorrectLines:
        print("El código es correcto.")
    else:
        print("El código es incorrecto en las líneas:", incorrectLines)


if __name__ == "__main__":
    main()'''
