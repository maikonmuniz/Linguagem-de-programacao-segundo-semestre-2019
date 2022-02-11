# Linguagem de Programação II
# AC08 SI2A - Sistemas da Informação - LMS
# alunos: maikon.silva@aluno.faculdadeimpacta.com.br


from sqlalchemy import (create_engine, MetaData,
                        Column, Integer, String,
                        ForeignKey, Date)

from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

# Setup do ambiente - Não é preciso alterar
load_dotenv()

# modifique o arquivo .env com os seus dados para realizar a conexão
user = os.environ.get("DB_USER")
pwd = os.environ.get("DB_PASS")
server = os.environ.get("DB_HOST")

engine = create_engine(f"mssql+pymssql://{user}:{pwd}@{server}/fit_alunos")

# Schema atualizado!
Base = declarative_base(bind=engine, metadata=MetaData
                        (schema="salas\\lms_si2a_ads2b"))


# Classes a serem criadas
# Crie todos os atributos (colunas) para as classes abaixo, e
# também  implemente o método __repr__


class Usuario(Base):
    '''
    Classe Usuario: mapeia a tabela usuário do Banco de dados
    '''
    __tablename__ = "Usuario"

    id_usuario = Column("IdUsuario", Integer, primary_key=True,
                        autoincrement=True)
    id_login = Column("IdLogin", String(30), unique=True, nullable=False)
    senha = Column("Senha", String(30))
    dt_expiracao = Column("DtExpiracao", Date)

    def __repr__(self):
        '''
        Método de representação do objeto
        '''
        return f'<Usuario: {self.id_login}>'


class Aluno(Base):
    '''
    Classe Aluno: mapeia a tabela Aluno do Banco de Dados
    possui um realacionamento com Usuario de nome usuario, e cria
    a backref perfil_aluno.
    '''
    __tablename__ = "Aluno"

    id_aluno = Column("IdAluno", Integer, primary_key=True, autoincrement=True)
    nome = Column("Nome", String(100), nullable=False)
    email = Column("Email", String(50), unique=True, nullable=False)
    celular = Column("Celular", String(14), unique=True, nullable=False)
    RA = Column("ra", Integer, unique=True, nullable=False)
    id_usuario = Column("IdUsuario", Integer, ForeignKey("Usuario.IdUsuario"))
    usuario = relationship("Usuario", backref="perfil_aluno")

    def __repr__(self):
        '''
        Método de representação do objeto
        '''
        return f"<Aluno: {self.nome}>"


class Professor(Base):
    '''
    Classe Professor: mapeia a tabela Profesor do Banco de Dados
    possui um realacionamento com Usuario de nome usuario, e cria
    a backref perfil_professor.
    '''
    __tablename__ = "Professor"

    id_professor = Column("IdProfessor", Integer, primary_key=True,
                          autoincrement=True)
    email = Column("Email", String(50), unique=True, nullable=False)
    celular = Column("Celular", String(14), unique=True, nullable=False)
    apelido = Column("Apelido", String(30), unique=True, nullable=False)
    id_usuario = Column("IdUsuario", Integer, ForeignKey("Usuario.IdUsuario"))
    usuario = relationship("Usuario", backref="perfil_professor")

    def __repr__(self):
        '''
        Método de representação do objeto
        '''
        return f'<Professor: {self.apelido}>'


class Coordenador(Base):
    '''
    Classe Coordenador: mapeia a tabela Profesor do Banco de Dados
    Possui um realacionamento com Usuario, de nome usuario, e cria
    a backref perfil_coordenador.
    Possui um relaciomento com Disciplina de nome disciplinas e cria
    a backref coordenador.
    '''
    __tablename__ = "Coordenador"

    id_coordenador = Column("IdCoordenador", Integer, primary_key=True,
                            autoincrement=True)
    nome = Column("Nome", String(30), nullable=False)
    email = Column("Email", String(50), unique=True, nullable=False)
    celular = Column("Celular", String(14), unique=True, nullable=False)
    id_usuario = Column("IdUsuario", Integer, ForeignKey("Usuario.IdUsuario"))
    usuario = relationship("Usuario", backref="perfil_coordenador")
    disciplinas = relationship("Disciplina", backref="coordenador")

    def __repr__(self):
        '''
        Método de representação do objeto
        '''
        return f'<Coordenador: {self.nome}>'


class Disciplina(Base):
    '''
    Classe Disciplina: mapeia a tabela Disciplina do Banco de Dados.
    Não é necessário colocar as restições das colunas: PercentualPrático,
    PercentualTeórico, CargaHoraria e StatusDisciplina
    '''
    __tablename__ = "Disciplina"

    id_disciplina = Column("IdDisciplina", Integer, primary_key=True,
                           autoincrement=True)
    nome = Column("Nome", String(30), unique=True, nullable=False)
    data_disciplina = Column("DataDisciplina", Date)
    status_disciplina = Column("StatusDisciplina", String(8))
    plano_de_ensino = Column("PlanoDeEnsino", String(500))
    carga_horaria = Column("CargaHoraria", Integer, nullable=True)
    competencias = Column("Competencias", String(500))
    habilidades = Column("Habilidades", String(500))
    ementa = Column("Ementa", String(500))
    conteudo_programatico = Column("ConteudoProgramatico", String(500))
    bibliografia_basica = Column("BibliografiaBasica", String(500))
    bibliografia_complementar = Column("BibliografiaComplementar", String(500))
    percentual_pratico = Column("PercentualPratico", Integer, nullable=False)
    percentual_teorico = Column("PercentualTeorico", Integer, nullable=False)
    id_coordenador = Column("IdCoordenador", Integer, ForeignKey
                            ("Coordenador.IdCoordenador"))

    def __repr__(self):
        '''
        Método de representação do objeto
        '''
        return f'<Disciplina: {self.nome}>'


class Curso(Base):
    '''
    Classe Curso: mapeia a tabela Curso do Banco de Dados.
    '''
    __tablename__ = "Curso"

    id_curso = Column("IdCurso", Integer, primary_key=True, autoincrement=True)
    nome = Column("Nome", String(50), nullable=True)

    def __repr__(self):
        '''
        Método de representação do objeto
        '''
        return f'<Curso: {self.nome}>'
