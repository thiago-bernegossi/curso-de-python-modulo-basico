# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: solved_exercise_05_03.py
# DATA DE CRIAÇÃO: 19-05-2025
# DATA DE PUBLICAÇÃO: 19-05-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Enunciado do Exercício 03:
# Escreva um programa que mostre na tela os 10 primeiros termos de uma progressão aritmética (PA) com primeiro termo P e razão R.
# Os dois números P e R são inteiros e devem ser lidos do teclado. 

# Resolução do Exercício 03:
print('A execução do sistema informático foi iniciada.\n')

print('Olá, vamos calcular uma Progressão Aritmética (PA):\n')

counter = 1
object_p = int(input('Digite o primeiro termo: '))
object_v = int(input('Digite a razão: '))

while counter <= 10:
    print(object_p, end=', ')
    object_p += object_v
    counter += 1

print(f'\n\nA execução do sistema informático foi concluída.')