# module Imports
import mariadb
import sys 
import time
import statistics



# connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user = "root",
        password = "123456",
        host = "127.0.0.1",
        port = 3306,
        database = "bdteste"
    )
except mariadb.Error as e:
    print(f"Error connection to MariaDB Platform:{e}")
    sys.exit(1)

# Get Cursor

RE = 10 # repeticao
BI = 500  # blocos de insert
BS = 500  # blocos de select
BU = 500  # blocos de update


def Insert():
    arquivo.write("###############################################################################")
    arquivo.write("\nTempo Blocos Insert em segundos:\n")
    print("\n###############################################################################")
    print("Tempo Blocos Insert em segundos:\n")
    vetor = []
    for r in range(RE):

        inicio = time.time()
        for b in range(BI):
            cur = conn.cursor()
            cur.execute('''INSERT INTO A(A1,A2,A3,A4,A5,A6) 
                          VALUES(1,1.2,'abcdefghijklmnopqrstuvxz','abcdefghijklmnopqrstuvxz','15:25:22','2021-05-11');'''
                        )
            conn.commit() 
        fim = time.time()
        tempo = fim - inicio
        vetor.append(tempo)                                     # Adiciona no final do vetor o valor tempo
        arquivo.write("\n%1.9f" % tempo)                        # Escreve os valores de tempo no arquivo
        print( "Media Bloco Insert", r,":%1.9f" % tempo,"s")

    Media = statistics.fmean(vetor)
    DesvioPadrao = statistics.stdev(vetor)
    arquivo.write("\n\nMedia        : %1.9f" % Media)           # Escreve a media no arquivo
    arquivo.write("\nDesvio Padrao: %1.9f" % DesvioPadrao)      # Escreve o desvio padrão no arquivo

    print("\nMedia        : %1.9f" % Media,"s")                 # Escreve a media no Terminal
    print("Desvio Padrao: %1.9f" % DesvioPadrao,"s")            # Escreve o desvio padrão no Terminal



def Select():
    arquivo.write("\n\n###############################################################################")
    arquivo.write("\nTempo Blocos Select em segundos:\n")
    print("\n###############################################################################")
    print("Tempo Blocos Select em segundos:\n")
    vetor = []
    c = 1
    for r in range(RE):

        inicio = time.time()
        for b in range(BS):
            cur = conn.cursor()
            cur.execute( "SELECT * from A where A0=%d" % c )
            c += 1
        fim = time.time()
        tempo = fim - inicio
        vetor.append(tempo)                                     # Adiciona no final do vetor o valor tempo
        arquivo.write("\n%1.9f" % tempo)                        # Escreve os valores de tempo no arquivo
        print( "Media Bloco Select", r,":%1.9f" % tempo,"s")  
    Media = statistics.fmean(vetor)
    DesvioPadrao = statistics.stdev(vetor)
    arquivo.write("\n\nMedia        : %1.9f" % Media)           # Escreve a media no arquivo
    arquivo.write("\nDesvio Padrao: %1.9f" % DesvioPadrao)      # Escreve o desvio padrão no arquivo

    print("\nMedia        : %1.9f" % Media,"s")                 # Escreve a media no Terminal
    print("Desvio Padrao: %1.9f" % DesvioPadrao,"s")            # Escreve o desvio padrão no Terminal


def Update():
    arquivo.write("\n\n###############################################################################")
    arquivo.write("\nTempo Blocos Update em segundos:\n")
    print("\n###############################################################################")
    print("Tempo Blocos Update em segundos:\n")
    vetor = []
    c = 1
    for r in range(RE):

        inicio = time.time()
        for b in range(BU):
            cur = conn.cursor()
            cur.execute( "UPDATE A SET A1=9, A2=2.222, A3='ABCDEFGHIJKLMNOPQRSTUVXZ', A4='ABCDEFGHIJKLMNOPQRSTUVXZ', A5= '16:25:22', A6='2031-05-11' where A0=%d" % c )
            conn.commit() 
            c += 1
        fim = time.time()
        tempo = fim - inicio
        vetor.append(tempo)                                     # Adiciona no final do vetor o valor tempo
        arquivo.write("\n%1.9f" % tempo)                        # Escreve os valores de tempo no arquivo
        print( "Media Bloco Update", r,":%1.9f" % tempo,"s") 
    Media = statistics.fmean(vetor)
    DesvioPadrao = statistics.stdev(vetor)
    arquivo.write("\n\nMedia        : %1.9f" % Media)           # Escreve a media no arquivo
    arquivo.write("\nDesvio Padrao: %1.9f" % DesvioPadrao)      # Escreve o desvio padrão no arquivo

    print("\nMedia        : %1.9f" % Media,"s")                 # Escreve a media no Terminal
    print("Desvio Padrao: %1.9f" % DesvioPadrao,"s")            # Escreve o desvio padrão no Terminal




# INICIO

cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS A;")  # Apaga a tabela A


cur.execute(
    '''CREATE TABLE A(
        A0  INT             NULL      AUTO_INCREMENT ,
        A1  INT             NULL                     ,
        A2  FLOAT           NULL                     ,
        A3  NVARCHAR(26)    NULL                     ,
        A4  VARCHAR(26)     NULL                     ,
        A5  TIME DEFAULT CURRENT_TIME NULL           ,
        A6  DATE DEFAULT CURRENT_DATE NULL           ,
        PRIMARY KEY (A0));
    '''
)

arquivo = open('DADOS/resumo.txt','w')  # Cria um arquivo chamado resumo.txt na pasta DADOS 
arquivo.write("###################################################################################################")
arquivo.write("\n***  RELATORIO DO PROGRAMA PARA MEDIR O TEMPO DE RESPOSTA DO BANCO DE DADOS MARIADB  ***\n") 
arquivo.write("\n Autor: Jose Adolfo de Castro Neto")
arquivo.write("\n Data : 18/08/2021")
arquivo.write("\n\n QUANTIDADE DE REPETIÇÕES PARA CADA BLOCO: %d" % RE)
arquivo.write("\n QUANTIDADE DE BLOCOS DE INSERT          : %d" % BI)
arquivo.write("\n QUANTIDADE DE BLOCOS DE SELECT          : %d" % BS)
arquivo.write("\n QUANTIDADE DE BLOCOS DE UPDATE          : %d" % BU)
arquivo.write("\n###################################################################################################\n\n")

print("\n###################################################################################################")
print("\n***  RELATORIO DO PROGRAMA PARA MEDIR O TEMPO DE RESPOSTA DO BANCO DE DADOS MARIADB  ***\n") 
print(" Autor: Jose Adolfo de Castro Neto")
print(" Data : 18/08/2021")
print("\n QUANTIDADE DE REPETIÇÕES PARA CADA BLOCO: %d" % RE)
print(" QUANTIDADE DE BLOCOS DE INSERT          : %d" % BI)
print(" QUANTIDADE DE BLOCOS DE SELECT          : %d" % BS)
print(" QUANTIDADE DE BLOCOS DE UPDATE          : %d" % BU)
print("###################################################################################################\n\n")

Insert()
Select()
Update()
arquivo.close()     # Fecha o arquivo
conn.close()        # Fecha a conexão com o banco de dados MariaDB