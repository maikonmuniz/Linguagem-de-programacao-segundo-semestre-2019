# Linguagem de Programação II
# Atividade Contínua 01 - Números Especiais
#
# e-mails: maikon.silva@aluno.faculdadeimpacta.com.br

from typing import List


def eh_armstrong(n: int):  # -> bool:
    '''
    Função que recebe um número natural e retorna verdadeiro se
    n é um número de Armstrong e falso caso contrário.
    Um número é dito número de Armstrong se a soma de seus digitos
    elevados ao número total de digitos é igual a ele próprio.
    Ex: 153 é número de Armstrong:
        1 ** 3 + 5 **3 + 3 ** 3 = 1 + 125 + 27 = 153
    Ex: 4 é número de Armstrong:
        4 ** 1 = 4
    '''
    n_str = str(n)
    n_digitos = len(n_str)
    soma = 0
    for x in n_str:
        soma += int(x) ** n_digitos
    if soma == n:
        return True
    else:
        return False


def lista_armstrong(n: int):  # -> List[int]:
    '''
    Função que recebe um número natural e retorna uma lista com todos o
    números de Armstrong menores que ele.
    '''
    lista_arm = []
    for x in range(n):
        if eh_armstrong(x):
            lista_arm.append(x)
    return lista_arm


def eh_perfeito(n: int):  # -> bool:
    '''
    Função que recebe um número natural como parâmetro e retorna verdadeiro
    se o número é perfeito e falso caso contrário.
    Um número é dito perfeito se a soma de todos os divisores próprios é
    igual a ele mesmo.
    Ex: 6 é um número perfeito:
        divisores próprios de 6: 1, 2, 3
        1 + 2 + 3 = 6
    '''
    soma = 0
    for x in range(1, n//2+1):
        if n % x == 0:
            soma += x
    if soma == n:
        return True
    else:
        return False


def lista_perfeitos(n: int):  # -> List[int]:
    '''
    Função que recebe um número natural e devolve todos os números perfeitos
    menores que ele.
    '''
    lista_per = []
    for x in range(1, n):
        if eh_perfeito(x):
            lista_per.append(x)
    return lista_per
