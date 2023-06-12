#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

caractere = list()
vogais = ['A', 'E', 'I', 'O', 'U']
consoantes = list()
for c in range(1, 11):
    caractere.clear()
    x = caractere.append(str(input('Digite um caractere: ')))
    if x not in vogais:
        consoantes.append(caractere)
print(consoantes)
    