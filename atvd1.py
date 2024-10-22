def verificar_semelhanca(lados1, angulos1, lados2, angulos2):
    def sao_lados_proporcionais(l1, l2):
        # Verifica se os lados são proporcionais
        return abs(l1[0] / l2[0] - l1[1] / l2[1]) < 1e-6 and abs(l1[1] / l2[1] - l1[2] / l2[2]) < 1e-6

    def sao_angulos_congruentes(a1, a2):
        # Verifica se os ângulos são congruentes
        return abs(a1[0] - a2[0]) < 1e-6 and abs(a1[1] - a2[1]) < 1e-6

    resultados = {}

    # Critério LAL (Lado-Ângulo-Lado)
    # Verifica se dois lados são proporcionais e o ângulo entre eles é congruente
    if (abs(lados1[0] / lados2[0] - lados1[1] / lados2[1]) < 1e-6 and
        abs(angulos1[2] - angulos2[2]) < 1e-6):
        resultados['LAL'] = True
    else:
        resultados['LAL'] = False

    # Critério AA (Ângulo-Ângulo)
    # Verifica se dois ângulos são congruentes
    if sao_angulos_congruentes(angulos1[:2], angulos2[:2]):
        resultados['AA'] = True
    else:
        resultados['AA'] = False

    # Critério LLL (Lado-Lado-Lado)
    # Verifica se todos os lados são proporcionais
    if sao_lados_proporcionais(lados1, lados2):
        resultados['LLL'] = True
    else:
        resultados['LLL'] = False

    return resultados


def obter_valores_triangulo(n):
    print(f"Insira os valores para o triângulo {n}:")
    lados = []
    angulos = []

    # Recebe os valores dos lados
    for i in range(1, 4):
        lado = float(input(f"Digite o valor do lado {i}: "))
        lados.append(lado)

    # Recebe os valores dos ângulos
    for i in range(1, 4):
        angulo = float(input(f"Digite o valor do ângulo {i} (em graus): "))
        angulos.append(angulo)

    return lados, angulos


# Recebendo os valores dos dois triângulos do usuário
lados1, angulos1 = obter_valores_triangulo(1)
lados2, angulos2 = obter_valores_triangulo(2)

# Verificando se os triângulos são semelhantes e obtendo resultados
resultados = verificar_semelhanca(lados1, angulos1, lados2, angulos2)

# Exibindo os resultados de cada critério
if resultados['LAL']:
    print("Os triângulos são semelhantes pelo critério LAL (Lado-Ângulo-Lado).")
else:
    print("Os triângulos NÃO são semelhantes pelo critério LAL (Lado-Ângulo-Lado).")

if resultados['AA']:
    print("Os triângulos são semelhantes pelo critério AA (Ângulo-Ângulo).")
else:
    print("Os triângulos NÃO são semelhantes pelo critério AA (Ângulo-Ângulo).")

if resultados['LLL']:
    print("Os triângulos são semelhantes pelo critério LLL (Lado-Lado-Lado).")
else:
    print("Os triângulos NÃO são semelhantes pelo critério LLL (Lado-Lado-Lado).")
