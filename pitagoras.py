def calcular_hipotenusa(a, b):
    hipotenusa = (a**2 + b**2)**0.5
    return hipotenusa

def calcular_cateto(a, c):
    b = (c**2 - a**2)**0.5
    return b

opcao = input("Escolha o que deseja calcular (hipotenusa/cateto): ").lower()

if opcao == "hipotenusa":
    cateto_a = float(input("Digite o cateto a: "))
    cateto_b = float(input("Digite o cateto b: "))

    hipotenusa = calcular_hipotenusa(cateto_a, cateto_b)
    print(f"A hipotenusa é: {hipotenusa:.1f}")

elif opcao == "cateto":
    cateto_conhecido = float(input("Digite o comprimento do cateto: "))
    hipotenusa = float(input("Digite o comprimento da hipotenusa: "))

    if cateto_conhecido >= 0 and hipotenusa >= 0:
        cateto_desconhecido = calcular_cateto(cateto_conhecido, hipotenusa)
        print(f"O comprimento do cateto desconhecido é: {cateto_desconhecido:.1f}")
    else:
        print("Por favor, insira valores válidos (não negativos) para os catetos e a hipotenusa.")

else:
    print("Opção inválida. Por favor, escolha 'hipotenusa' ou 'cateto'.")
