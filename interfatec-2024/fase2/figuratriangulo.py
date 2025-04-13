import math

letras_triangulo = "ABCDEFGHI"

entrada = int(input())
a = math.ceil(entrada / 9)
b = letras_triangulo[(entrada % 9) - 1]

print(f"{a}{b}")
