pilha = []
x = 0
while x < 5:
    palavra = input("Qual palavra vocé quer ?:")
    pilha.append (f"{palavra}")
    print (pilha)
    x = x + 1
y = 0
while y < 5:
    pilha.pop ()
    print (pilha)
    print ("Apagando informações.")
    y = y + 1