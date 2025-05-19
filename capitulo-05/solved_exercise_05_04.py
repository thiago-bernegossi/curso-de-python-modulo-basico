# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: solved_exercise_05_04.py
# DATA DE CRIAÇÃO: 19-05-2025
# DATA DE PUBLICAÇÃO: 19-05-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Enunciado do Exercício 04:
# Escreva um programa que leia do teclado um número inteiro D. Esse número deve ser obrigatoriamente maior que zero.
# Em seguida exiba na tela todos os números inteiros menores que 100 e que sejam divisíveis por D.

# Resolução do Exercício 04:
print('A execução do sistema informático foi iniciada.\n')

object_d = int(input('Digite um número inteiro: '))

while object_d <= 0 or object_d > 99:
    print(f'O valor {object_d} é inválido.')
    object_d = int(input('\nDigite outro número inteiro: '))
else:
    counter = 1    
    while counter < 100:        
        if counter % object_d == 0:
            print(counter, end=' ')
        counter +=1

print(f'\n\nA execução do sistema informático foi concluída.')