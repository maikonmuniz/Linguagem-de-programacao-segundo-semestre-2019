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
    log = ses.query(Usuario)
    log_string = list()

    for login in log:
        log_string.append(login.id_login)

    return log_string


def lista_alunos() -> List[str]:
    '''
    retorna uma lista com os nomes de todos os Alunos do banco.
    '''
    nome_aluno = ses.query(Aluno)
    nome_string = list()

    for nome_a in nome_aluno:
        nome_string.append(nome_a.nome)

    return nome_string


def lista_cursos() -> List[str]:
    '''
    retorna uma lista com os nomes de todos os Cursos do banco.
    '''
    curso_nome = ses.query(Curso)
    curso_string = list()

    for curso_n in curso_nome:
        curso_string.append(curso_n.nome)

    return curso_string


def lista_professores() -> List[str]:
    '''
    retorna uma lista com os apelidos de todos os professores do banco.
    '''
    pro_apelido = ses.query(Professor)
    apelido_string = list()

    for apelido_p in pro_apelido:
        apelido_string.append(apelido_p.apelido)

    return apelido_string


def lista_coordenadores() -> List[str]:
    '''
    retorna uma lista com os nomes de todos os coordenadores do banco.
    '''
    coorde_lista = ses.query(Coordenador)
    coorde_string = list()

    for coorde in coorde_lista:
        coorde_string.append(coorde.nome)

    return coorde_string


def lista_disciplinas() -> List[str]:
    '''
    retorna uma lista com o nome de todas as Discplinas do banco.
    '''
    disc_list = ses.query(Disciplina)
    disc_string = list()

    for disc in disc_list:
        disc_string.append(disc.nome)

    return disc_string


def carga_horaria_total() -> int:
    '''
    retorna a soma da carga horária de todas as diciplinas do banco
    '''
    soma_cargaH = ses.query(Disciplina)
    soma_numeros = list()

    for soma_desempacota in soma_cargaH:
        soma_numeros.append(soma_desempacota.carga_horaria)

    total = sum(soma_numeros)

    return total


def monta_coordenadores() -> Dict[str, List[str]]:
    '''
    Retorna um dicionario cujo as chaves são os nome dos
    coordenadores, e o valor é uma lista com os nomes das
    disciplinas que ele coordena. Caso um professor não coordene
    nenhuma diciplina o valor é uma lista vazia.
    '''
    coorde_disciplina = dict()
    lista_disc = list()
    coordenador_tbl = ses.query(Coordenador)

    for coorde_nome in coordenador_tbl.nome:
        for disc_lista in coordenador_tbl.disciplinas:
            lista_disc.append(disc_lista)
        coorde_disciplina[coorde_nome] = lista_disc

    return coorde_disciplina


if __name__ == '__main__':
    # Use esta área para testar sua funções, compare o resultado
    # obtido aqui com o feito direto com SELECT no SQL SERVER
    pass
