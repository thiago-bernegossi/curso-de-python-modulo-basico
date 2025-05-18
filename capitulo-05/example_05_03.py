# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_05_03.py
# DATA DE CRIAÇÃO: 18-05-2025
# DATA DE PUBLICAÇÃO: 18-05-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

counter = 1

while True:
    counter = int(input('Digite um número inteiro: '))
    if counter != 0:
        print(f'Escolha outro número inteiro...\n')
    else:
        print(f'O número inteiro digitado foi: {counter}.')    
        break                

print('\nA execução do sistema informático foi concluída.')