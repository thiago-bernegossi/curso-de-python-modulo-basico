# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: solved_exercise_07_02.py
# DATA DE CRIAÇÃO: 25-05-2025
# DATA DE PUBLICAÇÃO: 25-05-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Enunciado do Exercício 02:
# Usando a classe range, escreva um programa que leia três números inteiros: o primeiro termo P, a razão R e a quantidade Q de termos de uma progressão aritmética.
# O programa deve calcular os Q termos da progressão colocando-os em uma lista e no final exibi-la na tela. 
# Obs: é o mesmo enunciado do exercício resolvido anterior 7.1. 

# Resolução do Exercício 02:
print('A execução do sistema informático foi iniciada.\n')

print('Olá, vamos calcular uma Progressão Aritmética (PA):\n')

object_p = int(input('Digite o primeiro termo: '))
object_r = int(input('Digite a razão: '))
object_q = int(input('Digite a quantidade de termos: '))
stop_value = object_p + object_r * (object_q - 1)
final_list = list(range(object_p, stop_value + 1, object_r)) 

print(f'\nO resultado é: {final_list}')

print(f'\nA execução do sistema informático foi concluída.')