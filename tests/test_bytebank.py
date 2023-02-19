from codigos.bytebank import Funcionario
from pytest import raises, mark


class TestClass:
    def test_quando_metodo_idade_recebe_13_03_2000_deve_retornar_23(self):
        # Um dos padrões de Testes: Given-When-Then

        entrada = "13/03/2000"  # Given: Contexto
        resultado_esperado = 23

        funcionario_teste = Funcionario("Teste", entrada, 2000)
        resultado = funcionario_teste.idade()  # When: Acão a ser executada

        assert resultado == resultado_esperado  # Then: Resultado do teste

    def test_quando_metodo_sobrenome_recebe_michael_jackson_deve_retornar_jackson_com_j_maiusculo(self):
        entrada = "michael jackson"  # Given
        resultado_esperado = "Jackson"

        funcionario_teste = Funcionario(entrada, "13/03/2000", 2000)
        resultado = funcionario_teste.sobrenome()  # When

        assert resultado == resultado_esperado  # Then

    def test_quando_metodo_sobrenome_nao_recebe_sobrenome_deve_retornar_exception(self):
        with raises(Exception):
            entrada = "michael"  # Given

            funcionario_teste = Funcionario(entrada, "13/03/2000", 2000)
            resultado = funcionario_teste.sobrenome()  # When

            assert resultado  # Then

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100_000  # Given
        entrada_nome = 'Paulo Bragança'
        resultado_esperado = 90_000

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funcionario_teste.decrescimo_salario()  # When
        resultado = funcionario_teste.salario

        assert resultado == resultado_esperado  # Then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada_salario = 1000  # Given
        resultado_esperado = 100

        funcionario_teste = Funcionario("Ana", "13/03/2000", entrada_salario)
        resultado = funcionario_teste.calcular_bonus()  # When

        assert resultado == resultado_esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_100000000_deve_retornar_exception(self):
        with raises(Exception):
            entrada_salario = 1000000  # Given

            funcionario_teste = Funcionario("Ana", "13/03/2000", entrada_salario)
            resultado = funcionario_teste.calcular_bonus()  # When

            assert resultado
