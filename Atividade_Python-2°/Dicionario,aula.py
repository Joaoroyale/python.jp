copa2026 = [
    #Dicionário na posição copa[0]
    {
        "selecao": "França",
        "tecnico": "Didier Deschamps",
        "goleiro": "Mike Maignan",
        "titulos": 2
    },
    #Dicionário na posição copa[1]
    {
    "selecao": "Portugal",
    "tecnico": "Roberto Martínez",
    "goleiro": "Diogo Costa",
    "titulos": 0
    },


    #Dicionário na posição copa[2]
    {
    "selecao": "Brasil",
    "tecnico": "Carlo Ancelotti",
    "goleiro": "Alisson",
    "titulos": 5
    },

    #Dicionario na posição copa[3]
    {
    "selecao": "Portugal",
    "tecnico": "Roberto Martínez",
    "goleiro": "Diogo Costa",
    "titulos": 0
}
]
print (copa2026) #Imprime a lista com todas as seleções

maior = copa2026[0]

for time in copa2026:
    print ("Nome da seleção: ", time["selecao"])
    print ("Tecnico do time: ", time["tecnico"])
    print (f"Goleiro titular: {time["goleiro"]}")
    print (f"Quantidade de titulos: {time["titulos"]}")
    print ()

    if time["titulos"] > maior["titulos"]:
        maior = time
print ("A seleção com maior títulos é: ", maior["selecao"])