class Filme:
    def __init__(self, ano, diretor, classificacao, atores, sinopse, titulo, genero):
        self.ano = ano
        self.diretor = diretor
        self.classificação = classificacao
        self.atores = atores
        self.sinopse = sinopse
        self.titulo = titulo
        self.genero = genero

class Serie:
    def __init__(self, diretor, classificacao, atores, sinopse, titulo, genero, temporada, episodio):
        self.diretor = diretor
        self.classificação = classificacao
        self.atores = atores
        self.sinopse = sinopse
        self.titulo = titulo
        self.genero = genero
        self.temporada = temporada
        self.episodio = episodio


class Usuario:
    def __init__(self, nome, idade, email, cpf):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.cpf = cpf

#instanciar
filme1 = Filme(
    2010, 
    "nogui",
    +14,
    "arthur,micaias,renan",
    "um menino se perde pela mata e é achado por um grupo de resgate",
    "O achado",
    "terror,suspense")

#instanciar
serie1 = Serie(
    "sionise",
    "livre",
    "vitor,breno,antonio",
    "os meninos brincam no parque e acham um alien",
    "o encontro entre dois mundos",
    "comedia",
    4,
    32)

#instancia
usuario1 = Usuario(
    "joao",
    14,
    "aleatorio123@gmail.com.br",
    "123.456.789-00")