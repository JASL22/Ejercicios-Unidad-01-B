def redondear_3_digitos(numero):
    return int(numero * 1000) / 1000 

def suma_ascendente(n, potencia):
    suma = 0
    for i in range(1, n + 1):
        termino = 1 / (i ** potencia)
        suma = redondear_3_digitos(suma + termino)
    return suma

def suma_descendente(n, potencia):
    suma = 0
    for i in range(n, 0, -1):
        termino = 1 / (i ** potencia)
        suma = redondear_3_digitos(suma + termino)
    return suma

# Parte (a) con i^2
n = 10
potencia = 2

ascendente_i2 = suma_ascendente(n, potencia)
descendente_i2 = suma_descendente(n, potencia)
real_i2 = sum([1 / (i ** 2) for i in range(1, n + 1)])

print(" Suma de 1/i^2 para i=1 a 10:")
print(f"→ Orden ascendente (corte): {ascendente_i2}")
print(f"→ Orden descendente (corte): {descendente_i2}")
print(f"→ Valor real (sin corte): {real_i2:.10f}")

if abs(descendente_i2 - real_i2) < abs(ascendente_i2 - real_i2):
    print(" Método más preciso: Descendente\n")
else:
    print(" Método más preciso: Ascendente\n")

# Parte (b) con i^3
potencia = 3

ascendente_i3 = suma_ascendente(n, potencia)
descendente_i3 = suma_descendente(n, potencia)
real_i3 = sum([1 / (i ** 3) for i in range(1, n + 1)])

print("📘 Suma de 1/i^3 para i=1 a 10:")
print(f"→ Orden ascendente (corte): {ascendente_i3}")
print(f"→ Orden descendente (corte): {descendente_i3}")
print(f"→ Valor real (sin corte): {real_i3:.10f}")

if abs(descendente_i3 - real_i3) < abs(ascendente_i3 - real_i3):
    print(" Método más preciso: Descendente")
else:
    print(" Método más preciso: Ascendente")
