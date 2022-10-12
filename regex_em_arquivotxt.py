import re

with open("", "r") as arquivo:     #preencha com o nome do arquivo, de prefencia este arquivo deve estar na mesma pasta que o código

    for arquivo in arquivo:
        texto = str(arquivo)
        ref = re.compile(r"")   #insira o seu codigo REGEX
        busca = re.findall(ref, texto)
        print(busca)
