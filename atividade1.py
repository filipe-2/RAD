notas = [("Carlos", 2.0), ("Lucas", 10.0), ("Maria", 5.5)]

# Abre o arquivo notas no modo de escrita
with open("notas.txt", "w") as arquivo:
    for par in notas:
        aluno = par[0] # Aluno na posição 0
        nota = par[1] # Nota do aluno na posição 1

        # Escreve no arquivo a situação do aluno
        arquivo.write(f"{aluno} obteve nota {nota}.\n")

# Lê o arquivo notas
with open("notas.txt", "r") as arquivo:
        print(arquivo.read())

# Tenta escrever no arquivo notas no modo leitura, tratando a exceção caso não seja possível
try:
    with open("notas.txt", "r") as arquivo:
        arquivo.write("Tentando abrir o arquivo no modo leitura.")
        print(arquivo.read())
except IOError as erro:
    # Retorna a descrição do erro caso ocorra
    print("========================================================")
    print(f"Erro durante a execução; descrição do erro: {erro}")
    print("========================================================") 