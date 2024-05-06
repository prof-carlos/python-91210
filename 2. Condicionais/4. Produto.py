import os
os.system("cls || clear")

print("Solicitando dados para o usuário.")
primeiroNumero = float(input("Digite a primeiro número: "))
segundoNumero = float(input("Digite a segundo número: "))

soma = primeiroNumero + segundoNumero
media = soma / 2
produto = primeiroNumero * segundoNumero

maior = max(primeiroNumero, segundoNumero)
menor = min(primeiroNumero, segundoNumero)

'''
if primeiroNumero > segundoNumero:
    maior = primeiroNumero
else: 
    maior = segundoNumero

if primeiroNumero < segundoNumero:
    menor = primeiroNumero
else: 
    menor = segundoNumero
'''

print("\nExibindo dados do usuário.")
print(f"Primeiro número: {primeiroNumero}")
print(f"Segundo número: {segundoNumero}")

print(f"\nSoma: {soma}")
print(f"Produto: {produto}")
print(f"Média: {media}")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")