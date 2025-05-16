# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_04_05.py
# DATA DE CRIAÇÃO: 15-05-2025
# DATA DE PUBLICAÇÃO: 15-05-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('Olá, vamos classificar o valor do pH de uma solução:\n')

ph_value = float(input('Digite o valor do pH: '))
if ph_value < 6.0:
    message = 'ácida'
elif ph_value < 7.0:
    message = 'levemente ácida'
elif ph_value == 7.0:
    message = 'neutra'
elif ph_value < 8.0:
    message = 'levemente alcalina'
else:
    message = 'alcalina'

print(f'\nCom o pH no valor de {ph_value} a solução é classificada como {message}.')