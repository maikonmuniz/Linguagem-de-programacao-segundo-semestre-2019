# Linguagem de Programação II
# Atividade Contínua 02 - Dicionários
#
# e-mails: maikon.silva@aluno.faculdadeimpacta.com.br
#          luiz.franca@aluno.faculdadeimpacta.com.br


from mamifero import Mamifero
from reptil import Reptil


"""
Implementar aqui as cinco classes filhas de Mamifero ou Reptil,
de acordo com o caso, conforme dado no diagrama de classes visto
em sala.

ESTE É O ÚNICO ARQUIVO QUE DEVE SER ENTREGUE!

Os atributos específicos de cada classe filha devem ser recebidos
como parâmetros no momento da criação, a exceção é o número de vidas
do gato, que começa em 7.

Os métodos de cada classe filha devem sempre retornar uma string
no seguinte formato '<nome do animal> <método em questão no gerúndio>'
Sem nenhuma pontuação.

Exemplo:
método trocar_pele() retorna '<nome> trocando de pele'
método dormir() retorna '<nome> dormindo'
método miar() retorna '<nome> miando'
Onde <nome> é o nome dado para cada animal (o atributo, não o nome da classe)

A única exceção é o método morrer, que deve verificar
quantas vidas o gato ainda tem sobrando, se for igual a zero,
retornar '<nome> morreu', se ainda houver vidas sobrando,
retirar uma vida (que começa em 7) e
retornar '<nome> tem <vidas> sobrando'
Onde <vidas> é o número de vidas restantes do gato em questão.
"""


class Cavalo(Mamifero):
    def __init__(self, nome, cor_pelo, idade, tipo_pata, cor_crina):
        super().__init__(nome, cor_pelo, idade, tipo_pata)
        self.cor_crina = cor_crina

    def galopar(self):
        return "{} galopando".format(self.nome)

    def relichar(self):
        return "{} esta... sei la que porra é essa".format(self.nome)


class Cachorro(Mamifero):
    def __init__(self, nome, cor_pelo, idade, tipo_pata, raca):
        super().__init__(nome, cor_pelo, idade, tipo_pata)
        self.raca = raca

    def latir(self):
        return "{} latindo".format(self.nome)

    def rosnar(self):
        return "{} rosnando".format(self.nome)


class Gato(Mamifero):
    def __init__(self, nome, cor_pelo, idade, tipo_pata):
        super().__init__(nome, cor_pelo, idade, tipo_pata)
        self.vidas = 7

    def miar(self):
        return "{} miando".format(self.nome)

    def morrer(self):
        if self.vidas == 0:
            return "{} morreu".format(self.nome)
        else:
            self.vidas -= 1
            return '{} tem {} sobrando'.format(self.nome, self.vidas)


class Cobra(Reptil):
    def __init__(self, nome, cor_escamas, idade, veneno):
        super().__init__(nome, cor_escamas, idade)
        self.veneno = veneno

    def rastejar(self):
        return "{} rastejando".format(self.nome)

    def trocar_pele(self):
        return "{} trocando de pele".format(self.nome)


class Jacare(Reptil):
    def __init__(self, nome, cor_escamas, idade, num_dentes):
        super().__init__(nome, cor_escamas, idade)
        num_dentes = num_dentes

    def atacar(self):
        return "{} atacando".format(self.nome)

    def dormir(self):
        return "{} dorminando".format(self.nome)
