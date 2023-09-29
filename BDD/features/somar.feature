# pip install behave

Feature: Somar dois números
    Scenario: Realização de uma soma simples entre dois números
        Given dois número inteiros: 5 e 7
        When somar os dois número inteiros
        Then o resultado deve ser 12