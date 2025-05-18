import math

def numero_terminos_arctan(precision):
    n = 1
    aproximacion = 1
    valor_real = math.pi

    while abs(4 * aproximacion - valor_real) >= precision:
        n += 1
        termino = ((-1) ** (n + 1)) / (2 * n - 1)
        aproximacion += termino

    return n, 4 * aproximacion

# Parte (a): precisión 10^-3
terminos_1e_3, pi_aprox_1e_3 = numero_terminos_arctan(1e-3)
error_1e_3 = abs(pi_aprox_1e_3 - math.pi)

print(" Aproximación de π con arctan(1), precisión < 10^-3:")
print(f"→ Términos necesarios: {terminos_1e_3}")
print(f"→ Aproximación: {pi_aprox_1e_3}")
print(f"→ Error absoluto: {error_1e_3}\n")

# Parte (b): precisión 10^-10
terminos_1e_10, pi_aprox_1e_10 = numero_terminos_arctan(1e-10)
error_1e_10 = abs(pi_aprox_1e_10 - math.pi)

print(" Aproximación de π con arctan(1), precisión < 10^-10 (requisito C++):")
print(f"→ Términos necesarios: {terminos_1e_10}")
print(f"→ Aproximación: {pi_aprox_1e_10}")
print(f"→ Error absoluto: {error_1e_10}")
