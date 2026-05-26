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
    print ("Comprar figurinha.")

#OPÇÃO 2
def Comprar_album():
    print ("Comprar album.")

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
    print ("você foi adicionado ao grupo.")

while True:
    opcao = int(input("Ecolha uma opcao, se quiser sair digite '4': [1/2/3/4] :"))
    if opcao == 1:
        entrar_grupo()
    elif opcao == 2:
        Comprar_album()
    elif opcao == 3:
        entrar_grupo()
    elif opcao == 4:
        print ("Volte sempre!")
        break