import csv
# c=csv.writer(open("NOMES.csv","a"))
# c.writerow(["Cynthia","Lopes"])
# c.writerow(["Rosa","mae"])


class Arquivo(object):
    def salvar(self,nome,linha):
        objeto_arquivo=csv.writer(open(nome,"a"))
        objeto_arquivo.writerow(linha)


if __name__ == "__main__":
    teste_para_escrever_arquivo=Arquivo()
    teste_para_escrever_arquivo.salvar("teste.csv",["teste1","teste2"])
