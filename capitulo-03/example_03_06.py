# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_03_06.py
# DATA DE CRIAÇÃO: 14-05-2025
# DATA DE PUBLICAÇÃO: 14-05-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

integer_value = input('Digite um número inteiro: ')
print(f'O número inteiro é: {integer_value}')
print(f'O tipo de objeto é: {type(integer_value)}\n')

float_value = input('Digite um número real: ')
print(f'O número real é: {float_value}')
print(f'O tipo de objeto é: {type(float_value)}\n')

result_of_concatenation = integer_value + float_value
print(f'O resultado da concatenação dos dois números é: {result_of_concatenation}\n')

integer_value = int(integer_value)
print(f'O número inteiro é: {integer_value}')
print(f'O tipo de objeto foi convertido para: {type(integer_value)}\n')

float_value = float(float_value)
print(f'O número real é: {float_value}')
print(f'O tipo de objeto foi convertido para: {type(float_value)}\n')

addition_result = integer_value + float_value
print(f'O resultado da soma dos dois números é: {addition_result}\n')

multiplication_result = integer_value * float_value
print(f'O resultado da multiplicação dos dois números é: {multiplication_result}')