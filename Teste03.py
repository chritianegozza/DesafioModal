''' 3) A ModalGR criará um programa de empréstimo para os colaboradores que possuem tempo 
de casa superior a 5 anos. O colaborador poderá simular um empréstimo de até 2 vezes o valor 
de seu respectivo salário, desde que esse valor seja múltiplo de 2. Esse programa dará a 
possibilidade de retirada em dinheiro vivo, de acordo com as seguintes opções:
 Notas de maior valor: considerando primeiramente as notas de 100 e 50 reais, e em 
seguida, as inferiores;
 Notas de menor valor: considerando as notas de 20, 10, 5 e 2 reais.
 Notas meio a meio: metade do valor em notas maiores e a outra metade em notas 
menores.
Essas opções deverão ser exibidas ao colaborador, para assim, realizar a escolha de acordo com 
sua necessidade.
Visando atender esse quesito, você foi escolhido para nos ajudar nessa solução! 
A ideia é ter os seguintes campos para inserção: do nome do colaborador, data de admissão, 
salário atual, valor de empréstimo, e em seguida, exibir as opções de retirada, por exemplo:
Valor empréstimo: 8.550 reais
Notas de maior valor: 
 85 x 100 reais;
 1 x 50 reais.
Notas de menor valor: 
 427 x 20 reais;
 1 x 10 reais.
Notas meio a meio:
4.275 reais em notas de maior valor:
 42 x 100 reais;
 1 x 50 reais;
 1 x 20 reais;
 1 x 5 reais.
4.275 reais em notas de menor valor:
 213 x 20 reais;
 1 x 10 reais;
 1 x 5 reais.
Observações: 
 Caso o colaborador não se enquadre nos requisitos mínimos de adesão ao programa 
de empréstimo, exiba a mensagem: Agradecemos seu interesse, mas você não atende 
os requisitos mínimos do programa.
 Caso o colaborador insira um valor de empréstimo que não seja múltiplo de 2, exiba a 
mensagem: Insira um valor válido'''




def calcular_emprestimo(nome, data_admissao, salario_atual, valor_emprestimo):
    # Verificar se o colaborador possui tempo de casa superior a 5 anos
    anos_trabalhados = calcular_anos_trabalhados(data_admissao)
    if anos_trabalhados < 5:
        print("Agradecemos seu interesse, mas você não atende os requisitos mínimos do programa.")
        return

    # Verificar se o valor do empréstimo é múltiplo de 2
    if valor_emprestimo % 2 != 0:
        print("Insira um valor válido (múltiplo de 2).")
        return

    # Calcular as opções de retirada
    notas_maior_valor = calcular_notas_maior_valor(valor_emprestimo)
    notas_menor_valor = calcular_notas_menor_valor(valor_emprestimo)
    notas_meio_a_meio = calcular_notas_meio_a_meio(valor_emprestimo)

    # Exibir as opções de retirada
    print("Valor empréstimo:", valor_emprestimo, "reais")
    print("Notas de maior valor:")
    for nota, quantidade in notas_maior_valor.items():
        print(" -", quantidade, "x", nota, "reais")
    print("Notas de menor valor:")
    for nota, quantidade in notas_menor_valor.items():
        print(" -", quantidade, "x", nota, "reais")
    print("Notas meio a meio:")
    print(valor_emprestimo // 2, "reais em notas de maior valor:")
    for nota, quantidade in notas_meio_a_meio['maior_valor'].items():
        print(" -", quantidade, "x", nota, "reais")
    print(valor_emprestimo // 2, "reais em notas de menor valor:")
    for nota, quantidade in notas_meio_a_meio['menor_valor'].items():
        print(" -", quantidade, "x", nota, "reais")

def calcular_anos_trabalhados(data_admissao):
    # Cálculo do tempo de trabalho em anos
    # Implementação fictícia apenas para fins de exemplo
    # Você pode utilizar bibliotecas como datetime para fazer esse cálculo corretamente
    anos = 2023 - int(data_admissao)
    return anos

def calcular_notas_maior_valor(valor_emprestimo):
    notas_maior_valor = {
        100: 0,
        50: 0
    }
    valor_restante = valor_emprestimo

    # Cálculo das notas de maior valor
    for nota in notas_maior_valor.keys():
        quantidade = valor_restante // nota
        notas_maior_valor[nota] = quantidade
        valor_restante -= quantidade * nota

    return notas_maior_valor

def calcular_notas_menor_valor(valor_emprestimo):
    notas_menor_valor = {
        20: 0,
        10: 0,
        5: 0,
        2: 0
    }
    valor_restante = valor_emprestimo

    # Cálculo das notas de menor valor
    for nota in notas_menor_valor.keys():
        quantidade = valor_restante // nota
        notas_menor_valor[nota] = quantidade
        valor_restante -= quantidade * nota

    return notas_menor_valor

def calcular_notas_meio_a_meio(valor_emprestimo):
    notas_meio_a_meio = {
        'maior_valor': {},
        'menor_valor': {}
    }
    valor_restante = valor_emprestimo

    # Cálculo das notas de maior valor
    notas_maior_valor = calcular_notas_maior_valor(valor_emprestimo // 2)
    valor_restante -= sum(notas_maior_valor.values()) * 100

    # Cálculo das notas de menor valor
    notas_menor_valor = calcular_notas_menor_valor(valor_restante)

    notas_meio_a_meio['maior_valor'] = notas_maior_valor
    notas_meio_a_meio['menor_valor'] = notas_menor_valor

    return notas_meio_a_meio

# Exemplo de uso
nome = "Christiane"
data_admissao = "2016" # Ano de admissão fictício
salario_atual = 5000
valor_emprestimo = 8550

calcular_emprestimo(nome, data_admissao, salario_atual, valor_emprestimo)
