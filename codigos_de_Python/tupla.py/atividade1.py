pedido_completo = []
cardapio = ("carne_mofada","coxinha_com_lesma","bolo_com_baba","lasanha_de_bufalo","panqueca_de_cachorro","pudim_com_baba")
sair = ("finalizar  pedido")
print (f"Caso queria finalizar o pedido digite: {sair}.")
print (f"O nosso cardapio é:{cardapio}.")
x = 0
while x < 6:
    pedido = input("qual pedido voce quer?:")
    if pedido in cardapio:
        pedido_completo.append(pedido)
    else:
        print ("Não tem este pedido no cardapio.")
    print (pedido_completo)
    x = x + 1
bebidas = "guarana com baba","poeira cosmica","tinta","baba de lesma","cuspe de galo"
y = 0
while y < 6:
    pedido_bebidas = input("Quais bebidas voce quer?:")
    y = y + 1
lista_pedidos = []
lista_pedidos.append (pedido)