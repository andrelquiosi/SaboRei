import os

restaurantes = [{'nome':'Lazis','categoria':'Hamburger','ativo':False},
                {'nome':'sushiTown','categoria':'Japonesa','ativo':True},
                {'nome':'Baruk','categoria':'Arabe','ativo':True}]

def exibir_nome_do_programa():
    """
    Essa função exibe o nome do aplicativo
    """
    print("""
    ████████████████████████████████████████
    █─▄▄▄▄██▀▄─██▄─▄─▀█─▄▄─█▄─▄▄▀█▄─▄▄─█▄─▄█
    █▄▄▄▄─██─▀─███─▄─▀█─██─██─▄─▄██─▄█▀██─██
    ▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▀
    """)

def exibir_opcoes():
    """
    Essa função exibi as opções
    """
        
    print('1. Cadastrar Restaurante')
    print('2. Listar restaurantes')
    print('3. Alterar status do Restaurante')
    print('4. Sair\n')

def finalizar_app():
    """
    Essa função encerra o programa
    """
    exibir_subtitulo('Encerrando programa')

def opcao_invalida():
    """
    Essa função exibe uma mensagem caso uma entrada inválida seja realizada, e volta ao menu
    """
    input('Opção inválida!\nPressione uma tecla para voltar!')
    main()

def cadastrar_novo_restaurante():
    """
    Essa função realiza o cadastro do restaurante
    
    Inputs:
        - Nome do restaurante
        - Categoria do restaurante
    
    Outputs:
        - Adiciona um novo restaurante a lista de restaurantes
    """
    exibir_subtitulo('Cadastrar Restaurante')

    nome_do_restaurante = input('Digite o nome do restaurante: ')
    categoria_do_restaurante = input(f'Informe a categoria do restaurante {nome_do_restaurante}: ')
    
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria_do_restaurante,'ativo':False}
    restaurantes.append(dados_do_restaurante)
    
    print(f'O restaurante {nome_do_restaurante} foi cadastrado!')
    
    voltar_ao_menu_principal()

def listar_restaurantes():
    """Essa função exibe a lista dos restaurantes cadastrados no dicionário.
    Caso tenha algum erro na posição do dicionário, exibe uma mensagem e após volta para o menu principal
    """
    exibir_subtitulo('Listar restaurantes')
    
    print(f'{'NOME DO RESTAURANTE'.ljust(22)} | {'CATEGORIA'.ljust(20)} | {'STATUS'}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        if restaurante:
            print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo}')
        else:
            print(f'- !Restaurante não disponível!')

    voltar_ao_menu_principal()

def alternar_status_restaurante():
    """Essa função altera o status do restaurante de 'True' ou 'False'
    
    Inputs:
        - Selecionar o restaurante informando o Nome
        
    Outputs:
        - Exibe a mensagem caso não encontre o restaurante
        - Exibe a mensagem caso o restaurante alterou o status com sucesso
    """
    exibir_subtitulo('Alternando Status do restaurante!')
    
    nome_do_restaurante = input('Informe o nome do restaurante que deseja alterar o status: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        
        if nome_do_restaurante == restaurante['nome']:           
            restaurante_encontrado =True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_do_restaurante} foi ativado com sucesso.' if restaurante['ativo'] else f'O restaurante {nome_do_restaurante} foi desativado com sucesso.'
            print(mensagem)
            
    if not restaurante_encontrado:
        print(f'O restaurante {nome_do_restaurante} não foi encontrado!')
        
    voltar_ao_menu_principal()
def voltar_ao_menu_principal():
    """Essa função serve para voltar ao menu principal
    
    Inputs:
        - Ao pressionar o enter, volta para o menu principal
    """
    input('\nPressione uma tecla para voltar!')
    main()

def escolher_opcoes():
    """Essa função recebe a opção escolhida pelo usuário
    
    Inputs:
        - Usuário fornece o numero da opção escolhida
        
    Outputs:
        - O usuário é direcionado para função escolhida
    """

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        
        match opcao_escolhida:
            case  1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alternar_status_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()
    
def exibir_subtitulo(texto): 
    """Essa função limpa a tela e exibe o subtitulo informado formatado

    Inputs:
        - É informado o texto para ser exibido
        
    Outputs:
        - o texto informado é exibido formatado
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    
    print()

def main():
    """Essa função inicia o programa, limpando a tela, exibindo o nome do programa, exibindo as opções e disponibilizando uma para ser escolhida.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()
    
if __name__ == '__main__':
    
    main()