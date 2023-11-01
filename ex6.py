def calc_imc(p):
    return peso / (altura * altura)


peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = calc_imc(peso)

print(f"Meu imc é: {imc:.2f}")
