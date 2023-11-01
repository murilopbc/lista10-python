try:
    num = int(input("Digite um número: "))
    num += 10
    print(num)
except ValueError:
    print("A resosta precisa ser um número!")
