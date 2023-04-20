import os

# Função para multiplicar duas matrizes
def multiplicar_matrizes(matrizA, matrizB):
  
    # Obter as dimensões das matrizes A e B
    linhasA = len(matrizA)
    colunasA = len(matrizA[0])
    linhasB = len(matrizB)
    colunasB = len(matrizB[0])

    # Verificar se a multiplicação é possível
    if colunasA == linhasB:
        # Criar uma matriz C com a quantidade de linhas de A e colunas de B
        matrizC = [[0]*colunasB for _ in range(linhasA)]

        # Realizar a multiplicação das matrizes
        for i in range(linhasA):
            for j in range(colunasB):
                for k in range(colunasA):
                    matrizC[i][j] += matrizA[i][k] * matrizB[k][j]
        
        # Retornar a matriz resultante da multiplicação
        return matrizC
    else:
        # Retornar uma mensagem de erro se a multiplicação não for possível
        print("Matriz não multiplicável")
        return None

def carregar_matrizes_do_arquivo(nome_arquivo=None):
    if nome_arquivo is None:
        nome_arquivo = input("Digite o nome do arquivo: ")

    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r') as f:
            m, n = map(int, f.readline().split())
            A = [list(map(int, f.readline().split())) for _ in range(m)]
            n_b, p = map(int, f.readline().split())
            B = [list(map(int, f.readline().split())) for _ in range(n_b)]

        return A, B
    else:
        print("Arquivo não encontrado.")
        return None, None


def resolver_exe2():
  print("Exercício 2)\n")
  A, B = carregar_matrizes_do_arquivo("exe2.txt")
  if A: 
    resultado = multiplicar_matrizes(A, B)
    print(f"A)\tO contrutor precisará de {resultado[0][0]} ferros, {resultado[0][1]} madeiras, {resultado[0][2]} vidros, {resultado[0][3]} tintas e {resultado[0][4]} tijolos.")
    # Resolver valores
    resultado = multiplicar_matrizes(B, [[15.00], [8,00], [5,00], [1,00], [10,00]])
    casa_moderna = resultado[0][0]
    casa_mediterraneo = resultado[1][0]
    casa_colonial = resultado[2][0]
    print(f"B)\tO valor da casa moderna é R${casa_moderna}\n\tO valor da casa mediterranea é R${casa_mediterraneo}\n\tO valor da casa colonial é R${casa_colonial}.\n")


# Função principal
def main():
    resolver_exe2()
    # Perguntar ao usuário se deseja carregar as matrizes de um arquivo
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
        print(resultado)

# Iniciar a execução do programa
if __name__ == "__main__":
    main()

