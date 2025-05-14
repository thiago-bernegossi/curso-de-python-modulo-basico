# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: knowledge_assessment.py
# DATA DE CRIAÇÃO: 13-05-2025
# DATA DE PUBLICAÇÃO: 13-05-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Questão 01-) Considere o fragmento de código que segue:
n = 33
r = n < 100
print(r, type(r))
# O que será impresso no console?
# Resposta: True <class 'bool'>.

# Questão 02-) Quantas vezes o texto 'Python!' é produzido com a execução do seguinte trecho de programa?
for i in range(4, 0, -1) :
    for j in range(1, i) :
        print('Python!')
# Resposta: 6.