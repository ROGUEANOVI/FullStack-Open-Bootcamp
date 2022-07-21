numero_inicial = int(input("Ingrese el numero inicial: "))
numero_final = int(input("Ingrese el numero final: "))
lista_impares = []
while(numero_final <= numero_inicial):
  numero_final = int(input("El numero_final debe ser mayor al numero inicial por favor, introduce otro numero: "))

for numero in range(numero_inicial,numero_final + 1):
  if ((numero % 2) != 0):
    lista_impares.append(numero)

print(lista_impares)



