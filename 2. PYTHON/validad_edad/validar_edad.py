edad=int(input("Ingrese la edad: "))
if edad > 0 and edad <= 150:
    if edad >= 18:
        print("Es mayor de edad.")
    else:
        print("Es menor de edad.")
else:
    print("Edad invalida. Ingrese una edad razonable entre 1 y 150  años")