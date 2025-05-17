# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: solved_exercise_04_04.py
# DATA DE CRIAÇÃO: 17-05-2025
# DATA DE PUBLICAÇÃO: 17-05-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Enunciado do Exercício 04:
# Escreva um programa para exibir na tela o nome e a categoria de um lutador.
# O programa deve ler um string para o nome e um número real para o peso.
# Conforme o peso ocorrerá o enquadramento na categoria, segundo esta tabela (fictícia): 

# +-------------+------------+    +-------------+------------+
# | Peso (kg)   | Categoria  |    | Peso (kg)   | Categoria  |
# +-------------+------------+    +-------------+------------+
# | menor que 52|            |    | maior ou    | Meio-médio |
# |             |            |    | igual a 79  |            |
# |             |            |    | e menor que |            |
# |             |            |    | 86          |            |
# +-------------+------------+    +-------------+------------+
# | maior ou    | Pena       |    | maior ou    | Médio      |
# | igual a 52  |            |    | igual a 86  |            |
# | e menor que |            |    | e menor que |            |
# | 65          |            |    | 90          |            |
# +-------------+------------+    +-------------+------------+
# | maior ou    | Leve       |    | maior ou    | Meio-pesado|
# | igual a 65  |            |    | igual a 90  |            |
# | e menor que |            |    | e menor que |            |
# | 72          |            |    | 100         |            |
# +-------------+------------+    +-------------+------------+
# | maior ou    | Ligeiro    |    | maior ou    | Pesado     |
# | igual a 72  |            |    | igual a 100 |            |
# | e menor que |            |    +-------------+------------+
# | 79          |            |
# +-------------+------------+

# Resolução do Exercício 04:
print('Olá, vamos classificar a categoria de um lutador:\n')

name = input('Digite o nome do lutador: ')
weight = float(input('Digite o peso do lutador: '))

if weight < 52:
    value = ''
elif weight >= 52 and weight < 65:
    value = 'Pena'
elif weight >= 65 and weight < 72:
    value = 'Leve'
elif weight >= 72 and weight < 79:
    value = 'Ligeiro'    
elif weight >= 79 and weight < 86:
    value = 'Meio-médio'    
elif weight >= 86 and weight < 90:
    value = 'Meio-pesado'    
else:
    value = 'Pesado'

if value != '':
    print(f'O lutador {name} pesa {weight} kg e se enquadra na categoria {value}.')
else:
    print(f'O lutador {name} pesa {weight} kg e não se enquadra em nenhuma categoria.')

print(f'\nA execução do sistema informático foi concluída.')