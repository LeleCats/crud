# Ler a base de dados (arquivo)
# Utilizar a classe para armazenar os dados
# Recebr o índice da camiseta a ser atualizada
# Atualizar os dados na classe
# Reescrever o arquivo
def abrir():    
    import csv
    from joias import Joias
    joias = []

    #ler arquivo de produtos
    with open('joias.csv', newline='', encoding="utf-8", errors="ignore") as csvleitura:
        linha = csv.reader(csvleitura, delimiter=',')
        for coluna in linha:
            #armazenar os produtos numa lista
            novaJoia = Joias(coluna[0], coluna [1], coluna [2], coluna [3], coluna [4], coluna [5])
            joias.append(novaJoia)

    def altera_dados():
        indice = int(input("Digite o índice do produto a ser alterado:"))
        print("Digite apenas o atributo que você deseja alterar. Caso queira manter o valor antigo, apenas aperte ENTER")
        cor = input("Cor: ")
        material = input("material: ")
        tipo = input("tipo: ")
        quilates = input("quilates: ")
        preco = input("preco: ")
        pedra_preciosa = input("pedra_preciosa: ")
        
        if cor != "":
            joias[indice].cor = cor
        if material != "":
            joias[indice].material = material
        if tipo != "":
            joias[indice].tipo = tipo
        if quilates != "":
            joias[indice].quilates = quilates
        if preco != "":
            joias[indice].preco = preco
        if pedra_preciosa != "":
            joias[indice].pedra_preciosa = pedra_preciosa

    def escreve_arquivo():
        with open('joias.csv', 'w', newline='', encoding='utf-8', errors='ignore') as csvEscrita:
            escrever = csv.writer(csvEscrita)
            for j in joias:
                escrever.writerow([j.cor, j.material, j.tipo, j.quilates, j.preco, j.pedra_preciosa])
            print(f"Arquivo atualizado! joias atualizadas com sucesso!")


    altera_dados()
    escreve_arquivo()