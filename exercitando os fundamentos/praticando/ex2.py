#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

vetor = list()
for c in range(1,11):
    vetor.append(float(input('Digite o número que deseja inserir no vetor: ')))
vetor.sort(reverse=True)
print(vetor)
