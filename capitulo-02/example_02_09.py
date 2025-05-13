# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_02_09.py
# DATA DE CRIAÇÃO: 13-05-2025
# DATA DE PUBLICAÇÃO: 13-05-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

object_a = 10
object_a = object_a + 1
print(object_a)

object_a += 1 # OBS.: É equivalente a declarar: object_a = object_a + 1.
print(object_a)

object_a = 10
object_b = 4
object_a += object_b # OBS.: É equivalente a declarar: object_a = object_a + object_b.
print(object_a)

object_a -= object_b
print(object_a)

object_a *= object_b
print(object_a)

object_a /= object_b
print(object_a)
print(type(object_a))

object_a = 40
object_a //= object_b
print(object_a)
print(type(object_a))