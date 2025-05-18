import math
def truncar_3_digitos(x):
    if x == 0:
        return 0
    exp = math.floor(math.log10(abs(x)))
    factor = 10 ** (2 - exp)
    return math.trunc(x * factor) / factor

def suma_ascendente_potencia2(n):
    suma = 0
    for i in range(1, n + 1):
        termino = 1 / (i ** 2)
        suma = truncar_3_digitos(suma + termino)
    return suma

def suma_descendente_potencia2(n):
    suma = 0
    for i in range(n, 0, -1):
        termino = 1 / (i ** 2)
        suma = truncar_3_digitos(suma + termino)
    return suma

def suma_ascendente_potencia3(n):
    suma = 0
    for i in range(1, n + 1):
        termino = 1 / (i ** 3)
        suma = truncar_3_digitos(suma + termino)
    return suma

def suma_descendente_potencia3(n):
    suma = 0
    for i in range(n, 0, -1):
        termino = 1 / (i ** 3)
        suma = truncar_3_digitos(suma + termino)
    return suma

def suma_exacta_potencia(n, potencia):
    return sum([1 / (i ** potencia) for i in range(1, n + 1)])

def comparar_metodos(nombre, asc, desc, exacta):
    err_asc = abs(exacta - asc)
    err_desc = abs(exacta - desc)
    print(f"\n{nombre}")  # Aquí estaba el error: nombre en lugar de name
    print("Resultado exacto:", round(exacta, 6))
    print("Ascendente:", asc, "| Error:", round(err_asc, 6))
    print("Descendente:", desc, "| Error:", round(err_desc, 6))
    if err_desc < err_asc:
        print("→ El método DESCENDENTE es más preciso.")
    elif err_asc < err_desc:
        print("→ El método ASCENDENTE es más preciso.")
    else:
        print("→ Ambos métodos tienen la misma precisión.")


# Ejecutar para n = 10
n = 10
# Ejercicio a: 1/i^2
asc_a = suma_ascendente_potencia2(n)
desc_a = suma_descendente_potencia2(n)
exact_a = suma_exacta_potencia(n, 2)
comparar_metodos("Ejercicio a (1/i^2)", asc_a, desc_a, exact_a)

# Ejercicio b: 1/i^3
asc_b = suma_ascendente_potencia3(n)
desc_b = suma_descendente_potencia3(n)
exact_b = suma_exacta_potencia(n, 3)
comparar_metodos("Ejercicio b (1/i^3)", asc_b, desc_b, exact_b)