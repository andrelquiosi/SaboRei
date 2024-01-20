import os

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
    os.system('cls')
    print('Encerrando programa')

def escolher_opcoes():
    opcao_escolhida = int(input('Escolha uma opção: '))
    # print(f'Você enscolheu a opção {opcao_escolhida}')

    match opcao_escolhida:
        case  1:
            print('Cadastrar restaurante')
        case 2:
            print('Listar restaurantes')
        case 3:
            print('Ativar restaurante')
        case 4:
            finalizar_app()
        case _:
            print('Opção inválida!')
    
def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()
    
if __name__ == '__main__':
    main()