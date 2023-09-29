from src.calculadora import Calculadora

class Test_Calculadora:

    def test_adicao():
        resultado = Calculadora.adicao(2, 3)
        assert resultado == 5

    def test_adicao_2(self):
        resultado = Calculadora.adicao(2, 5)
        assert resultado == 7

    def test_divisao(self):
        resultado = Calculadora.divisao(2, 2)
        assert resultado == 1

    def test_divisao_por_zero(self):
        resultado = Calculadora.divisao(2, 0)
        assert resultado == 'erro'

    def test_multi(self):
        resultado = Calculadora.multiplicacao(2, 5)
        assert resultado == 10

# Set-ExecutionPolicy RemoteSigned

# python install venv
# pip install venv
# python -m venv venv
# venv/Scripts/activate

# pip install pytest
