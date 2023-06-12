#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = list()
for c in range(0,4):
    notas.append(float(input('Digite as notas: ')))
print(f'A primeira nota é {notas[0]}. ')
print(f'A segunda nota é {notas[1]}. ')
print(f'A terceira nota é {notas[2]}. ')
print(f'A quarta nota é {notas[3]}. ')

media = notas[0] + notas[1] + notas[2] + notas[3]

print(f'Por fim, a nota média é {round(media/4, 2)}.')