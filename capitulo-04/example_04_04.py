# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_04_04.py
# DATA DE CRIAÇÃO: 15-05-2025
# DATA DE PUBLICAÇÃO: 15-05-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

object_a = 0
object_b = 1

print(f'0 > 0: {object_a > 0}.')
print(f'0 não é > 0: {not object_a > 0}.')
print(f'0 == 0: {object_a == 0}.')
print(f'0 não é == 0: {not object_a == 0}.\n')

print(f'0 < 0 e 1 < 0: {object_a < 0 and object_b < 0}.')
print(f'0 < 0 e 1 == 1: {object_a < 0 and object_b == 1}.')
print(f'0 == 0 e 1 < 0: {object_a == 0 and object_b < 0}.')
print(f'0 == 0 e 1 == 1: {object_a == 0 and object_b == 1}.\n')

print(f'0 < 0 ou 1 < 0: {object_a < 0 or object_b < 0}.')
print(f'0 < 0 ou 1 == 1: {object_a < 0 or object_b == 1}.')
print(f'0 == 0 ou 1 < 0: {object_a == 0 or object_b < 0}.')
print(f'0 == 0 ou 1 == 0: {object_a == 0 or object_b == 0}.\n')

object_a = 15
object_b = 9
object_c = 9

print(f'9 == 9 ou 15 < 9 e 15 < 9: {object_b == object_c or object_a < object_b and object_a < object_c}.')
print(f'(9 == 9 ou 15 < 9) e 15 < 9: {(object_b == object_c or object_a < object_b) and object_a < object_c}.')