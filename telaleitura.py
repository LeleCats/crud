import csv
def abrir():
    i = 0 
    with open('joias.csv', newline='', encoding="utf-8", errors="ignore")as csvfile:
        leitor = csv.reader(csvfile, delimiter=',')
        for linha in leitor:
            print(f"## Joia {i}: {linha[2]}, {linha[1]}, {linha[3]}, Preço: R${linha[4]}")
            i = i+1 
            
