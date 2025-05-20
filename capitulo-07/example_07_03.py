# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_07_03.py
# DATA DE CRIAÇÃO: 20-05-2025
# DATA DE PUBLICAÇÃO: 20-05-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

source_list = [36, 25, 21, 48, 17, 9, 16, 23, 29, 31]
print(f'Exibindo uma lista completa: {source_list}')

destination_list_01 = source_list[3:6]
print(f'Exibindo uma sublista: {destination_list_01}')

destination_list_02 = source_list[1:7:2]
print(f'Exibindo uma sublista: {destination_list_02}')

destination_list_03 = source_list[:4]
print(f'Exibindo uma sublista: {destination_list_03}')

destination_list_04 = source_list[6:]
print(f'Exibindo uma sublista: {destination_list_04}')

print('\nA execução do sistema informático foi concluída.')