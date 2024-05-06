import os
os.system("cls || clear")

print("Solicitando dados para o usuário.")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
primeiraNota = float(input("Digite a primeira nota: "))
segundaNota = float(input("Digite a segunda nota: "))

media = (primeiraNota + segundaNota) / 2

print("\nExibindo dados do usuário.")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Primeira nota: {primeiraNota}")
print(f"Segunda nota: {segundaNota}")
print(f"Média: {media}")

if media >= 7:
    print("Aprovado.")
else: 
    print("Reprovado.")