# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: validate_number.py
# DATA DE CRIAÇÃO: 15-05-2025
# DATA DE PUBLICAÇÃO: 15-05-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('Olá, vamos classificar um número:\n')

number = float(input('Digite um número: '))

if number == 0:
    print(f'\nO número escolhido ({number}) é igual a 0.')
elif number > 0:
    print(f'\nO número escolhido ({number}) é positivo.')
else:
    print(f'\nO número escolhido ({number}) é negativo.')