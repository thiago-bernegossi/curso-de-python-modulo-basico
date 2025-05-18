# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: solved_exercise_05_01.py
# DATA DE CRIAÇÃO: 18-05-2025
# DATA DE PUBLICAÇÃO: 18-05-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Enunciado do Exercício 01:
# Escreva um programa que permaneça em laço enquanto um valor X lido for diferente de zero.
# Para cada valor de X apresente na tela se é par ou ímpar. 

# Resolução do Exercício 01:
print('A execução do sistema informático foi iniciada.\n')

print('Olá, vamos analisar se um número inteiro é par ou ímpar:\n')

counter = 1

while counter != 0:
    counter = int(input('Digite um número inteiro: '))
    if counter == 0:
        print(f'O número inteiro {counter} é par!')
        break
    if counter % 2 == 0:
        print(f'O número inteiro {counter} é par!')
        print('Digite outro número inteiro...\n')
    else:
        print(f'O número inteiro {counter} é ímpar!')
        print('Digite outro número inteiro...\n')

print(f'\nA execução do sistema informático foi concluída.')