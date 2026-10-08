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

class Professora:
    pass

class Aluno:
    pass

class TAE:
    pass

#Instanciar

aluno1 = Aluno("Joao", 19)
aluno2 = Aluno("vitor", 28)
prof1 = Professora("Sionise", 32)
prof2 = Professora("Estar", 42)

aluno1.exibir_informacao()
aluno2.exibir_informacao() 
prof1.exibir_informacao()
prof2.exibir_informacao()