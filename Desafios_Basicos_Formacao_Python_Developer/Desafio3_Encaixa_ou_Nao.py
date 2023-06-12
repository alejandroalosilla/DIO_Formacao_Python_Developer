"""
Desafio 3 (Encaixa ou Não?):
Paulinho tem em suas mãos um novo problema. Agora a sua professora lhe pediu que construísse um programa para verificar, à partir de dois valores muito grandes A e B, se B corresponde aos últimos dígitos de A.

Verifique, para cada entrada A e B, se os dois valores são compatíveis e imprima se "encaixa" ou "não encaixa" para cada uma das relações N vezes.
"""

n = int(input())

i = 0
while i < n:
    a, b = input().split()

    if a.endswith(b):
        print("encaixa")
    else:
        print("nao encaixa")

    i += 1