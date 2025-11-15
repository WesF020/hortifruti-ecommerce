import json
import os
from datetime import datetime

ARQUIVOS = {'clientes': 'clientes.json',
            'produtos': 'produtos.json'
            }


dados = {'clientes': [], 'produtos': []}

# ----- Carregar e Salvar Dados-----


def carregar_dados(dados):

    for chave, nome_arquivo in ARQUIVOS.items():
        if os.path.exists(nome_arquivo):
            try:
                with open(nome_arquivo, 'r', encoding='utf-8') as f:
                    dados[chave] = json.load(f)
            except Exception:
                print(
                    f'AVISO: Não foi possível ler o arquivo {nome_arquivo}. Criando listas vazias.')
                dados[chave] = []
        else:
            dados[chave] = []
    return dados


def salvar_dados(dados):
    for chave, nome_arquivo in ARQUIVOS.items():
        try:
            with open(nome_arquivo, 'w', encoding='utf-8') as f:
                json.dump(dados[chave], f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f'Erro ao salvar {nome_arquivo}:{e}')


carregar_dados(dados)  # carregar os dados ao iniciar o programa


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

def menu_clientes(dados):
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
            cadastrar_clientes(dados)
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


def cadastrar_clientes(dados):

    print('----Cadastrar Clientes----')
    nome = input('Digite o nome: ').strip()

    while True:
        cpf = (input('Digite o CPF(deve conter 11 dígitos): ')).strip()
        if not cpf.isdigit() or len(cpf) != 11:
            print('CPF inválido, digite 11 números.')
            continue
        if any(c['cpf'] == cpf for c in dados['clientes']):
            print('Já existe um cliente cadastrado com este CPF')
            return
        break

    idade = int(input('Digite a idade: '))

    if idade < 18:
        print('Somente maiores de idade podem ser cadastrados.')
        return

    dados['clientes'].append({'nome': nome, 'cpf': cpf, 'idade': idade})

    salvar_dados(dados)
    print('Cliente cadstrado com sucesso!')


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


def cadastro_produtos(dados):

    print("----Cadastrar Produto----")
    novo_produto = input("Digite o nome do novo produto: ").strip()

    while True:
        id_do_produto = input("Insira o id do produto (Deve ter até 5 números):  ").strip()
        if not id_do_produto.isdigit() or len(id_do_produto) != 5:
            print("O ID que você criou está invalido (Deve ter ao menos 5 números)")
            continue
        if any(p['id'] == id_do_produto for p in dados['produtos']):
            print('Este ID já está em uso por outro produto')
            continue

        print("ID válido e disponível!")
        break
    
    while True:
        try:
            preco_do_produto = float(input("Digite o preço deste produto:  "))
            if preco_do_produto <= 0:
                print("Erro! Insira um preço maior que zero.")
                continue
            break
        except ValueError:
            print("O valor inserido não é um número inteiro.")
    
    while True:
        try:
            quantidade_estoque = int(input("Digite a quantidade deste item no estoque:  "))
            if quantidade_estoque < 10:
                print("Erro! A quantidade de itens deve estar acima ou igual a 10.")
                continue
            break
        except ValueError:
            print("O valor inserido não é um número inteiro.")

    novo_produto_dict = {
    'id': id_do_produto,
    'nome': novo_produto,
    'preco': preco_do_produto,
    'quantidade': quantidade_estoque
}
        
    dados['produtos'].append(novo_produto_dict)

    salvar_dados(dados)

    print(f"\n Produto cadastrado com sucesso!")
    print(f"   Nome: {novo_produto}")
    print(f"   ID: {id_do_produto}")
    print(f"   Preço: R$ {preco_do_produto}")
    print(f"   Estoque: {quantidade_estoque} unidades")

        
