"""
Programa: Cálculo de área y perímetro de un rectángulo
Descripción:
Este programa pide al usuario el ancho y el alto de un rectángulo.
Con esos valores calcula el área y el perímetro, y muestra los resultados.
También identifica si la figura es un cuadrado.
"""

# Función que calcula el área del rectángulo
def calcular_area(ancho, alto):
    area = ancho * alto
    return area

# Función que calcula el perímetro del rectángulo
def calcular_perimetro(ancho, alto):
    perimetro = 2 * (ancho + alto)
    return perimetro


# Mensaje de inicio del programa
print("Calculadora de rectángulos")

# Pedimos los datos al usuario (float porque puede haber decimales)
ancho_usuario = float(input("Ingresa el ancho del rectángulo: "))
alto_usuario = float(input("Ingresa el alto del rectángulo: "))

# Ejecutamos los cálculos
area_resultado = calcular_area(ancho_usuario, alto_usuario)
perimetro_resultado = calcular_perimetro(ancho_usuario, alto_usuario)

# Variable booleana: True si es cuadrado
es_cuadrado = ancho_usuario == alto_usuario

# Mostramos los resultados
print("Área:", area_resultado)
print("Perímetro:", perimetro_resultado)

# Condicional para verificar si es cuadrado
if es_cuadrado:
    print("Este rectángulo es en realidad un cuadrado.")
else:
    print("Este rectángulo no es un cuadrado.")
