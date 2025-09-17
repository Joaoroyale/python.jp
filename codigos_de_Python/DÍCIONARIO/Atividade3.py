preços = {
    "batata":10,
    "banana":5,
    "laranja":20,
    "uva":30,
}
print ("digite 'sair' para finalizar.")
while True:
    escolha = input("Qual produto voce quer?:")
    if escolha in preços.keys():
        print ("Produto em estoque")
if escolha == ('sair'):
    print ("pedido finalizado")
    if escolha == preços:
        print (preços.values()) 
    if escolha not in preços:
        print ("Produto não encontrado")