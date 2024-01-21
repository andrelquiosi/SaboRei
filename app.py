import os

restaurantes = ['Lazis','sushiTown']

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
    print('3. Ativar Reustaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Encerrando programa')

def opcao_invalida():
    input('Opção inválida!\nPressione uma tecla para voltar!')
    main()
    
def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastrar Restaurante')

    nome_do_restaurante = input('Digite o nome do restaurante:')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado!')
    
    voltar_ao_menu_principal()
    
def listar_restaurantes():
    exibir_subtitulo('Listar restaurantes')
    
    for restaurante in restaurantes:
        print(f'- {restaurante}')
    
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
                print('Ativar restaurante')
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()
    
def exibir_subtitulo(texto): 
    os.system('cls' if os.name == 'nt' else 'clear')
    print(texto)
    print()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()
    
if __name__ == '__main__':
    main()