class Calculadora:

    @staticmethod
    def adicao(a, b):
        return a + b
    
    @staticmethod
    def divisao(a, b):
        if b == 0:
            return 'erro'
        else: 
            return a / b
    
    @staticmethod
    def multiplicacao(a, b):
        return a * b