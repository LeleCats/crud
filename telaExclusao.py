def abrir():    
    import csv
    linhas = []
    indice = int(input("Digite o numero das joias a ser excluido:"))

    #ler arquivo de produtos
    with open('joias.csv', newline='', encoding="utf-8", errors="ignore") as csvleitura:
        leitor = csv.reader(csvleitura, delimiter=',')
        for linha in leitor:
            #armazenar os produtos numa lista
            linhas.append(linha)

    #print(linhas)

    #remove o "indice" da lista
    linhas.pop(indice)  
    #print(linhas)

    #reescrever o arquivo com a lista atualizada
    with open('joias.csv','w', newline='', encoding="utf-8", errors="ignore") as csvEscrita:
        escrever = csv.writer(csvEscrita)
        escrever.writerows(linhas)
        print(f"Arquivo atualizado! joia {indice} excluída com sucesso!!")