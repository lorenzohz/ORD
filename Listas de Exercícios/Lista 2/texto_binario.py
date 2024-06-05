# Essa função converte um arquivo para binário e cria um novo arquivo com essa conversão

def main() -> None:
    nome_arq = input('Nome do arquivo: ')

    try:
        arq = open(nome_arq, 'r')

    except FileNotFoundError:
        print('Erro ao abrir o arquivo!')

    else:
        texto = arq.read()
        bytes = texto.encode()
        with open(nome_arq + '_binario', 'wb') as novo_arq:
            novo_arq.write(bytes)

if __name__ == '__main__':
    main()