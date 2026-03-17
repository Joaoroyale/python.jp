produtos = {"Arroz": 1, "Feijão": 1.50, "Batata_palha": 3, "Pirulito": 0.50, }

while True:
    produto = input ("Digite qual produto vocé deseja. Digite 'fim' para teminar:")
    if produto == "fim":
        print ("fim")
        break
    elif produto in produtos:
        print (f"Preço{produtos[produto]:5.2f}")
    else: 
        print ("Produto não encontrado!")