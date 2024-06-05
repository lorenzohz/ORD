def main() -> None:
    # solicitar o nome do arquivo ao usuário
    nome_arq = input('Nome Do Arquivo: ')

    try:
        # abrir o arquivo para leitura
        arq = open(nome_arq, 'r')
    except FileNotFoundError:
        # caso o arquivo não seja encontrado
        print('Arquivo não encontrado.')
    else:
        # ler o conteúdo do arquivo e contar o número de linhas e tamanho em bytes
        texto = arq.readlines()
        linhas = len(texto)
        array = ''
        for linha in texto: array += linha
        em_bytes = array.encode()
        
        # fechar o arquivo
        arq.close()

        # exibir o tamanho do arquivo e o número de linhas
        print(f'O tamanho do arquivo em bytes é: {len(em_bytes)} bytes. \nO arquivo possui: {linhas} linhas.')

if __name__ == '__main__':
    main()