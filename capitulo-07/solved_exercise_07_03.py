# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: solved_exercise_07_03.py
# DATA DE CRIAÇÃO: 25-05-2025
# DATA DE PUBLICAÇÃO: 25-05-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Enunciado do Exercício 03:
# Escreva um programa que leia um número inteiro N.
# Em seguida leia N números reais carregando-os em uma lista.
# Ao final exiba os elementos da lista na tela, sendo um em cada linha.  

# Resolução do Exercício 03:
print('A execução do sistema informático foi iniciada.\n')

print('Olá, vamos exibir uma lista com números reais.\n')

object_n = int(input('Digite a quantidade de números: '))
final_list = []

for counter in range(object_n):
    message = float(input(f'Digite o elemento {counter}: '))
    final_list.append(message)

print(f'\nO resultado é:')

for value in final_list:
    print(f'{value:.2f}')

print(f'\nA execução do sistema informático foi concluída.')