import telaJoias
import telaleitura
import telaExclusao
import telaAtualizar
while(True):
    print("### MENU PRINCIPAL ###")
    print("1 - Cadastrar novo joias")
    print("2 - Ver estoque de joias")
    print("3 - Excluir o joias")
    print("4 - Atualizar o joias")
    opcao = int(input("Digite a opção desejada:"))
    if opcao == 1:
        telaJoias.abrir()
    elif opcao == 2:
        telaleitura.abrir()
    elif opcao == 3:
        telaExclusao.abrir()
    elif opcao == 4:
        telaAtualizar.abrir()

        print("Opção inválida")
            