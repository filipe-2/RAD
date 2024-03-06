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

'''
precos = [8000, 6000]

with open("precos_roupas.txt", "a") as arquivo:
    for preco in precos:
        arquivo.write(str(preco) + '\n')
'''

# disciplinas = ["Rad \n", "introdução a C \n", "Program"]
# with open("displicinas.txt", "w") as file:
#     file.write("Relação de disciplinas \n")
#     file.writelines(disciplinas)

# with open("displicinas.txt", "r") as file:
#     print(file.read())

# with open("texto.txt", "r") as arquivo:
#     print("Representação original da linha")

#     for linha in arquivo:
#         print(repr(linha))

# with open("texto.txt", "r") as arquivo:
#     print("=================================")
#     print("Conteúdo da linha:\n")

#     for linha in arquivo:
#         linha_ = linha.strip()
        
#         print(repr(linha_))
#     print("=================================")

'''minha_lista = ["Arroz", "Feijão", "Carne"]
lista_ = '.'.join(minha_lista)

with open("texto.txt", "w") as arquivo:
    arquivo.write(lista_)'''

'''try:
    with open("arquivo_teste.txt", "r") as arquivo:
        print(arquivo.read())
except FileNotFoundError:
    print("Arquivo inexistente")'''

'''import os
try:
    os.remove("teste.txt")
    print("Arquivo removido")
except FileNotFoundError as erro:
    print("Arquivo inexistente")
    print("Descrição:", erro)'''

try:
    f = open("novo.txt", "r")
    f.write("Hello")
except IOError as erro:
    print("O erro foi:", erro)