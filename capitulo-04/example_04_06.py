# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_04_06.py
# DATA DE CRIAÇÃO: 16-05-2025
# DATA DE PUBLICAÇÃO: 16-05-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Básico
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('Olá, vamos analisar o melhor investimento de acordo com o grau de risco e o valor aplicado:\n')

financial_risk = input('Digite ALTO ou BAIXO para o grau de risco: ')

if financial_risk != 'BAIXO' and financial_risk != 'ALTO':
    print(f'\nO valor digitado ({financial_risk}) é inválido!')
else:
    value = float(input('Agora, digite o valor aplicado: '))
    if financial_risk == 'BAIXO':
        if value < 1000.00:
            investment = 'Poupança'
        else:
            investment = 'Renda Fixa'
    else:
        if value < 1000.00:
            investment = 'Bitcoin'
        else:
            investment = 'Ações'
    print(f'\nApós a análise, o melhor investimento será em: {investment}.')