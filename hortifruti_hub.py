# -----Menu Relatórios-----

def menu_relatorios():
    while True:
        print('[1]- Relatório dos Clientes')
        print('[2]- Relatório dos Produtos')
        print('[3]- Relatório das vendas')
        print('[0]- Vlotar ao menu principal')

        opcao = int(input('>'))

        if opcao == 1:
            lista_de_clientes()
        elif opcao == 2:
            relatorio_produtos()
        elif opcao == 3:
            relatorio_vendas()
        elif opcao == 0:
            return
        else:
            print('Opção inválida.')


# -----Menu Vendas-----

def menu_vendas():
    while True:
        print('[1]- Registrar venda')
        print('[2]- Buscar venda por produto')
        print('[3]- Listar todas as vendas')
        print('[4]- Relatório das vendas')
        print('[0]- Voltar ao menu principal')

        opcao = int(input('>'))

        if opcao == 1:
            registrar_venda()
        elif opcao == 2:
            buscar_venda_por_produto()
        elif opcao == 3:
            listar_vendas()
        elif opcao == 4:
            relatorio_vendas()
        elif opcao == 0:
            return
        else:
            print('Opção inválida.')


# -----Menu Clientes-----

def menu_clientes():
    while True:
        print('===Menu Clientes===')
        print('[1]- Cadastrar cliente')
        print('[2]- Buscar cliente por CPF')
        print('[3]- Atualizar cliente')
        print('[4]- Excluir cliente')
        print('[5]- Lista de clientes')
        print('[0]- Voltar ao menu principal')

        opcao = int(input('>'))

        if opcao == 1:
            cadastrar_clientes()
        elif opcao == 2:
            buscar_clientecpf()
        elif opcao == 3:
            atualizar_cliente()
        elif opcao == 4:
            excluir_cliente()
        elif opcao == 5:
            lista_de_clientes()
        elif opcao == 0:
            return
        else:
            print('Opção inválida')


#   -----Menu Produtos-----

def menu_produtos():
    while True:
        print('=== Menu Produtos ===')
        print('[1] - Cadastrar produto')
        print('[2] - Atualizar produto')
        print('[3] - Excluir produto')
        print('[4] - Listar todos os produtos')
        print('[5] - Relatório: produtos em estoque')
        print('[0] - Voltar ao menu principal')
        opcao = int(input('> '))
        if opcao == 1:
            cadastrar_produto()
        elif opcao == 2:
            atualizar_produto()
        elif opcao == 3:
            excluir_produto()
        elif opcao == 4:
            listar_produtos()
        elif opcao == 5:
            relatorio_produtos()
        elif opcao == 0:
            return
        else:
            print('Opção inválida.')


#  ----Menu Principal-----

while True:
    print('==== Sistema de estoque - Hortifruti ==== ')
    print('[1]- Clientes ')
    print('[2]- Produtos ')
    print('[3]- Vendas')
    print('[4]- Relatórios')
    print('[0]- Sair')

    opcao = int(input('>'))

    if opcao == 1:
        menu_clientes()  # Função que abre o menu de clientes
    elif opcao == 2:
        menu_produtos()  # função que abre o menu de produtos
    elif opcao == 3:
        menu_vendas()  # função que abre o menu de vendas
    elif opcao == 4:
        menu_relatorios()     # função que abre o menu de relatórios
    elif opcao == 0:
        print('Salvando dados...')
        salvar_dados()  # função responsável por salvar os dados no arquivo .JSON
        print('Dados salvos, programa encerrado.')
        break
    else:
        print('Opção inválida.')
