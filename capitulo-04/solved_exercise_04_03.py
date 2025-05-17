# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: solved_exercise_04_03.py
# DATA DE CRIAÇÃO: 17-05-2025
# DATA DE PUBLICAÇÃO: 17-05-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Enunciado do Exercício 03:
# Altere o programa anterior de modo que ele continue exibindo o menor dos dois valores lidos.
# Porém, quando forem iguais o programa deve exibir o valor junto com o texto "Os dois números são iguais".

# Resolução do Exercício 03:
print('Olá, vamos analisar dois números e apresentar o menor deles:\n')

integer_01 = int(input('Digite o primeiro número inteiro: '))
integer_02 = int(input('Digite o segundo número inteiro: '))

if integer_01 == integer_02:
    print(f'Os dois números inteiros são iguais e valem {integer_01}.')
else:
    if integer_01 < integer_02:
        print(f'O menor número inteiro é {integer_01}.')
    else:
        print(f'O menor número inteiro é {integer_02}.')

print(f'\nA execução do sistema informático foi concluída.')