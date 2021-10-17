

def bisiesto():
    year = int(input("Introduce un año: "))
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        else:
            leap = True
    return leap

print(bisiesto())
