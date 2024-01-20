import os

print("""
████████████████████████████████████████
█─▄▄▄▄██▀▄─██▄─▄─▀█─▄▄─█▄─▄▄▀█▄─▄▄─█▄─▄█
█▄▄▄▄─██─▀─███─▄─▀█─██─██─▄─▄██─▄█▀██─██
▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▀
""")

print('1. Cadastrar Restaurante')
print('2. Listar restaurantes')
print('3. Ativar Reustaurante')
print('4. Sair\n')

opcao_escolhida = int(input('Escolha uma opção: '))
# print(f'Você enscolheu a opção {opcao_escolhida}')

def finalizar_app():
    os.system('cls')
    print('Encerrando programa')

if opcao_escolhida == 1:
    print('Cadastrar restaurante')
elif opcao_escolhida == 2:
    print('Listar restaurantes')
elif opcao_escolhida == 3:
    print('Ativar restaurante')
else:
    finalizar_app()