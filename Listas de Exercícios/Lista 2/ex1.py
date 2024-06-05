def main() -> None:
    # Solicitar o nome do arquivo ao usuário
    nomeArq = input('Digite o nome do arquivo: ')
    # Abrir o arquivo para escrita
    arq = open(nomeArq, 'w')
    # Escrever no arquivo
    escrita = input('Escreva algo no arquivo (*Enter* para parar): ')
    while escrita != '':
        arq.write(escrita)
        escrita = input('Escreva algo no arquivo (*Enter* para parar): ')
    # Fechar o arquivo
    arq.close()

if __name__ == '__main__':
    main()