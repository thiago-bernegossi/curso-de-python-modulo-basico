# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: solved_exercise_05_05.py
# DATA DE CRIAÇÃO: 19-05-2025
# DATA DE PUBLICAÇÃO: 19-05-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Enunciado do Exercício 05:
# Escreva um programa que permaneça em laço enquanto um valor inteiro lido for diferente de zero. 
# Totalize e conte os valores digitados, exceto o zero, e apresente esses valores na tela.
# Totalizar é somar os valores. 

# Resolução do Exercício 05:
print('A execução do sistema informático foi iniciada.\n')

object_a = int(input('Digite um número inteiro: '))
sum_of_objects = number_of_objects = 0

while object_a != 0:
    sum_of_objects += object_a 
    number_of_objects += 1
    object_a = int(input('Digite outro número inteiro: '))

print(f'\nA soma dos números digitados é {sum_of_objects}.')
print(f'A quantidade de números digitados é {number_of_objects}.')

print(f'\nA execução do sistema informático foi concluída.')