# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_02_07.py
# DATA DE CRIAÇÃO: 13-05-2025
# DATA DE PUBLICAÇÃO: 13-05-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

object_01 = 8
print(id(object_01))

object_01 = 12
print(id(object_01))

list_01 = [44, 17, 26, 35, 20]
print(id(list_01))
print(type(list_01))
print(list_01)
print(len(list_01))

print(list_01[0])
print(list_01[1])
print(list_01[2])
print(list_01[3])
print(list_01[4])

list_01[0] = 12
print(id(list_01))