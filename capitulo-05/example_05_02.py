# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_05_02.py
# DATA DE CRIAÇÃO: 18-05-2025
# DATA DE PUBLICAÇÃO: 18-05-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

counter = 0

while counter < 25:    
    counter = counter + 1
    if counter % 4 == 0:
        print('_', end='   ')
        continue
    print(counter, end='   ')

print('\n\nA execução do sistema informático foi concluída.')