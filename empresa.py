# AC07 SI2A - ADS2B - Empresa
# alunos: maikon.silva@aluno.faculdadeimpacta.com.br
#         catarina.sousa@aluno.faculdadeimpacta.com.br
#         felipe.augusto@aluno.faculdadeimpacta.com.br
from typing import List
from abc import ABC, abstractmethod


class Pessoa(ABC):
    '''
    Abstração de pessoa:
    '''
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade


class Funcionario(Pessoa):
    '''
    Classe Abstrata funcionário.
    '''
    def calcula_salario(self) -> float:
        '''
        Calcula o salário do Mês para o funcionário
        '''
        total_salario = (self.salario * self.carga_horaria_semanal) * 4.5
        return total_salario

    def altera_carga_horaria(self, nova_carga_horaria: int) -> None:
        '''
        altera a carga horária do funcionário, respeitando o limite,
        de horas por categoria.
        Caso o numero informado seja inválido, da raise em um ValueError
        '''
        raise NotImplementedError

    def consulta_carga_horaria(self) -> int:
        '''
        Devolve a carga horária de trabalho do funcionário
        '''
        return self.carga_horaria_semanal

    def aumenta_salario(self) -> None:
        '''
        Da um aumento de 5% no valor da hora trabalhada para o funcionário
        '''
        self.salario += (self.salario * 0.05)


class Programador(Funcionario):
    '''
    Funcionário do tipo programador, salario base por hora 35,00.
    Regime de trabalho deve estar entre 20 e 40h semanais,
    caso contrário devolve um ValueError.
    Para efeito de cálculo de pagamento o mês possui 4,5 semanas
    '''
    def __init__(self, nome: str, idade: int, email: str,
                 carga_horaria_semanal: int = 40):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.salario_pmds = 35

        if carga_horaria_semanal > 20 or carga_horaria_semanal < 40:
            self.carga_horaria_semanal = carga_horaria_semanal
        else:
            raise ValueError("carga horária é entre 20 e 40")

    def altera_carga_horaria(self, nova_carga_horaria):

        if nova_carga_horaria >= 20 or nova_carga_horaria <= 40:
            self.carga_horaria_semanal = nova_carga_horaria
        else:
            raise ValueError("carga horária é 20 e 40")


class Estagiario(Funcionario):
    '''
    Funcionário do tipo estagiário, salario base por hora 15,50
    e auxilio alimentação de 250 reais por mês.
    Regime de trabalho deve estar entre 16h e 30h semanais,
    caso contrário da raise em um ValueError.
    Para efeito de cálculo de salário o mês possui 4,5 semanas
    '''
    def __init__(self, nome: str, idade: int, email: str,
                 carga_horaria_semanal: int = 20):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.salario_est = 15.50

        if carga_horaria_semanal >= 16 or carga_horaria_semanal <= 30:
            self.carga_horaria_semanal = carga_horaria_semanal
        else:
            raise ValueError("A carga horaria 16 e 30")

    def altera_carga_horaria(self, nova_carga_horaria):
        if nova_carga_horaria >= 16 or nova_carga_horaria <= 30:
            self.carga_horaria_semanal = nova_carga_horaria
        else:
            raise ValueError("carga horária deve estar entre 16 e 30")

    def calcula_salario(self) -> float:
        '''
        Calcula o salário do Mês para o funcionário
        '''
        total_salario = ((self.salario_est * self.carga_horaria_semanal) * 4.5)
        total_salario = total_salario + 250
        return total_salario


class Empresa:
    '''
    Classe empresa, gerencia diversos funcionários
    '''
    def __init__(self, nome: str, cnpj: int, area_atuacao: str,
                 equipe: List[Funcionario] = []):
        self.nome = nome
        self.cnpj = cnpj
        self.area_atuacao = area_atuacao
        self.funcionarios_contratados = equipe

    def contrata(self, novo_funcionario: Funcionario) -> None:
        '''
        Contrata um novo funcionário para a empresa
        '''
        self.funcionarios_contratados.append(novo_funcionario)

    def lista_fucionarios(self) -> List[Funcionario]:
        '''
        Devolve um lista com todos os funcionarios
        '''
        return self.funcionarios_contratados

    def folha_pagamento(self) -> float:
        '''
        Devolve o montante total gasto com pagamento dos funcionários
        '''
        salario_folha = 0
        for f in self.funcionarios_contratados:
            salario_folha += f.calcula_salario()
        return salario_folha

    def dissidio_anual(self) -> None:
        '''
        Aumenta o valor da hora trabalhada em 5% para todos os funcionários
        '''
        for f in self.funcionarios_contratados:
            f.salario += (f.calcula_salario() * 0.05)
