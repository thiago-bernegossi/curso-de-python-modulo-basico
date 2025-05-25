# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: solved_exercise_07_04.py
# DATA DE CRIAÇÃO: 25-05-2025
# DATA DE PUBLICAÇÃO: 25-05-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Enunciado do Exercício 04:
# Escreva um programa que leia um número inteiro N.
# Em seguida leia N números inteiros carregando os valores negativos em uma lista e os positivos em outra.
# Ao final exiba na tela cada uma das listas juntamente como seu tamanho.  
# Obs. Se o valor zero for fornecido ele deve ser incluído na lista de positivos. 

# Resolução do Exercício 04:
print('A execução do sistema informático foi iniciada.\n')

print('Olá, vamos classificar uma lista de números em positivos e negativos.\n')

object_n = int(input('Digite a quantidade de números: '))
negative_list = []
positive_list = []

for counter in range(object_n):
    value = int(input(f'Digite o elemento {counter}: '))
    if value >= 0:
        positive_list.append(value)
    else:
        negative_list.append(value)

print(f'\nO resultado é:')
print(f'A lista de números positivos é formada pelo(s) número(s) {positive_list} e contém {len(positive_list)} elemento(s).')
print(f'A lista de números negativos é formada pelo(s) número(s) {negative_list} e contém {len(negative_list)} elemento(s).')

print(f'\nA execução do sistema informático foi concluída.')