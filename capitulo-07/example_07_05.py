# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_07_05.py
# DATA DE CRIAÇÃO: 23-05-2025
# DATA DE PUBLICAÇÃO: 23-05-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

list_01 = []
list_01.append(81)
print(f'Exibindo os elementos da lista 01: {list_01}')

list_01.append(17)
list_01.append(49) 
list_01.append(53)  
print(f'Exibindo os elementos da lista 01 após adicionar três elementos: {list_01}\n')

list_01.clear()
print(f'Exibindo os elementos da lista 01 após limpar seus elementos: {list_01}')

list_01 = [81, 17, 49, 53]
print(f'Exibindo os elementos da lista 01 após adicionar quatro elementos: {list_01}\n')

list_02 = list_01.copy()
print(f'Exibindo os elementos da lista 01: {list_01}')
print(f'Exibindo os elementos da lista 02: {list_02}\n')

print(f'Exibindo o identificador da lista 01: {id(list_01)}')
print(f'Exibindo o identificador da lista 02: {id(list_02)}\n')

list_01.count(78)
print(f'Exibindo a ocorrência de elementos da lista 01 cujo valor é 78: {list_01.count(78)}')

new_value = list_01.count(81)
print(f'Exibindo a ocorrência de elementos da lista 01 cujo valor é 81: {new_value}\n')

list_01.append(81)
print(f'Exibindo os elementos da lista 01 após adicionar um elemento: {list_01}')

new_value = list_01.count(81)
print(f'Exibindo a ocorrência de elementos da lista 01 cujo valor é 81: {new_value}\n')

print(f'Exibindo os elementos da lista 01: {list_01}')
print(f'Exibindo os elementos da lista 02: {list_02}\n')

list_02 = [1, 2, 3, 4]
print(f'Exibindo os elementos da lista 02 após seus elementos serem alterados: {list_02}')

list_01.extend(list_02)
print(f'Exibindo os elementos da lista 01 após seus elementos serem estendidos da lista 02: {list_01}')

print(f'Exibindo os elementos da lista 02: {list_02}\n')

list_01.index(17)
print(f'Exibindo a posição de um elemento no índice da lista 01 cujo valor é 17: {list_01.index(17)}')
print(f'Exibindo a posição de um elemento no índice da lista 01 cujo valor é 49: {list_01.index(49)}\n')

print(f'Exibindo a existência de um elemento da lista 01 cujo valor é 50: {50 in list_01}')
print(f'Exibindo a existência de um elemento da lista 01 cujo valor é 81: {81 in list_01}')
print(f'Exibindo a existência de um elemento da lista 01 cujo valor é 2: {2 in list_01}\n')

print(f'Exibindo a posição de um elemento da lista 01 cujo valor é 2 e a posição é baseada em índice 0: {list_01.index(2, 0)}')
print(f'Exibindo a posição de um elemento da lista 01 cujo valor é 81 e a posição é baseada em índice 0: {list_01.index(81, 0)}')
print(f'Exibindo a posição de um elemento da lista 01 cujo valor é 81 e a posição é baseada em índice 1: {list_01.index(81, 1)}\n')

list_01.count(81)
print(f'Exibindo a ocorrência de elementos da lista 01 cujo valor é 81: {list_01.count(81)}\n')

print(f'Exibindo os elementos da lista 01: {list_01}\n')

list_01.insert(1, 195)
print(f'Exibindo os elementos da lista 01 após adicionar um elemento na posição 1 do índice: {list_01}')

list_01.insert(0, 2)
print(f'Exibindo os elementos da lista 01 após adicionar um elemento na posição 0 do índice: {list_01}\n')

print(f'Exibindo a quantidade de elementos da lista 01: {len(list_01)}\n')

list_01.insert(15, 35)
print(f'Exibindo os elementos da lista 01 após adicionar um elemento na última posição do índice: {list_01}\n')

new_value = list_01.pop(0)
print(f'Exibindo o elemento removido na posição 0 do índice da lista 01: {new_value}')

new_value = list_01.pop(4)
print(f'Exibindo o elemento removido na posição 4 do índice da lista 01: {new_value}\n')

new_value = list_01.pop()
print(f'Exibindo o elemento removido na última posição do índice da lista 01: {new_value}\n')

list_01.remove(17)
print(f'Exibindo os elementos da lista 01 após remover um elemento cujo valor é 17: {list_01}')

list_01.remove(81)
print(f'Exibindo os elementos da lista 01 após remover um elemento cujo valor é 81: {list_01}\n')

list_01 = [81, 195, 17, 49, 81, 1, 2 ,3, 4, 35]
print(f'Exibindo os elementos da lista 01 após adicionar dez elementos: {list_01}')

list_01.insert(0, 2)
print(f'Exibindo os elementos da lista 01 após adicionar um elemento na posição 0 do índice: {list_01}\n')

list_01.reverse()
print(f'Exibindo os elementos da lista 01 após inverter a order dos elementos: {list_01}')

list_01.reverse()
print(f'Exibindo os elementos da lista 01 após inverter a order dos elementos: {list_01}\n')

list_01.sort()
print(f'Exibindo os elementos da lista 01 após ordenar os elementos de forma crescente: {list_01}')

list_01.sort(reverse=True)
print(f'Exibindo os elementos da lista 01 após ordenar os elementos de forma decrescente: {list_01}')

print('\nA execução do sistema informático foi concluída.')