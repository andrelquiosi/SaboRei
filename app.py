import os

restaurantes = [{'nome':'Lazis','categoria':'Hamburger','ativo':False},
                {'nome':'sushiTown','categoria':'Japonesa','ativo':True},
                {'nome':'Baruk','categoria':'Arabe','ativo':True}]

def exibir_nome_do_programa():
    print("""
    ████████████████████████████████████████
    █─▄▄▄▄██▀▄─██▄─▄─▀█─▄▄─█▄─▄▄▀█▄─▄▄─█▄─▄█
    █▄▄▄▄─██─▀─███─▄─▀█─██─██─▄─▄██─▄█▀██─██
    ▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▀
    """)

def exibir_opcoes():
        
    print('1. Cadastrar Restaurante')
    print('2. Listar restaurantes')
    print('3. Alterar status do Restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Encerrando programa')

def opcao_invalida():
    input('Opção inválida!\nPressione uma tecla para voltar!')
    main()
    
def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastrar Restaurante')

    nome_do_restaurante = input('Digite o nome do restaurante: ')
    categoria_do_restaurante = input(f'Informe a categoria do restaurante {nome_do_restaurante}: ')
    
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria_do_restaurante,'ativo':False}
    restaurantes.append(dados_do_restaurante)
    
    print(f'O restaurante {nome_do_restaurante} foi cadastrado!')
    
    voltar_ao_menu_principal()
    
def listar_restaurantes():
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
    exibir_subtitulo('Alternando Status do restaurante!')
    
    nome_do_restaurante = input('Informe o nome do restaurante que deseja alterar o status: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        
        if nome_do_restaurante == restaurante['nome']:           
            restaurante_encontrado =True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_do_restaurante} foi ativado com sucesso.' if restaurante['ativo'] else f'O restaurante {nome_do_restaurante} doi desativado com sucesso.'
            print(mensagem)
            
    if not restaurante_encontrado:
        print(f'O restaurante {nome_do_restaurante} não foi encontrado!')
        
    voltar_ao_menu_principal()
         
def voltar_ao_menu_principal():
        input('\nPressione uma tecla para voltar!')
        main()

def escolher_opcoes():
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
    os.system('cls' if os.name == 'nt' else 'clear')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    
    print()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()
    
if __name__ == '__main__':
    main()