# Linguagem de Programação II
# AC09 SI2A - Sistema da Informação - Querys LMS
# alunos: maikon.silva@aluno.faculdadeimpacta.com.br

from lms import (engine, Usuario, Aluno, Professor,
                 Coordenador, Disciplina, Curso)
from sqlalchemy.orm import sessionmaker
from typing import List, Dict

# Setup: não alterar
Session = sessionmaker(engine)
ses = Session()

# Funções de Query para implementar


def lista_logins() -> List[str]:
    '''
    retorna uma lista com todos os logins de Usuarios presentes no banco.
    '''
    log = ses.query(Usuario.logins).all()
    return log


def lista_alunos() -> List[str]:
    '''
    retorna uma lista com os nomes de todos os Alunos do banco.
    '''
    nome_aluno = ses.query(Aluno.nome).all()
    return nome_aluno


def lista_cursos() -> List[str]:
    '''
    retorna uma lista com os nomes de todos os Cursos do banco.
    '''
    curso_nome = ses.query(Curso.nome).all()
    return curso_nome


def lista_professores() -> List[str]:
    '''
    retorna uma lista com os apelidos de todos os professores do banco.
    '''
    pro_apelido = ses.query(Professor.apelido).all()
    return pro_apelido


def lista_coordenadores() -> List[str]:
    '''
    retorna uma lista com os nomes de todos os coordenadores do banco.
    '''
    coorde_lista = ses.query(Coordenador.nome).all()
    return coorde_lista


def lista_disciplinas() -> List[str]:
    '''
    retorna uma lista com o nome de todas as Discplinas do banco.
    '''
    disc_list = ses.query(Disciplina.nome).all()
    return disc_list


def carga_horaria_total() -> int:
    '''
    retorna a soma da carga horária de todas as diciplinas do banco
    '''
    soma_cargaH = ses.query(Disciplina.carga_horaria).all()
    total = sum(soma_cargaH)
    return total


def monta_coordenadores() -> Dict[str, List[str]]:
    '''
    Retorna um dicionario cujo as chaves são os nome dos
    coordenadores, e o valor é uma lista com os nomes das
    disciplinas que ele coordena. Caso um professor não coordene
    nenhuma diciplina o valor é uma lista vazia.
    '''
    coorde_disciplina = dict()
    lista = []

    for coorde in ses.query(Coordenador):
        lista = ses.query(Disciplina.carga_horaria).all()
        coorde_disciplina[coorde.nome] = lista


if __name__ == '__main__':
    # Use esta área para testar sua funções, compare o resultado
    # obtido aqui com o feito direto com SELECT no SQL SERVER
    pass
