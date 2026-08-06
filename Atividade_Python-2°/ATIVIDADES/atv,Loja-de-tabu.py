cardapio = [
    {
    "sabor": "morango",
    "preco": 2,
    "quantidade": 5
    },

    {
    "sabor": "caja",
    "preco": 2,
    "quantidade": 3
    },

    {
    "sabor": "jaca",
    "preco": 3,
    "quantidade": 1
    }
    ]
listasab = ["morango", "caja", "jaca"]

for sabores in cardapio:
    print ("sabor: ", sabores["sabor"])
    print ("preco: ", sabores["preco"])
    print ("quantidade: ",sabores["quantidade"])

total_compras = 0

p1 = input("Vocé deseja comprar um tabú? [S/N]: ").lower( )
if p1 == "n":
    print ("OK, Tchau!")
elif p1 == "s":
    while True:
        p2 = input("Qual sabor deseja?: ").lower()
        if p2 in listasab:
            indice = listasab.index(p2)
            if cardapio[indice]["quantidade"] == 0:
                print (f"Não temos mais tabú de {p2} no cardapio!")
            else:
                qtd = int(input("Quantos tabús você deseja? "))
                if qtd > cardapio[indice]["quantidade"]:
                    limite = int(input(f"Você excediu a quantidade de itens no estoque! ({cardapio[indice]["quantidade"]}) | Deseja comprar a quantidade máxima ou decidir novamente?[1/2]: "))
                    if limite == 1:
                        total_compras = total_compras + cardapio[indice]["quantidade"]
                        print (f"Certo! Itens adicionados ao carrinho. ({total_compras})")
                    elif limite == 2:
                        while qtd > cardapio[indice]["quantidade"]:
                            qtd = int(input(f"Quantos tabús você deseja? (Lembrando, o limite é: {cardapio[indice]["quantidade"]}): "))
                            if qtd <= cardapio[indice]["quantidade"]:
                                total_compras = total_compras + qtd
                                print (f"Certo! {qtd} itens adicionados ao carrinho.")
                else:
                    total_compras = total_compras + qtd
                    print (f"Certo! {qtd} itens adicionados ao carrinho.")
        else:
            p3 = input("Erro, Sabor Inexistente. Deseja continuar? [S/N]: ").lower()
            if p3 == "s":
                continue
            elif p3 == "n":
                break
        conta = total_compras * cardapio[indice]["preco"]
        print (f"A sua conta deu: {conta}.")
        cardapio[indice]["quantidade"] = cardapio[indice]["quantidade"] - total_compras
        total_compras = 0
        if cardapio[0]["quantidade"] == 0 and cardapio[1]["quantidade"] == 0 and cardapio[2]["quantidade"] == 0:
            print ("O estoque acabou totalmente. Volte outro dia!")
            break
        continuar = input("Deseja continuar comprando? [S/N]: ").lower()
        if continuar == "s":
            continue
        if continuar == "n":
            print ("Certo, obrigado pela compra!")
            break