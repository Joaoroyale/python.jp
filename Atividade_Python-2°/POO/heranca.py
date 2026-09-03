class Pessoa: 
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade
    def exibir_informacao(self):
        print(f"Nome: {self.nome}")
        print(f"idade: {self.idade}")
Pessoa1 = Pessoa( 
    "Joao pedro ", 
    16
)
Pessoa1.exibir_informacao()