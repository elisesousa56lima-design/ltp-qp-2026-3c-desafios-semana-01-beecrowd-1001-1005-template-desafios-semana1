7"""
Beecrowd 1001 - Extremamente Básico

Leia 2 valores inteiros e armazene-os nas variáveis A e B.
Efetue a soma de A e B atribuindo o seu resultado na variável X.
Imprima X conforme exemplo apresentado abaixo.
Não apresente mensagem alguma além daquilo que está sendo especificado e
não esqueça de imprimir o fim de linha após o resultado, caso contrário,
você receberá "Presentation Error".
"""

# Link do problema: https://judge.beecrowd.com/pt/problems/view/1001

# Escreva sua solução abaixo
# Lê as duas notas como ponto flutuante (double precision)
A = float(input())
B = float(input())

# Pesos: A = 3.5, B = 7.5
# Soma dos pesos = 3.5 + 7.5 = 11.0
peso_A = 3.5
peso_B = 7.5

# Cálculo da média ponderada
media = (A * peso_A + B * peso_B) / 11.0

# Imprime "MEDIA =" com 5 casas decimais
print(f"MEDIA = {media:.5f}")

