lista_compras = []
dados = []
def menu():
    print ('''Bem vindo a loja de figurinhas da copa do mundo."
    "1 - comprar pacotes de figurinhas."
    "2 - compra album."
    "3 - entrar no grupo de troca de figurinha."
    "4 - sair do programa.''')
menu()
# OPÇÃO 1
def comprar_figurinha():
    pacote = 7
    print ("O pacote de figurinha custa R$ 7,00")
    estoque_pacotes = 20
    print (f"Nos temos {estoque_pacotes} pacoteinhos no estoque.")
    carrinho_compra = 0
    qtd_pacote = int(input("Quantos pacotes vc deseja ?"))
    if qtd_pacote > estoque_pacotes:
        print ("Você exedeu a quantidade em estoque.")
        p1 = input("Deseja comprar todos os pacotes de figurinhas? ")
    else:
       print ("Adicionando os pacotes a lista de compras...")
       soma_do_valor = pacote * qtd_pacote
       lista_compra_pacotes = qtd_pacote + carrinho_compra
       print (f"Você comprou {lista_compra_pacotes} pacotinhos da copa.")
       print (f"O valor da compra deu {soma_do_valor}R$")
       soma_do_valor.append(lista_compras)
#OPÇÃO 2
def Comprar_album():
    estoque_capa_mole = 20
    estoque_capa_dura = 15
    estoque_edicao_premiun = 10
    print ("Nos temos os seguintes albuns disponiveis: " \
    "1 - capa mole = 24R$" \
    "2 - capa dura = 50R$"
    "3 - edição premiun = 110R$")
    opcao_album = input("Qual tipo de album você deseja? ")
    if opcao_album == "1":
        print ("Adicionando album de capa mole no ")

#OPÇÃO 3
def entrar_grupo():
    print ("Para entrar no grupo digite os seus dados ")
    grupo = []
    nome = input("Digite seu nome: ")
    tel = int(input("Digite seu telefone: "))
    usuario = {
        "nome": nome ,
        "telefone": tel
        }
    grupo.append (usuario)
    print (usuario)
    print ("você sera adicionado em breve no grupo de troca de figurinhas.")
    print ("Nós temos 100 pessoas no grupo de troca de figurinhas.")

while True:
    opcao = int(input("Ecolha uma opcao, se quiser sair digite '4': [1/2/3/4] :"))
    if opcao == 1:
        comprar_figurinha()
    elif opcao == 2:
        Comprar_album()
    elif opcao == 3:
        entrar_grupo()
    elif opcao == 4:
        print ("Volte sempre!")
        break