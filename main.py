""" arquivo = open("texto.txt", "r")
print(arquivo.read())
print(arquivo.tell())
arquivo.close()
print(arquivo.closed) """

""" arquivo = open("novo.txt", 'w')
arquivo.write("Arquivo de escrita")
arquivo.close()
print(arquivo.closed) """

""" arquivo = open("frutas.txt", "w")
arquivo.write("banana\n")
arquivo.write("uva\n")
arquivo.write("mamao\n")
print(arquivo.read()) """

precos = [8000, 6000]

with open("precos_roupas.txt", "a") as arquivo:
    for preco in precos:
        arquivo.write(str(preco) + '\n')
        