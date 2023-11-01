def contagem_regressiva(n):
    if n == 0:
        print("Fim")
    else:
        print(n)
        contagem_regressiva(n - 1)


n = int(input("Digite um valor: "))
contagem_regressiva(n)
