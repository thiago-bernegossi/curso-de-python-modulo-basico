# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: solved_exercise_04_02.py
# DATA DE CRIAÇÃO: 17-05-2025
# DATA DE PUBLICAÇÃO: 17-05-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Enunciado do Exercício 02:
# Escreva um programa que leia dois inteiros e mostre na tela apenas o menor dos dois.
# Se ambos forem iguais, mostre qualquer um deles. 

# Resolução do Exercício 02:
print('Olá, vamos analisar dois números e apresentar o menor deles:\n')

integer_01 = int(input('Digite o primeiro número inteiro: '))
integer_02 = int(input('Digite o segundo número inteiro: '))

if integer_01 <= integer_02:
    print(f'O menor número inteiro é {integer_01}.')
else:
    print(f'O menor número inteiro é {integer_02}.')

print(f'\nA execução do sistema informático foi concluída.')