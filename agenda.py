# Linguagem de Programação II
# Atividade Contínua 04 - Classes e encapsulamento
#
# e-mails: maikon.silva@aluno.faculdadeimpacta.com.br



class Agenda:
    def __init__(self, titular, meu_numero, meu_email=''):
        """
        - O atributo titular recebe titular,
        - O atributo meu_numero deve ser um dicionário criado com a chave
        'principal' e o valor meu_numero (o número dado na criação da
        agenda de um dado titular sera sempre o número principal)
        Outros tipos de número do titular da agenda são adicionados com o
        o método set_meu_numero(), incluindo a atualização do número principal
        - O dicionário de contatos é um dicionário de dicionários:
        tem como chave o número de telefone principal e como valor
        um dicionário secundário cujas chaves são:
        'nome', 'email', 'principal', 'celular', 'trabalho', 'casa'
        todas as entradas devem possuir as 3 primeiras chaves da lista
        as demais chaves só devem ser criadas caso haja inclusão do dado
        - O atributo de meu_email recebe meu_email, e deve ser uma string
        vazia caso o email não seja fornecido

        Notem que:
        - todos os dados serão salvos com strings, pois assim
        é possível manter números de telefone que comecem com zero, por
        exemplo: '01188998899'
        - a escolha da chave do dicionário de contatos como o número de
        telefone principal se deve ao fato dos telefones serem sempre únicos
        (o que não é verdade para os nomes: é possível criar mais de um contato
        com o mesmo nome se quisermos, isso não é recomendável pois a busca por
        nome não será mais confiável, mas é uma possibilidade).
        """
        self.__titular = titular
        self.__meu_numero = {'principal': meu_numero}
        self.__meu_email = meu_email
        self.__contatos = {}

    def novo_contato(self, nome, telefone, tipo='principal', email='') -> None:
        """
        Insere um novo contato na agenda:
        Todo contato sempre tem o tipo 'principal', portanto
        se o tipo for diferente de 'principal', deve ser adicionada
        ao dicionário uma cópia de telefone com o tipo 'principal'
        o email é opicional e caso não seja fornecido, deverá ser vazio
        """
        if tipo == 'principal':
            self.__contatos[nome] = {tipo: telefone, "e-mail": email}
        else:
            self.__contatos[nome] = {
                'principal': telefone, tipo: telefone,
                'e-mail': email}

    def busca_contato(self, chave_busca) -> str:
        """
        Busca um contato na agenda por nome ou por número de telefone,
        Deve buscar tanto pelo telefone principal quanto por qualquer outro.
        Retorna a chave do contato encontrado (idem telefone principal)
        """
        for i, j in self.__contatos.items():
            for sem_ideia in j.values():
                if chave_busca == i or chave_busca == sem_ideia:
                    return i

    def novo_telefone(self, chave_busca, telefone, tipo='principal') -> None:
        """
        Em um contato existente:
        Se tipo não existir -> insere um novo tipo de telefone
        Se tipo existir -> atualiza o número de telefone
        Se tipo == 'principal' -> atualiza também a chave do contato
                                  no dicionário para <telefone>

        a chave_busca pode ser tanto um dos números ou o nome do contato.
        """
        for key_contato, busca_tipo in self.__contatos.items():
            for chave, numero in busca_tipo.items():
                if (tipo == chave and chave_busca == key_contato
                   or tipo == chave and chave_busca == numero):
                    self.__contatos[key_contato][chave] = telefone

        if tipo not in self.__contatos:
            self.__contatos[key_contato][tipo] = telefone

    def ligar(self, chave_busca, tipo='principal') -> None:
        """
        Busca um contato e liga para o telefone do tipo dado
        Imprime: 'Ligando para <nome_contato>: <telefone>'
        ou 'Contato não encontrado!', conforme o caso.
        """
        if chave_busca in self.__contatos:
            for nome, com_tipo in self.__contatos.items():
                for sem_ideia in com_tipo.keys():
                    if (chave_busca == nome and tipo == sem_ideia):
                        print('Ligando para {}: {}'.format(
                                chave_busca, self.__contatos[nome][sem_ideia]))

        else:
            print("Contato não encontrado!")

    def apagar_contato(self, chave_busca) -> None:
        """
        Busca um contato e o apaga do dicionário.
        Imprime 'Contato de <nome_contato> apagado com sucesso!'
        ou 'Contato não encontrado!', conforme o caso.
        """
        if chave_busca in self.__contatos:
            print('Contato de {} apagado com sucesso!'.format(chave_busca))
            del self.__contatos[chave_busca]

        else:
            print('Contato não encontrado!')

    def apagar_telefone(self, chave_busca, tipo) -> None:
        """
        Busca um contato, apaga o telefone dado em tipo e imprime:
        'Telefone <tipo> de <nome_contato> apagado com sucesso!'
        se tipo for 'principal', não apaga o telefone e imprime a mensagem:
        'Não é possível apagar o telefone principal!'
        Se o contato não existir, imprime: 'Contato não encontrado!'
        """
        if chave_busca in self.__contatos and tipo != 'principal':
            print('Telefone {} de {} apagado com sucesso!'.format(tipo,
                  chave_busca))
            del self.__contatos[chave_busca][tipo]

        elif chave_busca in self.__contatos and tipo == 'principal':
            print('Não é possível apagar o telefone principal!')

        else:
            print('Contato não encontrado!')

    def get_titular(self) -> str:
        return self.__titular

    def get_meu_numero(self, tipo='principal') -> str:
        return self.__meu_numero

    def get_meu_email(self) -> str:
        return self.__meu_email

    def set_meu_numero(self, numero, tipo) -> None:
        self.__meu_numero[tipo] = numero

    def set_meu_email(self, email) -> None:
        self.__meu_email = email
