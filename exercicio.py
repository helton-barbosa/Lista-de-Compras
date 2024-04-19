from os import system

lista_de_compras = []
ativo = True
escolha = 0


def limpar_tela():
    system('cls')


def pausar():
    system('pause')


def listar():
    if len(lista_de_compras) == 0:
        print('\nA lista está vazia!\n')
    else:
        print()
        for number, itens in enumerate(lista_de_compras):
            print(f'{number+1} - {itens}')
        print()


def adicionar():
    item = input('\nAdicionar item à lista: ').capitalize()
    lista_de_compras.append(item)


def remover(item):
    if item in lista_de_compras:
        lista_de_compras.remove(item)
        print(f'O item "{item}" foi removido da lista\n')
        pausar()
    else:
        print(f'O item "{item}" não existe na lista\n')
        pausar()


while ativo:
    limpar_tela()
    print('LISTA DE COMPRAS')
    listar()
    print('1.:: Adicionar 2.:: Remover 0.:: Sair')

    escolha = int(input('\n\nEscolha uma opção: '))

    if escolha == 1:
        adicionar()
    elif escolha == 2:
        item = input('\nRemover: ')
        remover(item.capitalize())
    elif escolha == 0:
        print('\nSaindo do programa!')
        ativo = False
    else:
        print('Opção inválida!!!')
        pausar()
