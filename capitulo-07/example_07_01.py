# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_07_01.py
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

print(f'Exibindo os elementos de uma lista individualmente:')
counter = 0
while counter < len(first_list):
    print(f'No índice {counter} da lista há um elemento de valor {first_list[counter]}')
    counter += 1

print('\nA execução do sistema informático foi concluída.')