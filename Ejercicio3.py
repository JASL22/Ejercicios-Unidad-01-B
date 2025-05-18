import math

def calcular_pi_con_formula(precision):
    n1 = 1
    arctan1_5 = 1 / 5

    n2 = 1
    arctan1_239 = 1 / 239

    aproximacion_pi = 4 * (4 * arctan1_5 - arctan1_239)

    while abs(aproximacion_pi - math.pi) >= precision:
        n1 += 1
        termino1 = ((-1) ** (n1 + 1)) * ((1 / 5) ** (2 * n1 - 1)) / (2 * n1 - 1)
        arctan1_5 += termino1

        n2 += 1
        termino2 = ((-1) ** (n2 + 1)) * ((1 / 239) ** (2 * n2 - 1)) / (2 * n2 - 1)
        arctan1_239 += termino2

        aproximacion_pi = 4 * (4 * arctan1_5 - arctan1_239)

    return max(n1, n2), aproximacion_pi

terminos, pi_aprox = calcular_pi_con_formula(1e-3)
error = abs(pi_aprox - math.pi)

print(" Resultado usando fórmula π = 4*(4*arctan(1/5) - arctan(1/239)):")
print(f"→ Términos necesarios: {terminos}")
print(f"→ Aproximación de π: {pi_aprox}")
print(f"→ Error absoluto: {error}")
