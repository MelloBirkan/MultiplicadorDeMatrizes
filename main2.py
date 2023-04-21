import os


def ler_dimensoes():
    m, n = map(int, input("Digite as dimensões da matriz (m n): ").split())
    return m, n


def ler_matriz(m, n):
    matriz = []
    print(f"Digite a matriz {m}x{n}:")
    for _ in range(m):
        matriz.append([int(x) for x in input().split()])
    return matriz


def carregar_matrizes_do_arquivo(nome_arquivo):
    if not os.path.exists(nome_arquivo):
        print("Arquivo não encontrado.")
        return None, None

    with open(nome_arquivo, 'r') as f:
        m, n = map(int, f.readline().split())
        A = [list(map(int, f.readline().split())) for _ in range(m)]
        n_b, p = map(int, f.readline().split())
        B = [list(map(int, f.readline().split())) for _ in range(n_b)]

    return A, B


def multiplicar_matrizes(A, B):
    linhasA, colunasA = len(A), len(A[0])
    linhasB, colunasB = len(B), len(B[0])

    if colunasA != linhasB:
        print("Matriz não multiplicável")
        return None

    matrizC = [[0] * colunasB for _ in range(linhasA)]

    for i in range(linhasA):
        for j in range(colunasB):
            for k in range(colunasA):
                matrizC[i][j] += A[i][k] * B[k][j]

    return matrizC


def resolver_exe1():
    print("Exercício 1)")

    opcao = input("Deseja carregar as matrizes de um arquivo? (s/n): ")

    if opcao.lower() == 's':
        nome_arquivo = input("Digite o nome do arquivo: ")
        A, B = carregar_matrizes_do_arquivo(nome_arquivo)
    else:
        m, n = ler_dimensoes()
        A = ler_matriz(m, n)
        n_b, p = ler_dimensoes()
        B = ler_matriz(n_b, p)

    resultado = multiplicar_matrizes(A, B)
    if resultado:
        print("Matriz resultante:")
        for linha in resultado:
            print(" ".join(map(str, linha)))


def resolver_exe2():
  
    print("Exercício 2)")
    A, B = carregar_matrizes_do_arquivo("exe2.txt")
    if A:
        resultado = multiplicar_matrizes(A, B)
        print(f"A) O contrutor precisará de {resultado[0][0]} ferros, {resultado[0][1]} madeiras, {resultado[0][2]} vidros, {resultado[0][3]} tintas e {resultado[0][4]} tijolos.")

        resultado = multiplicar_matrizes(B, [[15.00], [8, 00], [5, 00], [1, 00], [10, 00]])
        casa_moderna, casa_mediterraneo, casa_colonial = resultado[0][0], resultado[1][0], resultado[2][0]
        print(f"\nB) O valor da casa moderna é R${casa_moderna}\nO valor da casa mediterranea é R${casa_mediterraneo}\nO valor da casa colonial é R${casa_colonial}.\n")


def resolver_exe3():
  
  print("Exercício 3)")
  A, B = carregar_matrizes_do_arquivo("exe3.txt")
  if A:
    resultado = multiplicar_matrizes(A, B)
    mulheres, homens = resultado[1], resultado[0]
    comparar_grupos("carboidratos", mulheres[0], homens[0])
    comparar_grupos("proteínas", mulheres[1], homens[1])
    comparar_grupos("cilindros", mulheres[2], homens[2])


def comparar_grupos(tipo, mulheres, homens):
  if mulheres >= homens:
    print(f"As mulheres são as que mais comem {tipo}: {mulheres} - elas comem {mulheres - homens} a mais que os homens")
  else:
    print(f"Os homens são os que mais comem {tipo}: {homens} - eles comem {homens - mulheres} a mais que as mulheres")


def main():
    resolver_exe2()
    resolver_exe3()
    resolver_exe1()


if __name__ == "__main__":
  main()


