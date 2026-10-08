import datetime


def es_palabra_valida(cadena: str) -> bool:
    '''
    Comprueba si la cadena es una palabra válida:
    - Tiene 5 letras
    - Solo contiene letras a-z o A-Z

    Parámetros:
        cadena: la cadena a comprobar
    Devuelve:
        True si la cadena es una palabra válida, False en otro caso
    '''
    # TODO: Implementa esta función
    if len(cadena) == 5 and cadena.isalpha():
        for c in cadena:
            if c == cadena.isdigit():
                return False
        return True
    else:
        return False

def calcula_minutos_y_segundos(inicio: datetime, fin: datetime) -> tuple:
    """ 
    Recibe dos datetime y devuelve la diferencia en minutos y segundos.

    Parámetros:
        inicio: datetime de inicio
        fin: datetime de fin
    Devuelve:
        Una tupla (minutos, segundos) con la diferencia entre los dos datetime
    """
    # TODO: Implementa esta función
    tiempo_transcurrido = fin - inicio
    # type(tiempo_transcurrido)
    print (f"Han pasado {(tiempo_transcurrido.seconds)//60} minutos, {tiempo_transcurrido.seconds} segundos")

def obtener_pistas(secreta:str, intento:str) -> str:
    res = 0
    for i in intento:
        if secreta.find(i) == i and len(secreta.find(i))==len(intento.find(i)):
            return "V"
        elif secreta.find(i) == i:
            return "A"
        else:
            return "_"
    res += 1
        


# TODO: Escribe la cabecera completa e implementa la función quitar_letra
def quitar_letras(palabra:str, caracter:str) -> str:
    palabra = palabra.replace(caracter, "",1)
    return palabra

def marcar_verdes(secreta: str, intento: str) -> str:
    verdes = ""
    restantes = ""
    pos = 0
    for i in secreta:
        if i in intento:
            if pos >= len(intento) or intento[pos] != i:
                verdes += "_"
                restantes += i
            else:
                verdes += "V"
        else:
            verdes += "_" 
            restantes += i
        pos += 1
    return verdes, restantes

# TODO: Escribe la cabecera completa e implementa la función marcar_verdes

# TODO: Escribe la cabecera completa e implementa la función marcar_amarillos



