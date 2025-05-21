# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_07_04.py
# DATA DE CRIAÇÃO: 21-05-2025
# DATA DE PUBLICAÇÃO: 21-05-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

list_01 = [10, 12, 14, 16]
list_02 = list_01

print(f'Exibindo os elementos da lista 01: {list_01}')
print(f'Exibindo os elementos da lista 02: {list_02}\n')

list_02[0] = 99

print(f'Exibindo os elementos da lista 02 após um elemento ser alterado: {list_02}')
print(f'Exibindo os elementos da lista 01 após um elemento da lista 02 ser alterado: {list_01}\n')

print(f'Exibindo o identificador da lista 01: {id(list_01)}')
print(f'Exibindo o identificador da lista 02: {id(list_02)}\n')

list_01 = [10, 12, 14, 16]
list_02 = list_01[:]

print(f'Exibindo os elementos da lista 01: {list_01}')
print(f'Exibindo os elementos da lista 02: {list_02}\n')

list_02[0] = 99

print(f'Exibindo os elementos da lista 02 após um elemento ser alterado: {list_02}')
print(f'Exibindo os elementos da lista 01 após um elemento da lista 02 ser alterado: {list_01}\n')

print(f'Exibindo o identificador da lista 01: {id(list_01)}')
print(f'Exibindo o identificador da lista 02: {id(list_02)}')

print('\nA execução do sistema informático foi concluída.')