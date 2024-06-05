def main() -> None:
    nome_arq = input('Nome Do Arquivo: ')
    arq = open(nome_arq, 'r')
    texto = arq.readlines()
    linhas = len(texto)
    array = ''
    for linha in texto: array += linha
    em_bytes = array.encode()
    print(f'O tamanho do arquivo em bytes é: {len(em_bytes)} bytes. \nO arquivo possui: {linhas} linhas.')

if __name__ == '__main__':
    main()