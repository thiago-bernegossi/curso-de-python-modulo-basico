# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_06_02.py
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

try:
    object_a = float(input('Digite o primeiro número real: '))
    object_b = float(input('Digite o segundo número real: '))
    print(f'O resultado é: {object_a / object_b}.')
except ValueError:
    print('Digite somente números reais como valores.')
except ZeroDivisionError:
    print('O valor do segundo número real não pode ser 0.')
except:
    print('Não foi possível calcular a divisão.')

print('\nA execução do sistema informático foi concluída.')