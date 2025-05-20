# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: list_operations.py
# DATA DE CRIAÇÃO: 20-05-2025
# DATA DE PUBLICAÇÃO: 20-05-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

second_list = []
second_list.append(71)
second_list.append(18)
second_list.append(36)

print('Exibindo uma lista completa: ')
print(f'{second_list}\n')

second_list.append(44)

print('Exibindo uma lista completa após adicionar um elemento: ')
print(f'{second_list}\n')

del second_list[1]

print('Exibindo uma lista completa após remover um elemento: ')
print(f'{second_list}\n')

second_list[0] = 999

print('Exibindo uma lista completa após alterar um elemento: ')
print(f'{second_list}')

print('\nA execução do sistema informático foi concluída.')