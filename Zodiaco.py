

signo = ["Capricornio", "Acuario", "Piscis", "Aries", "Tauro", "Geminis", "Cancer", "Leo", "Virgo", "Libra", "Escorpio", "Sagitario"]

fecha =[20, 19, 20, 21, 21, 22, 22, 22, 22, 22, 21]

mes = int(input("Mes de Nacimiento: "))
dia = int(input("Dia de Nacimiento: "))

mes = mes - 1
if dia > fecha[mes]:
    mes = mes +1
if mes == 12:
    mes = 0

print("Su Signo zodiacal es: ", signo[mes])

