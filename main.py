import os
from threading import Thread

# Função para realizar a multiplicação de uma linha de A por uma coluna de B
def multiplicar_elemento(i, j, matrizA, matrizB, matrizC):
    for k in range(len(matrizA[0])):
        matrizC[i][j] += matrizA[i][k] * matrizB[k][j]

# Função para multiplicar duas matrizes utilizando threads
def multiplicar_matrizes(matrizA, matrizB):
    linhasA, colunasA = len(matrizA), len(matrizA[0])
    linhasB, colunasB = len(matrizB), len(matrizB[0])

    if colunasA != linhasB:
        print("Matriz não multiplicável")
        return None

    matrizC = [[0] * colunasB for _ in range(linhasA)]

    threads = []
    for i in range(linhasA):
        for j in range(colunasB):
            thread = Thread(target=multiplicar_elemento, args=(i, j, matrizA, matrizB, matrizC))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

    return matrizC


# Função para carregar matrizes de um arquivo
def carregar_matrizes_do_arquivo(nome_arquivo=None):
    if nome_arquivo is None:
        nome_arquivo = input("Digite o nome do arquivo: ")

    # Verificar se o arquivo existe
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r') as f:
            # Ler as dimensões das matrizes A e B do arquivo
            m, n = map(int, f.readline().split())
            A = [list(map(int, f.readline().split())) for _ in range(m)]
            n_b, p = map(int, f.readline().split())
            B = [list(map(int, f.readline().split())) for _ in range(n_b)]

        return A, B
    else:
        print("Arquivo não encontrado.")
        return None, None

# Função para resolver o problema 1 e calcular a matriz resultante
def resolver_exe1_resolver_matriz():
    # Perguntar ao usuário se deseja carregar as matrizes de um arquivo
    print("Exercício 1)\n")
    opcao = input("Deseja carregar as matrizes de um arquivo? (s/n): ")

    if opcao.lower() == 's':
        A, B = carregar_matrizes_do_arquivo()


    else:
        # Ler a matriz A
        A = []
        m = int(input("Digite o número de linhas da matriz A: "))
        n = int(input("Digite o número de colunas da matriz A: "))
        print("Digite os elementos da matriz A:")
        for i in range(m):
            A.append([int(x) for x in input().split()])

        # Ler a matriz B
        B = []
        n_b = int(input("Digite o número de linhas da matriz B: "))
        p = int(input("Digite o número de colunas da matriz B: "))
        print("Digite os elementos da matriz B:")
        for i in range(n_b):
            B.append([int(x) for x in input().split()])

    # Chamar a função multiplicar_matrizes passando as matrizes como argumentos
    resultado = (multiplicar_matrizes(A, B))
    if resultado:
      print("Resultado:")
      for linha in resultado:
        print(" ".join(str(x) for x in linha))
# Função para resolver o problema 2
def resolver_exe2():
    print("Exercício 2)\n")
    A, B = carregar_matrizes_do_arquivo("exe2.txt")
    if A:
        resultado = multiplicar_matrizes(A, B)
        print(
            f"A)\tO contrutor precisará de {resultado[0][0]} ferros, {resultado[0][1]} madeiras, {resultado[0][2]} vidros, {resultado[0][3]} tintas e {resultado[0][4]} tijolos."
        )
        # Resolver valores
        resultado = multiplicar_matrizes(
            B, [[15.00], [8, 00], [5, 00], [1, 00], [10, 00]])
        casa_moderna = resultado[0][0]
        casa_mediterraneo = resultado[1][0]
        casa_colonial = resultado[2][0]
        print(
            f"\nB)\tO valor da casa moderna é R${casa_moderna}\n\tO valor da casa mediterranea é R${casa_mediterraneo}\n\tO valor da casa colonial é R${casa_colonial}.\n"
        )

# Função para resolver o problema 3
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


# Função principal
def main():
    resolver_exe2()
    resolver_exe3()
    resolver_exe1_resolver_matriz()

# Iniciar a execução do programa
if __name__ == "__main__":
    main()

