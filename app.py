from downloader import *
import os

def main():
    os.system('cls')
    print('Olá, sou Kobe!!')
    print('Digite o número da opção que deseje fazer\n')
    
    print('1 - Baixar Música')
    print('2 - Sair')

    opcao = input()

    if opcao == '1':
        while True:
            os.system('cls')
            baixar_mp3()

            os.system('cls')
            print('---- DOWNLOAD COMPLETO ----\n')
            print('1 - Baixar outra música')
            print('2 - Voltar ao menu')
            
            select = input()

            if select == '1':
                pass
            else:
                main()

    elif opcao == '2':
        os.system('cls')
        exit()

    else:
        input('Selecione uma opção existente')
        main()
    
        

main()