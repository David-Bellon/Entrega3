precio_l = 1.3

def price():
    galons = int(input("Introduce el numero de galones: "))
    litros = galons * 3.78
    return litros * precio_l

print(price())