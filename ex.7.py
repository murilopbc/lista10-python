def maior_n():
    num = input("Digite o número: ")
    num = num.split()
    num = [int(n) for n in num]

    if num:
        maior = num[0]
        for numero in num:
            if numero > maior:
                maior = numero
        return maior
    else:
        return None


maior = maior_n()
if maior is not None:
    print(f"O maior número digitado é: {maior}")
else:
    print("Nenhum número foi fornecido.")
