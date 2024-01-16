num1 = 20
num2 = 40


print("La suma es: ", (num1+num2))
print("La resta es: ", (num1-num2))
print("La multiplicacion es: ", (num2 * num1))
print("La division es: ", (num1/ num2))
print("La divicion exacta es: ", (num2 //num1))
print("La potencia es. ", (num1 ** num2))


#Concatenaciuon Python

texto1 = "Hola"
texto2 = "Mundo"

textfinal = texto1 + texto2

print(textfinal)

print("El saludo es:  %s %s" % (texto1,texto2))
saludoFinal = "Saludo {}{}".format(texto1,texto2)

print(saludoFinal)