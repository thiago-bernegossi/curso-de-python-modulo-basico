# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: solved_exercise_07_01.py
# DATA DE CRIAÇÃO: 23-05-2025
# DATA DE PUBLICAÇÃO: 24-05-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Enunciado do Exercício 01:
# Escreva um programa que leia três números inteiros: o primeiro termo P, a razão R e a quantidade Q de termos de uma progressão aritmética.
# O programa deve calcular os Q termos da progressão colocando-os em uma lista e no final exibi-la na tela. 
# Obs: esse problema já foi abordado, sem o uso de listas, no exercício resolvido 5.3.  

# Resolução do Exercício 01:
print('A execução do sistema informático foi iniciada.\n')

print('Olá, vamos calcular uma Progressão Aritmética (PA):\n')

counter = 0
final_list = []
object_p = int(input('Digite o primeiro termo: '))
object_r = int(input('Digite a razão: '))
object_q = int(input('Digite a quantidade de termos: '))

while counter < object_q:
    final_list.append(object_p)
    object_p += object_r
    counter += 1

print(f'\nO resultado é: {final_list}')

print(f'\nA execução do sistema informático foi concluída.')