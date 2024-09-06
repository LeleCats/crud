import csv

from joias import Joias

def escreveArquivo(cor, material, tipo, quilates, preco, pedra_preciosa):
    with open('joias.csv', 'a', newline='') as csvfile:
        escreve_Joias = csv.writer(csvfile, delimiter=',')
        escreve_Joias.writerow([cor, material, tipo, quilates, preco, pedra_preciosa])
        print("### JOIA ", joias, "adicionada com sucesso! ###")

joias = []

def abrir():
    print("### BEM VINDO A TELA DE CADASTRO DE JOIAS ###")
    print("\nNOVA JOIA:")
    cor = input("Escolha a cor: \n")
    material = input("qual e o material da joia: \n")
    tipo = input("qual e o tipo da joia: \n")
    quilates = int(input("quantos quilates tem a joia: \n"))
    preco = float(input("qual o valor: "))
    pedra_preciosa = input("escolha a pedra preciosa: \n")
    novaJoia = Joias(cor, material, tipo, quilates, preco, pedra_preciosa)
    
    escreveArquivo(cor, material, tipo, quilates, preco, pedra_preciosa)
    joias.append(novaJoia)
    # TESTE PARA VER SE O SISTEMA FUNCIONA:
