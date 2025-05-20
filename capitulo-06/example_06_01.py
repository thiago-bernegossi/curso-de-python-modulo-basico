# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_06_01.py
# DATA DE CRIAÇÃO: 19-05-2025
# DATA DE PUBLICAÇÃO: 19-05-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

print('Olá, vamos calcular a divisão entre dois números reais:\n')

object_a = float(input('Digite o primeiro número real: '))
object_b = float(input('Digite o segundo número real: '))

try:
    print(f'O resultado é: {object_a / object_b}.')
except:
    print('Não foi possível calcular a divisão.')

print('\nA execução do sistema informático foi concluída.')