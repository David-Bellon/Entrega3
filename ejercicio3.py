correctas = int(input("Introduce el numero de preguntas acertadas: "))
incorrectas = int(input("Introduce el numero de preguntas incorrectas: "))
blanco = int(input("Introduce el numero de preguntas no contestadas: "))

puntuacion = (correctas * 3) + (incorrectas * -1)
print(puntuacion)