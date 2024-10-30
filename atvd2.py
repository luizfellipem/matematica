# Função para calcular a razão das partes formadas pela bissetriz interna
def bissetriz_interna(lado_a, lado_b, lado_c):
    # A bissetriz interna divide o lado oposto em partes proporcionais aos dois outros lados
    return lado_b / lado_c

# Função para calcular a divisão do lado oposto pela bissetriz externa
def bissetriz_externa(lado_a, lado_b, lado_c):
    # A bissetriz externa divide o lado oposto em uma razão envolvendo os lados adjacentes
    return lado_b / lado_a

# Função principal para permitir a escolha da bissetriz interna ou externa
def calcular_bissetriz():
    print("Escolha o tipo de bissetriz para calcular: ")
    print("1. Bissetriz Interna")
    print("2. Bissetriz Externa")

    escolha = input("Indique 1 para Bissetriz Interna ou 2 para Bissetriz Externa: ")

    if escolha == "1":
        print("Cálculo da razão das partes formadas pela bissetriz interna.")
        lado_a = float(input("Indique o valor do lado A: "))
        lado_b = float(input("Indique o valor do lado B: "))
        lado_c = float(input("Indique o valor do lado C (lado oposto à bissetriz): "))

        # Razão das partes formadas pela bissetriz interna
        razao = bissetriz_interna(lado_a, lado_b, lado_c)
        print(f"A razão das partes formadas pela bissetriz interna é {razao:.2f}.")

    elif escolha == "2":
        print("Cálculo da divisão do lado oposto pela bissetriz externa.")
        lado_a = float(input("Indique o valor do lado A: "))
        lado_b = float(input("Indique o valor do lado B: "))
        lado_c = float(input("Indique o valor do lado C (lado oposto à bissetriz): "))

        # Divisão do lado oposto pela bissetriz externa
        razao_externa = bissetriz_externa(lado_a, lado_b, lado_c)
        print(f"A divisão do lado oposto pela bissetriz externa é {razao_externa:.2f}.")

    else:
        print("Escolha inválida! Por favor, escolha 1 ou 2.")

# Executar o programa
calcular_bissetriz()