# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: solved_exercise_05_02.py
# DATA DE CRIAÇÃO: 18-05-2025
# DATA DE PUBLICAÇÃO: 18-05-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Enunciado do Exercício 02:
# Escreva um programa que mostre na tela a tabuada do número inteiro N que deve ser lido do teclado. 

# Resolução do Exercício 02:
print('A execução do sistema informático foi iniciada.\n')

print('Olá, vamos exibir a tabuada de um número que você escolher.\n')

counter = 0
number = int(input('Digite um número inteiro: '))

while counter <= 10:
    print(f'{number} X {counter} = {number * counter}.')
    counter = counter + 1

print(f'\nA execução do sistema informático foi concluída.')