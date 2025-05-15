# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_04_02.py
# DATA DE CRIAÇÃO: 15-05-2025
# DATA DE PUBLICAÇÃO: 15-05-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('Olá, vamos calcular a divisão entre dois números inteiros:\n')

object_a = int(input('Digite o primeiro número inteiro: '))
object_b = int(input('Digite o segundo número inteiro: '))

if object_b == 0:
    print('\nNão foi possível calcular a divisão.')
else:
    print(f'\nO resultado da divisão é: {object_a / object_b}.')