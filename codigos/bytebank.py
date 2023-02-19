from datetime import date


class Funcionario:
    def __init__(self, nome, data_nascimento: str, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, novo_salario):
        self._salario = novo_salario

    def idade(self):
        data_nascimento_quebrada = self._data_nascimento.split("/")
        ano_nascimento = data_nascimento_quebrada[-1]
        ano_atual = date.today().year
        return ano_atual - int(ano_nascimento)

    def sobrenome(self):
        nome_completo = self.nome.strip().title()
        nome_quebrado = nome_completo.split(" ")
        if len(nome_quebrado) == 1:
            raise Exception("Nome inserido não contem sobrenome")
        else:
            return nome_quebrado[-1]

    def _eh_socio(self):
        sobrenomes_diretores = ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Tudor', 'Ptolomeu']
        salario_igual_ou_maior_a_cem_mil = self.salario >= 100000
        eh_diretor = self.sobrenome() in sobrenomes_diretores
        return salario_igual_ou_maior_a_cem_mil and eh_diretor

    def decrescimo_salario(self):
        if self._eh_socio():
            decrescimo = self.salario * 0.1
            self.salario -= decrescimo

    def calcular_bonus(self):
        valor = self.salario * 0.1
        if valor > 1000:
            raise Exception("Inelegível para o bonus salarial")
        return valor

    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'
