def main() -> None:
    nomeArq = input('Digite o nome do arquivo: ')
    arq = open(nomeArq, 'w')
    escrita = input('Escreva algo no arquivo (*Enter* para parar): ')
    while escrita != '':
        arq.write(escrita)
        escrita = input('Escreva algo no arquivo (*Enter* para parar): ')
    arq.close()

if __name__ == '__main__':
    main()