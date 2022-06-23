import operacoes
import this
this.opcao = -1

def menu():
    print('\nEscolha uma das opções abaixo: \n\n' +
          '1. Cadastrar\n'                        +
          '2. Consultar\n'                        +
          '0.Sair\n')
    this.opcao = int(input())

def operacao():
        while(this.opcao != 0):
            menu()
            if this.opcao == 1:
                print('Informe seu nome: ')
                nome = input()
                print('Informe seu telefone: ')
                telefone = input()
                print ('Informe seu endereço: ')
                endereco = input()
                print ('Informe sua data de nascimento: ')
                dataDeNascimento = input()
                #Chamar o metodo inserir
                operacoes.inserir(nome, telefone, endereco, dataDeNascimento)
            elif this.opcao == 2:
                operacoes.consultar()
            else:
                print("Opção escolhida não é valido , porfavor tente novamente e escolha uma válida!")



