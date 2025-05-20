# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_07_02.py
# DATA DE CRIAÇÃO: 20-05-2025
# DATA DE PUBLICAÇÃO: 20-05-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

first_list = [36, 26,21, 48 ,17, 9, 16, 23, 29, 31]

print('Exibindo uma lista completa: ')
print(f'{first_list}\n')

print('Exibindo a quantidade de elementos de uma lista completa: ')
print(f'{len(first_list)}\n')

print('Exibindo o tipo de uma lista: ')
print(f'{type(first_list)}\n')

print(f'No índice 0 da lista há um elemento de valor {first_list[0]}')
print(f'No índice 9 da lista há um elemento de valor {first_list[9]}')
print(f'No índice -1 da lista há um elemento de valor {first_list[-1]}')
print(f'No índice -2 da lista há um elemento de valor {first_list[-2]}')
print(f'No índice -3 da lista há um elemento de valor {first_list[-3]}')
print(f'No índice -10 da lista há um elemento de valor {first_list[-10]}\n')

print('Exibindo uma lista completa: ')
print(f'{first_list}\n')

new_value = 3
print(f'No índice 3 da lista há um elemento de valor {first_list[3]}')

first_list[new_value + 1]
print(f'No índice 4 da lista há um elemento de valor {first_list[4]}')

first_list[new_value - 1]
print(f'No índice 2 da lista há um elemento de valor {first_list[2]}')

first_list[new_value * 2]
print(f'No índice 6 da lista há um elemento de valor {first_list[6]}')

print('\nA execução do sistema informático foi concluída.')