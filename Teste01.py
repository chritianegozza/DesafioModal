'''1- A ModalGR possui um sistema em desenvolvimento que recebe dois vetores de 20 números 
inteiros. A partir desses valores armazenar em um terceiro vetor números que se repetem, por 
exemplo:
Entradas: a = [1, 2, 3, ... ] e b = [4, 2, 4, ... ]
Saída: [2]
Visando atender esse quesito, você foi escolhido para nos ajudar nessa solução! 
Após a finalização exibir em tela os valores do terceiro vetor.
Observações: 
 Valores repetidos no mesmo vetor não devem ser armazenados no vetor final;
 Caso o vetor ”a” contenha dois ou mais números repetidos e no vetor “b” contenha uma 
ou mais ocorrências desse valor, deve-se armazenar no vetor final apenas uma 
ocorrência dessa situação'''

def numeros_repetidos(a, b):
    valores_repetidos = [] #vetor para armazenar os números repetidos
    for valor in a: #Percorre cada número do vetor 
        if valor in b and valor not in valores_repetidos: # não deixa valores repetidos ir no novo vertor
            # Verifica se o número está presente no vetor 'b' e ainda não foi adicionado aos números repetidos
            valores_repetidos.append(valor) #Adiciona os numeros repetidos
    return valores_repetidos

a = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 10, 11, 12, 13, 14, 15, 16, 17, 18]
b = [4, 2, 4, 6, 7, 2, 9, 10, 10, 11, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]

terceiro_vetor = numeros_repetidos(a, b)
print("Entradas: a =", a, "e b =", b)
print("Saída:", terceiro_vetor)
