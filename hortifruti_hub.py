#   -----Menu dos Produtos-----

def menu_produtos():
    while True:
        print('=== Menu Produtos ===')
        print('[1] - Cadastrar produto')
        print('[2] - Atualizar produto')
        print('[3] - Excluir produto')
        print('[4] - Listar todos os produtos')
        print('[5] - Relatório: produtos em estoque')
        print('[0] - Voltar ao menu principal')
        op = input('> ').strip()
        if op == '1':
            cadastrar_produto()
        elif op == '2':
            atualizar_produto()
        elif op == '3':
            excluir_produto()
        elif op == '4':
            listar_produtos()
        elif op == '5':
            relatorio_produtos()
        elif op == '0':
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

    opcao = input('>').strip
    if opcao == '1':
        menu_clientes()  # Função que abre o menu de clientes
    elif opcao == '2':
        menu_produtos()  # função que abre o menu de produtos (Mostrado em cima)
    elif opcao == '3':
        menu_vendas  # função que abre o menu de vendas
    elif opcao == '4':
        menu_relatorios     # função que abre o menu de relatórios
    elif opcao == '5':
        print('Salvando dados...')
        salvar_dados()  # função responsável por salvar os dados no arquivo .JSON
        print('Dados salvos, programa encerrado.')
        break
    else:
        print('Opção inválida.')
