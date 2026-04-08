lista_original = []

for i in range(30):
    numero = int(input("Digite um numero inteiro?:"))
    lista_original.append(numero)

lista_modificada = []

for i in range(30):
    if i % 2 == 0:
        lista_modificada.append(lista_original[i] * 2)
    else:
        lista_modificada.append(lista_original[1] * 3)
print ("lista original")
print (lista_original)

print ("Lista modificada")
print (lista_modificada)