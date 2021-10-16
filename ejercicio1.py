distancia_inicial = int(input("Introduce la distancia inicial a la que se encuentra: "))
tiempo = int(input("Introduce el tiempo durante el cual se esta moviendo: "))
velocidad = int(input("Introduce la velocidad a la que va el movil: "))

posiccion = distancia_inicial + velocidad * tiempo
print(posiccion)