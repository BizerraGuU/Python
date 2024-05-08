#Tentar: dar a opção na hora de cadastrar: endereço, email, telefone,
# tipo de restaurante (sushi, churrascaria, fast food);

#Desafio Master: criar uma opção de fazer busca de restaurantes,
# o usuario pode escolher o filtro pra achar o restaurante com base nas opções;

import os

restaurantes = [{'nome':'Restaurante Teste', 'categoria':'Teste_Teste', 'ativo':True}]

def exibir_nome_do_programa():
    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
''')

def voltar_menu_principal():
    '''esssa função retorna ao menu princial, chamando a função main após clicar em qualquer tecla'''
    input('Digite uma tecla para voltar ao menu principal: ')
    main()
def exibir_opcoes():
    '''essa função mostra ao usuário as opções que o programa oferece'''
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Alterar Estado do Restaurante')
    print('4. Sair\n')

def finaliza_app():
    '''essa função finaliza o app e exibe uma mensagem de finalizaçaõ'''
    exibir_subtitulo('App Encerrado')

def opcao_invalida():
    '''essa funçao alerta ao usuário que a opção que ele escolheu
    não é válida e permite que ele volta ao menu principal da aplicação'''
    print('Opção Inválida!\n')
    input('Digite um tecla para voltar ao menu principal: ')
    voltar_menu_principal()
    main()

def exibir_subtitulo(texto):
    '''essa função limpa a tela após a escolha de uma das opções,
    mostra o subitítulo da opção escolhida
    e coloca linhas feitas por * para melhorar a vizualização'''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''essa função cadastra os dados do novo restaurante:

    inputs:
    - nome do restaurante
    - categoria do restaurante

    outputs:
    - coloca os dados digitados no dicionário
    - mostra ao usuário o nome que foi cadastrado

    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_do_restaurante = input(f'Digite a categoria do restaurante "{nome_do_restaurante}": ')
    dados_do_restaurante = {'nome':nome_do_restaurante,'categoria':categoria_do_restaurante,'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante '{nome_do_restaurante}' foi cadastrado com sucesso!\n")

    voltar_menu_principal()

def listar_restaurantes():
    '''essa função lista o nome dos restaurantes,
    seguidos de sua categoria e se o mesmo está ativo ou não no cadastro
    ela printa na tela algo parecido com uma tabela para mostrar ao usuário os dados
    de uma maneira mais intuitiva
    '''

    exibir_subtitulo('Listando Restaurantes')

    print(f'{"Nome do Resturante".ljust(22)} | {"Categoria".ljust(20)} | Status')
    print('-------------------------------------------------------') #essa linha aqui é só firula pq eu queria deixar mais bonitinho
    for restaurante in restaurantes:
        exibir_nome_do_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {exibir_nome_do_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_menu_principal()

def alterar_estado_do_restaurante():
    '''essa função altera o estado do restaurante:
    se ele estiver desativado, é possivel ativar digitando o nome do restaurante
    e ativá-lo, fazendo a mesma coisa

    inputs:
    - pede o nome do restaurante que o usuario deseja alterar o estado (ativo, desativado)

    outputs:
    - dentro do laço for, o if verifica se o nome de algum item da lista é igual ao digitado
    caso sim, o programam verifica se ele esta ativo ou não, caso esteja ativo, o programa o desativa
    e avisa ao usuário o estado atual, e vice e versa.

    '''
    exibir_subtitulo('Alterando Estado do Restaurante')
    nome_para_alterar = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_econtrado = False

    for restaurante in restaurantes:
        if nome_para_alterar == restaurante['nome']:
            restaurante_econtrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O resturante {nome_para_alterar} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_para_alterar} foi desativado com sucesso!'
            print(mensagem)

    if not restaurante_econtrado:
        print('O restaurante não foi encontrado!')

    voltar_menu_principal()

def escolher_opcoes():

    '''essa função pede ao usuário que digite um número
    caso o numero seja correspondente a uma opção programada
    então o programa realiza alguma função, sendo que caso ele digite algo que não
    seja o que está definido, o programa realiza a função opcao_invalida() e retorna ao menu inicial'''

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()

        elif opcao_escolhida == 2:
            listar_restaurantes()

        elif opcao_escolhida == 3:
            alterar_estado_do_restaurante()

        elif opcao_escolhida == 4:
            print('Finalizando o Programa...')

        else:
            opcao_invalida() #esse else trata das opcoes numericas difente de 1, 2, 3 e 4.

    except:
        opcao_invalida()

def main():
    '''essa função main, é específica para que se retorne ao menu principal'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()
