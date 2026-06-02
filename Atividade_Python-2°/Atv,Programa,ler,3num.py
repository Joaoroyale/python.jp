#Programa que leia três números e, em seguida leie o usuario escolher entre:
#1 - somar os números
#2 - Ordem crescente
#3 - Vereficar pares e impares
#4 - Dobro e metade dos números
num = []
def menu():
    print ('''"Escolha uma das seguintes opções abaixo quando o numero for escolhido por você mesmo:"
    "1 - somar os numeros"
    "2 - ordem crescente"
    "3 - verificar pares e impares"
    "4 - dobro e metade dos números"''')
menu()    
def somar_os_numeros():
    soma = num[0] + num[1] + num[2]
    print (f"A soma total dos números são: {soma}")
#opcao 1

def ordem_crescente():
    num.sort()
    print(num)
#opcao 2

def verificacao():
    if num[1] % 2 == 0:
        print (f"O número {num[1]} é par.")
    else:
        print (f"O numero {num[1]} é impar")

    if num[2] % 2 == 0:
        print (f"O número {num[2]} é par.")
    else:
        print (f"O numero {num[2]} é impar")

    if num[3] % 2 == 0:
        print (f"O número {num[3]} é par.")
    else:
        print (f"O numero {num[3]} é impar")
#opcao 3

def dobro_metade():
    dobro = (num[1] * 2), (num[2] * 2), (num[2] * 2)
    print (f"O dobro dos numeros é igual á : {dobro}")
    
    metade = (num[1] / 2), (num[2] / 2), (num[3] / 2)
    print (f"A metade dos números escolhidos foram: {metade}")
#opcao 4
for i in range(3):
    numeros = int(input("Digite alguns números inteiros?  "))
    num.append(numeros)
while True:
    escolha = input("Escolha uma das opções a cima? [1/2/3/4] : ")
    if escolha == "1":
        somar_os_numeros()
    elif escolha == "2":
        ordem_crescente()
    elif escolha == "3":
        verificacao()
    elif escolha == "4":
        dobro_metade()
    elif escolha == "5":
        print ("Ok, até mais!")