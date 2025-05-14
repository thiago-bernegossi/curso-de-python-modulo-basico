# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_02_10.py
# DATA DE CRIAÇÃO: 13-05-2025
# DATA DE PUBLICAÇÃO: 13-05-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

import math

object_x = 49
print(math.sqrt(object_x))

object_x = 81
print(math.sqrt(object_x))

print(math.pi)

print(math.sin(math.pi / 2))

print(math.cos(math.pi / 2))

object_y = math.cos(math.pi / 2)
result = round(object_y)
print(result)

result = round(object_y, 3)
print(result)

object_y = 18.71428999
result = round(object_y, 3)
print(result)

object_y = 18.71458999
result = round(object_y, 3)
print(result)