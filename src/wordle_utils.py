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
    from datetime import datetime
    tiempo_transcurrido = fin - inicio
    type(tiempo_transcurrido)
    print (f"Han pasado ¨{tiempo_transcurrido.min} minutos,{tiempo_transcurrido.seconds} segundos")

calcula_minutos_y_segundos(datetime.datetime(2024, 1, 1, 23, 0, 0), datetime.datetime(2024, 1, 1, 23, 0, 30))

# TODO: Escribe la cabecera completa e implementa la función quitar_letra

# TODO: Escribe la cabecera completa e implementa la función marcar_verdes

# TODO: Escribe la cabecera completa e implementa la función marcar_amarillos

def obtener_pistas(palabra_secreta: str, intento: str) -> str:
    """
    Devuelve la cadena de pistas para un intento dado.
    Parámetros:
        palabra_secreta: la palabra secreta
        intento: la palabra del intento
    Devuelve:
        Una cadena de 5 caracteres con 'V', 'A' y '_'
    """
    # TODO: Implementa esta función
    return "_____"  # Elimina esta línea cuando la implementes


