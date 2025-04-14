# Este exercício é muito fácil, o problema é a eficiência.
# Não me recordo se durante a competição em 2024 tivemos um timeout por execução.
# A ideia é selecionar três valores e retornar a mediana deles, o valor que não é nem o maior nem o menor.

# É possivel resolver o problema em apenas uma linha, mas para fins de aprendizado.
print(sorted(map(int, input().split()))[1])
