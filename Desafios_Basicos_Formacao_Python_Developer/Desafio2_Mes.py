"""
Desafio 2 (Mes): 
Leia um valor inteiro entre 1 e 12, inclusive. Correspondente a este valor, deve ser apresentado como resposta o mês do ano por extenso, em inglês, com a primeira letra maiúscula.

Faça uma relação entre as possíveis entradas e os meses (em inglês).
Imprima o valor de cada chave em relação as entradas do programa.
"""

month = input()

months_dict = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June',
7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}

print(months_dict[int(month)])