def atualizar_produto(dados):
    
    print("----Atualizar Produto-----")

    if not dados['produtos']:
        print("Nenhum produto cadastrado para atualizar.")
        return
    
    print("\nProdutos cadastrados:\n")
    for produto in dados['produtos']:
        print(f"ID: {produto['id']} | Nome: {produto['nome']} | Preço: R$ {produto['preco']} | Estoque: {produto['quantidade']}")

        busca_por_id = input("\nDigite o ID do produto que você quer atualizar:  ").strip()
        
        produto_encontrado = None
        for produto in dados['produtos']:
            if produto ['id'] == busca_por_id:
                produto_encontrado = produto
                break
        
        if not produto_encontrado:
            print("Erro! Produto não encontrado.")
            return
        
        print(f"\nProduto encontrado: {produto_encontrado['nome']}")

        while True:
            print("\nO que você deseja atualizar?\n")
            print("1 - Nome")
            print("2 - Preço")
            print("3 - Quantidade em estoque")
            print("4 - Tudo (nome, preço e quantidade)")
            print("0 - Cancelar")

            opcao = input("Escolha uma opção:  ").strip()

            if opcao == "1":
                novo_nome = input(f"Novo nome (atual: {produto_encontrado['nome']}): ").strip()
                if novo_nome:
                    produto_encontrado['nome'] = novo_nome
                    print("Sucesso! Nome atualizado.")

            elif opcao == "2":
                while True:
                    try:
                        novo_preco = float(input(f"Novo preço (atual: R$ {produto_encontrado['preco']}): R$ "))

                        if novo_preco <= 0:
                            print("Erro! O preço deve ser maior que zero!")
                            continue
                        produto_encontrado['preco'] = novo_preco
                        break

                    except ValueError:
                        print("Erro! Digite um número válido!")

            elif opcao == "3":
                while True:
                    try:
                        nova_quantidade = int(input(f"Nova quantidade (atual: {produto_encontrado['quantidade']}):   "))

                        if nova_quantidade < 10:
                            print("Erro! A quantidade deve ser maior ou igual a 10.")
                            continue
                        produto_encontrado['quantidade'] = nova_quantidade
                        print("Sucesso! Quantidade atualizada.")
                        break
                    except ValueError:
                        print("Erro! Insira um valor válido!")

            elif opcao == "4":

                novo_nome = input(f"Novo nome(atual: {produto_encontrado['nome']}):   ").strip()
                if novo_nome:
                    produto_encontrado['nome'] = novo_nome

                while True:
                    try:
                        novo_preco = float(input(f"Novo preço (atual: R$ {produto_encontrado['preco']}): R$ "))
                        if novo_preco <= 0:
                            print("Erro! O preço deve ser maior que zero!")
                            continue
                        produto_encontrado['preco'] = novo_preco
                        break
                    except ValueError:
                        print("Erro! Digite um valor válido!")
            
                while True:
                    try:
                        nova_quantidade = int(input(f"Nova quantidade (atual: {produto_encontrado['quantidade']}): "))
                        if nova_quantidade < 10:
                            print("Erro! A quantidade deve ser maior ou igual a 10!")
                            continue
                        produto_encontrado['quantidade'] = nova_quantidade
                        break
                    except ValueError:
                        print("Erro! Digite um número inteiro válido!")
            
                print("Sucesso! Todos os dados atualizados!")
        
            elif opcao == '0':
                print("Operação cancelada.")
                return
        
            else:
                print("Erro! Opção inválida!")
                continue
        
            continuar = input("\nDeseja fazer mais alterações neste produto? (s/n): ").strip().lower()
            if continuar != 's':
                break
    
        print(f"\n Produto atualizado com sucesso!")
        print(f"   Nome: {produto_encontrado['nome']}")
        print(f"   Preço: R$ {produto_encontrado['preco']:.2f}")
        print(f"   Estoque: {produto_encontrado['quantidade']}")

#  ----Menu Principal-----

while True:
    print('==== Sistema de estoque - Hortifruti ==== ')
    print('[1]- Clientes ')
    print('[2]- produtos')
    print('[3]- Vendas')
    print('[4]- Relatórios')
    print('[0]- Sair')

    opcao = int(input('>'))

    if opcao == 1:
        menu_clientes(dados)
    elif opcao == 2:
        menu_produtos(dados)
    elif opcao == 3:
        menu_vendas(dados)
    elif opcao == 4:
        menu_relatorios(dados)
    elif opcao == 0:
        print('Salvando dados')
        salvar_dados(dados)
        print('Dados salvos, programa encerrado')
        break
    else:
        print('Opção inválida')

