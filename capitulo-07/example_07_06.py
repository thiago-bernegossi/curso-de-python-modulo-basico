# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_07_06.py
# DATA DE CRIAÇÃO: 23-05-2025
# DATA DE PUBLICAÇÃO: 23-05-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

print('Iterando e exibindo os elementos da lista 01: ')

list_01 = [21, 45, 17, 28]
for value in list_01:
    print(value)

print('\nIterando e exibindo os elementos da lista 01: ')

list_01 = [21, 45, 17, 28]
for value in list_01:
    print(value)
    value = 0
    print(value)
print(list_01)

print('\nIterando e exibindo os elementos da lista 01: ')

list_01 = [21, 45, 17, 28]
position = 0
for value in list_01:
    print(f'O elemento na posição {position} do índice da lista 01 contém o valor {value}')
    position += 1

print('\nA execução do sistema informático foi concluída.')