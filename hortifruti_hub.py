import json
import os
from datetime import datetime

ARQUIVOS = {'clientes': 'clientes.json',
            'produtos': 'produtos.json'
            }

# Talvez tenha que estar dentro da função(ou não)
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
                json.dump(dados[chave], f, ensure_ascii=false, indent=2)
        except Exception as e:
            print(f'Erro ao salvar {nome_arquivo}:{e}')


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
        cpf = (input('Digite o CPF(deve conter 11 dígitos): '))
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


#  ----Menu Principal-----

while True:
    print('==== Sistema de estoque - Hortifruti ==== ')
    print('[1]- Clientes ')
    print('[3]- Vendas')
    print('[4]- Relatórios')
    print('[0]- Sair')

    opcao = int(input('>'))

    if opcao == 1:
        menu_clientes(dados)
    elif opcao == 2:
        menu_produtos()
    elif opcao == 3:
        menu_vendas(dados)
    elif opcao == 4:
        menu_relatorios(dados)
    elif opcao == 0:
        print('Salvando dados')
        salvar_dados(dados)
        print('Dados salvos, programa encerrado')
    else:
        print('Opção inválida')
