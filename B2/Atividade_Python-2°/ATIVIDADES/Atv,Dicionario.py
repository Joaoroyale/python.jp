Pessoa = {"Nome": 'João',
          "idade": 16, 
          "sexo": 'Masculino'}
print (Pessoa)
for chave, valor in Pessoa.items():
    print (f"{chave} é {valor}")

for chave in Pessoa.keys():
    print (f'A chave é {chave}')

for valor in Pessoa.values():
    print (f'O valor da chave é {valor}')
