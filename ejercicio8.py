from random import randint as rd

number_to_guess = rd(0, 300)
intentos = 1

guess = int(input("Introduce su prediccion: "))
while guess != number_to_guess:
    if guess > number_to_guess:
        print("El numero buscado es mas peueño.")
    else:
        print("El numero buscado es mas grande.")
    
    guess = int(input("Introduce su prediccion: "))
    intentos += 1

print("Bien hecho CRACK el numero era", number_to_guess)
print(intentos)