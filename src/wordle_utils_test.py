# Pruebas para las funciones de wordle_utils.py

# TODO: Implementa las pruebas que te indica el enunciado

from wordle_utils import es_palabra_valida, calcula_minutos_y_segundos, quitar_letras, marcar_verdes

def test_es_palabra_valida():
    print("Probando es_palabra_valida...")
    assert es_palabra_valida("casar") == True
    assert es_palabra_valida("casa") == False
    assert es_palabra_valida("casarr") == False
    assert es_palabra_valida("c4sar") == False
    assert es_palabra_valida("casa ") == False
    assert es_palabra_valida(" casa") == False
    assert es_palabra_valida("CASAR") == True

def test_calcula_minutos_y_segundos():
    import datetime
    assert calcula_minutos_y_segundos(datetime.datetime(2024, 1, 1, 23, 0, 0), datetime.datetime(2024, 1, 1, 23, 0, 30))
    assert calcula_minutos_y_segundos(datetime.datetime(2024, 1, 1, 23, 0, 0), datetime.datetime(2024, 1, 1, 23, 3, 45))
    assert calcula_minutos_y_segundos(datetime.datetime(2024, 1, 1, 23, 0, 0), datetime.datetime(2024, 1, 2, 0, 1, 15))

def test_quitar_letras():
    assert quitar_letras("casar", "a")
    assert quitar_letras("casar", "c")
    assert quitar_letras("casar", "r")
    assert quitar_letras("casar", "z")
    assert quitar_letras("aaaaa", "a")

def test_marcar_verdes():
    print("Probando marcar_verdes...")
    assert marcar_verdes("casar", "polio") == ("_____", "casar")
    assert marcar_verdes("casar", "casar") == ("VVVVV", "")
    assert marcar_verdes("casar", "cazar") == ("VV_VV", "s")
    assert marcar_verdes("casar", "secta") == ("_____", "casar")
    assert marcar_verdes("casar", "sacar") == ("_V_VV","cs")
    assert marcar_verdes("casar", "peras") == ("___V_", "csar")

#test_es_palabra_valida()
#test_calcula_minutos_y_segundos()
#test_quitar_letras()
test_marcar_verdes()
print("✅Todas las pruebas pasaron correctamente.")