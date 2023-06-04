''' 2) A ModalGR possui um sistema em desenvolvimento sobre notas musicais, no qual cada uma 
das 7 notas possui um grau representado por um algarismo romano conforme abaixo:
A ideia é receber um vetor de notas e retornar um outro vetor com os respectivos graus da 
escala, por exemplo:
Entrada: ['Ré', 'Sol', 'Dó']
Saída: ['II', 'V', 'I']
Visando atender esse quesito, você foi escolhido para nos ajudar nessa solução! 
Após a finalização exibir em tela a saída de acordo com a entrada das notas musicais'''

def converter_notas(notas):
    # Dicionário que mapeia cada nota para o seu grau romano correspondente
    escala = {
        'Dó': 'I',
        'Ré': 'II',
        'Mi': 'III',
        'Fá': 'IV',
        'Sol': 'V',
        'Lá': 'VI',
        'Si': 'VII'
    }
    graus = [] # Vetor para armazenar os graus das notas
    
    # Percorre cada nota do vetor de notas de entrada
    for nota in notas:
        # Verifica se a nota está presente no dicionário de escala
        if nota in escala:
            # Adiciona o grau correspondente ao vetor de graus
            graus.append(escala[nota])
    return graus

notas = ['Ré', 'Sol', 'Dó']
graus = converter_notas(notas)
print("Entrada:", notas)
print("Saída:", graus)
