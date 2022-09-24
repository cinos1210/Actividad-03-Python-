from math import factorial



limite = input("Digite el limite: ")
limite = float(limite)
n = 0
e = 0
while n < limite:
    e += 1/factorial(n)
    n = n + 1
    
print("El valor de numero e es: ", e)

