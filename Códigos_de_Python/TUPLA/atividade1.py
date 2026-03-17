pedido_completo = []
cardapio = ("carne_mofada","coxinha_com_lesma","bolo_com_baba","lasanha_de_bufalo","panqueca_de_cachorro","pudim_com_baba")
print ("Caso queria finalizar o pedido digite: sair.")
print (f"O nosso cardapio é:{cardapio}.")

x = 0
while True: 
    pedido = input("qual pedido voce quer?:")
    if pedido == "sair":   
       break
    if pedido in cardapio:
        pedido_completo.append(pedido)
        if pedido == "carne_mofada":
           x = x + 20
        elif pedido == "coxinha_com_lesma":
           x = x + 5
        elif pedido == "bolo_com_baba":
           x = x + 10
        elif pedido == "lasanha_de_bufalo":
           x = x + 40
        elif pedido == "panqueca_de_cachorro":
           x = x + 30
        elif pedido == "pudim_com_baba":
           x = x = 25
        else:  
            print ("Não tem este alimento no cardapio.")
            print (pedido_completo)
x = x + 1
bebidas = "Guarana com baba","Poeira cosmica","Tinta","Baba de lesma","Cuspe de galo"
y = 0
pedido_de_bebidas = []
while True:
    pedido_bebidas = input("Quais bebidas voce quer?:")
    if pedido_bebidas == "Não quero nada":
       break
    if pedido_bebidas in bebidas:
        pedido_de_bebidas.append(pedido_bebidas)
        if pedido_bebidas == "Guarana com baba":
           x = x + 9
        elif pedido_bebidas == "Poeira cosmica":
           x = x + 100
        elif pedido_bebidas == "Tinta":
           x = x + 5
        elif pedido_bebidas == "Baba de lesma":
           x = x + 10
        elif pedido_bebidas == "Cuspe de galo":
           x = x + 12
print (f"Vocé pediu:{pedido} para comer e de bebidas pedisse {pedido_bebidas}:")