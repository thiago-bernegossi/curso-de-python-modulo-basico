# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: solved_exercise_04_01.py
# DATA DE CRIAÇÃO: 16-05-2025
# DATA DE PUBLICAÇÃO: 17-05-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Enunciado do Exercício 01:
# Escreva um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.
# Lembrando que para saber a paridade de um inteiro é preciso calcular o resto da sua divisão por 2.
# Se o resto for 0 o número é par, se o resto for 1 o número é ímpar.

# Resolução do Exercício 01:
print('Olá, vamos analisar se um número inteiro é par ou ímpar:\n')

integer = int(input('Digite um número inteiro: '))
if integer % 2 == 0:
    print(f'O número inteiro {integer} é par!')
else:
    print(f'O número inteiro {integer} é ímpar!')

print(f'\nA execução do sistema informático foi concluída.')