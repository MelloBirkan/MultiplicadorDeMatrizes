def multiplicar_matrizes(matrizA, matrizB):
  
  linhasA = len(matrizA)
  colunasA = len(matrizA[0])
  linhasB = len(matrizB)
  colunasB = len(matrizB[0])

  if colunasA == linhasB:
    matrizC = [[0]*linhasA for _ in range(colunasB)]

    for i in range(linhasA):
      for j in range(colunasB):
        for k in range(colunasA):
          matrizC[i][j] += matrizA[i][k] * matrizB[k][j]
        
    return matrizC
  else:
    return "Matriz não multiplicável"

def main():
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
    print(multiplicar_matrizes(A, B))


if __name__ == "__main__":
    main()

  
  