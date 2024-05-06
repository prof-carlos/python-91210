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

print("\nExibindo dados do usuário.")
print(f"Primeiro número: {primeiroNumero}")
print(f"Segundo número: {segundoNumero}")

print(f"\nSoma: {soma}")
print(f"Produto: {produto}")
print(f"Média: {media}")

if primeiroNumero == segundoNumero:
    print("Os números são iguais.")
else: 
    print(f"Maior número: {maior}")
    print(f"Menor número: {menor}")