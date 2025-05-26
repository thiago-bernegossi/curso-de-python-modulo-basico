# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: solved_exercise_07_07.py
# DATA DE CRIAÇÃO: 26-05-2025
# DATA DE PUBLICAÇÃO: 26-05-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Enunciado do Exercício 07:
# Escreva um programa que leia um número inteiro Qtde e carregue uma lista com essa quantidade de números inteiros aleatórios.
# Exiba a lista na tela. 
# Em seguida inicie um laço que deve permanecer em execução enquanto um valor inteiro X for maior que zero.
# Para cada valor de X verifique se ele está ou não na lista gerada. Caso esteja é preciso exibir a quantidade de ocorrências. 

# Resolução do Exercício 07:
from random import randint

print('A execução do sistema informático foi iniciada.\n')

print('Olá, vamos exibir uma lista de números inteiros com a quantidade e a ocorrência de elementos aleatórios que ela contém.\n')

object_q = int(input('Digite a quantidade de números inteiros: '))
final_list = []

for counter in range(object_q):
    final_list.append(randint(1, 20))

print(f'\nO resultado é:')
print(f'A lista de números inteiros é formada pelo(s) número(s) {final_list}')

object_x = 1

while object_x > 0:
    object_x = int(input('\nDigite um número inteiro: '))
    if object_x in final_list:
        print(f'Há {final_list.count(object_x)} ocorrência(s) do número inteiro {object_x} na lista.')
    else:
        print(f'Não há ocorrência do número inteiro {object_x} na lista.')

print(f'\nA execução do sistema informático foi concluída.')