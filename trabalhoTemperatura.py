clima = []
climas = {}
temperaturaMin = {}
datas2006Mais = []
escolha = 6
mesInicialVf = True
mesFinalVf = True
anoInicialVf = True
anoFinalVf = True

import matplotlib.pyplot as plt
cabecalho = ["DATA", "PRECIPITACAO", "TEMP MAX", "TEMP MIN", "HORAS INSOL", "TEMP MEDIA", "UMIDADE RELATIVA", "VELOCIDADE VENTO"]
mesesDoAno = ["Janeiro","Fevereiro","Marco","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]

def leituraArquivo():#faz a leitura do arquivo e adiciona em uma lista
    umaVezz = 0
    arq = open("Anexo_Arquivo_Dados_Projeto_Logica_e_programacao_de_computadores.csv", "r")#recebe o arquivo
    for linha in arq:
            valor = linha.split(',')#separa as informações que tiverem ','

            clima.append(valor)#adiciona os valores na lista

            if umaVezz == 0:
                del clima[0]
                umaVezz = 1
                continue

            data = valor[0].split('/')#recebe as datas e divide elas

            if int(data[2]) >= 2006 and int(data[2]) <= 2016:#sempre que o ano for maior ou igual a 2006 e menor ou igual a 2016 ele é adicionado na lista 
                datas2006Mais.append(valor)
    arq.close() 
        

            

def criandoDicionario():#passa o mes em extenso + ano para criar as chaves
    for num in range(0, len(clima)):#faz um for de acordo com o tamanho da lista
        dataFormatada = str(clima[num][0]).split('/')#converte em String as datas e as divide 

        mes = int(dataFormatada[1])#pega o mes e converte em int
        ano = int(dataFormatada[2])#pega o ano e converte em int

        climas[mesesDoAno[mes-1] + str(ano)] = {"Prep": 0}#cria um dicionario para a precipitação

        if ano >= 2006 and ano <= 2016:
            temperaturaMin[mesesDoAno[mes-1]+ str(ano)] = {"TempMedMin":0}#cria outro dicionario para os anos de 2006 a 2016

def adcMaiorPrep():#adiciona a maior precipitacao de cada mes nas chaves correspondentes 
    mantem = 0
    maior = 0
    for ano in range(1961, 2017):#gira todos os anos 

        for mes in range (1, 13):#gira todos os meses

            for num in range(mantem, len(clima)):#gira toda lista
                dataFormatada = str(clima[num][0]).split('/')#divide a data

                mes2 = int(dataFormatada[1])#converte em int o mes
                ano2 = int(dataFormatada[2])#converte em int o ano
                
                if ano == ano2 and mes == mes2:#se o ano do for for igual ao ano que foi puxado da lista dá verdadeiro, mesmo ocorre com mes
                    if maior < float(clima[num][1]):#verifica se a precipitação é maior que o valor anterior
                        maior = float(clima[num][1])#se for maior que o atual ele é substituido
                        climas[mesesDoAno[mes-1] + str(ano)]["Prep"] = maior#adiciona o maior valor no dicionario, cria a chave e permite navegar no dicionario -> mesesDoAno[mes-1] + str(ano) 
                else:
                    maior = 0
                    mantem = num#para não zerar o FOR, ele pega o ultimo numero do giro para não zerar o loop, e continuar do numero que parou
                    break
def mostraMesEanoMaisChuvoso():#mostra o mes|ano mais chuvoso
    maior = 0

    for num in climas:
        if maior < climas[num]["Prep"]:
            maior = climas[num]["Prep"]
            chave = num
    print("Ano|mes com maior precipitação de chuva ",chave," - ",maior)
            


def temperaturaMediaMinima():#calcula a temperatura media minima de cada mes
    mantem = 0
    media = 0
    cont = 0
    for ano in range(2006, 2017):
        mantem = 0
        media = 0
        cont = 0
        for ano in range(2006, 2017):
            for mes in range (1, 13):
                 for num in range(mantem, len(datas2006Mais)):
                    dataFormatada = str(datas2006Mais[num][0]).split('/')

                    mes2 = int(dataFormatada[1])
                    ano2 = int(dataFormatada[2])

                    if ano == ano2 and mes == mes2:
                        media = media + float(datas2006Mais[num][3])
                        cont += 1
                                
                    else:        
                        if media > 0:
                            media = media / cont
                            if ano == 2016 and mes == 8:
                                mes -= 1
                            media = round(media,2)
                            temperaturaMin[mesesDoAno[mes-1]+ str(ano)]["TempMedMin"] = media          
                        mantem = num     
                        cont = 0
                        media = 0
                        break 
def exibePrepEtempMediaMin():#exibe a maior precipitação do mes|ano
    for num in climas:
        print(f"{num}, Maior Precipitacao ,({climas[num]["Prep"]}), Temperatura media Minima de cada mes ,({climas[num]["TempMedMin"]}) Graus")
        
   
    
print("iNFORME O PERIODO QUE DESEJA VER AS INFORMAÇÕES, MES INICIAL E MES FINAL, ANO INICIAL E ANO FINAL")

while escolha >= 6:
    escolha = int(input("Digite o que deseja ver (1) Ver todos os dados, (2) Apenas precipitacao,"+
                    "(3) Apenas temperatura, (4) Apenas umidade e vento (5) escolher dados entre 2006 e 2016-> "))
   
if escolha != 5:
    
    while mesInicialVf:
        mesInicial = int(input("Digite o mes inicial -> "))
        if mesInicial >= 1 and mesInicial <= 12:
            mesInicialVf = False
    while mesFinalVf:
        mesFinal = int(input("Digite o mes final -> "))
        if mesFinal >= 1 and mesFinal <= 12:  
            mesFinalVf = False
    while anoInicialVf:
        anoInicial = int(input("Digite o ano inicial -> "))
        if anoInicial >= 1961 and anoInicial <= 2016:
            anoInicialVf = False
    while anoFinalVf:
        anoFinal = int(input("Digite o ano final -> "))
        if anoFinal >= 1961 and anoFinal <= 2016:
            anoFinalVf = False


leituraArquivo()
criandoDicionario()
adcMaiorPrep()
temperaturaMediaMinima()

match escolha:
    case 1:#exibe todos os dados 
        for num in range(0, len(clima)):    
            for coluna in range(0, len(clima[0])):
                print(cabecalho[coluna], clima[num][coluna]," | ", end=" ")
        
                             
    case 2:#exibe apenas a precipitação 
        for num in range(0, len(clima)):
            dataFormatada = str(clima[num][0])
            
            mes =  (int(dataFormatada.split('/')[1]))
            ano =  (int(dataFormatada.split('/')[2]))
            
            if (mes >= mesInicial and mes <= mesFinal) and (ano >= anoInicial and ano <= anoFinal):
                print(cabecalho[0],"- ", clima[num][0],"  |  ", cabecalho[1],"- ", clima[num][1])
        
                 
    case 3:#exibe as temperaturas
        for num in range(0, len(clima)):
            dataFormatada = str(clima[num][0])
            
            mes =  (int(dataFormatada.split('/')[1]))
            ano =  (int(dataFormatada.split('/')[2]))
            
            if (mes >= mesInicial and mes <= mesFinal) and (ano >= anoInicial and ano <= anoFinal):
                print(cabecalho[0],"- ", clima[num][0],"  |  ", cabecalho[2],"- ", clima[num][2],"  |  ",cabecalho[3],"- ", clima[num][3])
       
    case 4:#exibe umidade e vento
        for num in range(0, len(clima)):
            dataFormatada = str(clima[num][0])
            
            mes =  (int(dataFormatada.split('/')[1]))
            ano =  (int(dataFormatada.split('/')[2]))
            
            if (mes >= mesInicial and mes <= mesFinal) and (ano >= anoInicial and ano <= anoFinal):
                print(cabecalho[0],"- ", clima[num][0],"  |  ", cabecalho[6],"- ", clima[num][6],"  |  ",cabecalho[7],"- ", clima[num][7])
    
    case 5:#exibe os anos de 2006 a 2016, apenas o mes que o usuario escolher
       mesInicial = True
       while mesInicial:
        mes = int(input("Informe o mes que deseja ver a temperatura minima de cada mes, lembrando que é de 2006 até 2016 os anos que serão considerados - > "))
        if mes >= 1 and mes <= 12:
            for ano in range(2006, 2017):
                if  ano == 2016 and mes >= 8:
                    print()
                else:
                    print(mesesDoAno[mes-1]+ str(ano), temperaturaMin[mesesDoAno[mes-1]+ str(ano)])
                    plt.bar(mesesDoAno[mes-1]+ str(ano), temperaturaMin[mesesDoAno[mes-1]+ str(ano)]["TempMedMin"])
            mesInicial = False
            plt.xlabel("Mes de cada ano")
            plt.ylabel("Temperatura media minima")
            plt.show()
                
