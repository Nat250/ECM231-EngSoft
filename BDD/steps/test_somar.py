from behave import given, when, then

@given('dois número inteiros: {num1:d} e {num2:d}')
def step_given(context, num1, num2):
    context.num1 = num1
    context.num2 = num2

@when('somar os dois número inteiros')
def step_when(context):
    context.resultado = context.num1 + context.num2

@then('o resultado deve ser {resultado:d}')
def step_then(context, resultado):
    assert context.resultado == resultado