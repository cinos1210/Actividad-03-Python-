import math

def area_cuadrado(num):
    num = float(num)
    num = num * num
    print("El area del cuadrado es:", num)

def area_triangulo(base, altura):
    base = float(base)
    altura = float(altura)
    area = (base * altura)/2

    print("El area del triangulo es:", area)

def area_circulo(radio):
    radio = float(radio)
    pi = math.pi
    area = (radio*radio) * pi
    print("El area del circulo es:", area)

lado = input("Digita un lado: ")
area_cuadrado(lado)

base = input("Digita la base: ")
altura = input("Digita la altura")
area_triangulo(base, altura)

radio = input("Digita el radio: ")
area_circulo(radio)
