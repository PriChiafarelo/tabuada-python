"""faça um programa que leia um número inteiro qualquer e mostra na tela a sua tabuada"""
valor = int(input('Digite um valor para ver sua tabuada: '));


print(" Tabuada do ",valor,":\n")
for i in range(0,11):
    print(valor," X ",i," = ",valor*i)