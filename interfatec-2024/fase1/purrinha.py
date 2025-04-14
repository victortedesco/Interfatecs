QJ = int(input())
jogadores = [input().strip() for _ in range(QJ)]

pontos = [0] * QJ
NR = int(input())

for _ in range(NR):
    palitos = list(map(int, input().split()))
    palpites = list(map(int, input().split()))

    total_palitos = sum(palitos)

    for i in range(QJ):
        if palpites[i] == total_palitos:
            pontos[i] += 1
            break

    max_pontos = max(pontos)
    vencedores = [i for i, p in enumerate(pontos) if p == max_pontos]

    if len(vencedores) == 1:
        print(f"{jogadores[vencedores[0]]} GANHOU")
    else:
        print("EMPATE")
