# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: solved_exercise_07_05.py
# DATA DE CRIAÇÃO: 25-05-2025
# DATA DE PUBLICAÇÃO: 25-05-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Enunciado do Exercício 05:
# Escreva um programa que permaneça em laço lendo números inteiros.
# O laço termina quando for digitado 0 (zero).
# Cada valor diferente de zero digitado deve ser colocado em uma lista.
# Ao final exiba a lista na tela e a quantidade de elementos que ela contém.  

# Resolução do Exercício 05:
print('A execução do sistema informático foi iniciada.\n')

print('Olá, vamos exibir uma lista de números inteiros e a quantidade de elementos que ela contém.\n')

object_n = int(input('Digite um número inteiro: '))
final_list = []

while object_n != 0:
    final_list.append(object_n)
    object_n = int(input('Digite outro número inteiro: '))

print(f'\nO resultado é:')
print(f'A lista de números inteiros é formada pelo(s) número(s) {final_list} e contém {len(final_list)} elemento(s).')

print(f'\nA execução do sistema informático foi concluída.')