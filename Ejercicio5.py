import math
def suma_doble_optimizada(a, b, n):
    suma = 0
    suma_b = 0
    
    for i in range(n):
        suma_b += b[i]
        suma += a[i] * suma_b
    
    return suma

def suma_serie_inversa(x, n):
    suma = 0
    
    for i in range(n-1, -1, -1): 
        suma += x[i]
    
    return suma

def mostrar_comparacion_rendimiento():
    print("Comparación de rendimiento para la suma doble:")
    
    def suma_doble_directa(a, b, n):
        """Implementación directa (ineficiente) de la suma doble"""
        suma = 0
        for i in range(n):
            for j in range(i+1):
                suma += a[i] * b[j]
        return suma
    
    a = [1, 2, 3, 4, 5]
    b = [5, 4, 3, 2, 1]
    n = len(a)
    
    resultado_directo = suma_doble_directa(a, b, n)
    resultado_optimizado = suma_doble_optimizada(a, b, n)
    print(f"Tamaño n = {n}")
    print(f"Resultado directo: {resultado_directo}")
    print(f"Resultado optimizado: {resultado_optimizado}")
    print("\nAnálisis de complejidad:")
    print("Implementación directa:")
    print(f"  - Multiplicaciones: {n*(n+1)//2} = {n*(n+1)//2}")
    print(f"  - Sumas: {n*(n+1)//2 - 1} = {n*(n+1)//2 - 1}")
    print("Implementación optimizada:")
    print(f"  - Multiplicaciones: {n}")
    print(f"  - Sumas: {2*n - 1}")
def demostrar_suma_inversa():
    """Demuestra el funcionamiento de la suma en orden inverso"""
    print("\nDemostración de suma en orden inverso:")
    x = [10, 20, 30, 40, 50]
    n = len(x)
    suma_normal = sum(x)
    suma_inversa = suma_serie_inversa(x, n)
    
    print(f"Lista: {x}")
    print(f"Suma normal: {suma_normal}")
    print(f"Suma en orden inverso: {suma_inversa}")
    print(f"¿Son iguales? {'Sí' if suma_normal == suma_inversa else 'No'}")

mostrar_comparacion_rendimiento()
demostrar_suma_inversa()