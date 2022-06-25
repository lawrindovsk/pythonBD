import operacoes
import this
this.opcao = -1
this.codigo = 0
this.campo = ""

def menu():
    print('\nEscolha uma das opções abaixo: \n\n' +
          '1. Cadastrar\n'                        +
          '2. Consultar\n'                        +
          '3. Atualizar Nome\n'                   +
          '4. Atualizar Telefone\n'               +
          '5. Atualizar Endereço\n'               +
          '6. Atualizar Data de Nascimento\n'     +
          '7. Excluir\n'                          +
          '0.Sair\n')
    this.opcao = int(input())

def operacao():
        while(this.opcao != 0):
            menu()
            if this.opcao == 0:
                print('Obrigado !')
            elif this.opcao == 1:
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
            elif this.opcao == 3:
                print("Informe o código que deseja atualizar")
                this.codigo = int(input())
                print("Informe o novo Nome: ")
                this.nome = input()
                operacoes.atualizar(this.codigo, 'nome', this.nome)
            elif this.opcao == 4:
                print("Informe o código que deseja atualizar o telefone ")
                this.codigo = int(input())
                print("Informe o novo número de telefone: ")
                this.telefone = input()
                operacoes.atualizar(this.codigo, 'telefone', this.telefone)
            elif this.opcao == 5:
                print("Informe o código que deseja atualizar o endereço/email: ")
                this.codigo = int(input())
                print("Informe o novo endereço/email que deseja atualizar: ")
                this.endereco = input()
                operacoes.atualizar(this.codigo, 'endereco', this.endereco)
            elif this.opcao == 6:
                print("Informe o código que deseja atualizar a Data de Nascimento: ")
                this.codigo = int(input())
                print("Informe a nova Data que deseja atualizar: ")
                this.datadeNascimento = input()
                operacoes.atualizar(this.codigo, 'datadeNascimento', operacoes.tratarData(this.datadeNascimento))
            elif this.opcao == 7:
                print("Informe o codigo que deseje excluir: ")
                this.codigo = int(input())
                operacoes.excluir(this.codigo)
            else:
                print("Opção digitada inválida , porfavor tente novamente escolha a opção correta!")



