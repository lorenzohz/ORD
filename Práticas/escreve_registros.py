def main() -> None:
    nome_arq = input('Nome do Arquivo: ')
    campo = input('Sobrenome ou ENTER para sair: ')
    saida = open(nome_arq, 'wb')
    while campo != '':

        nome = input('Nome: ')
        endereco = input('Endereço: ')
        cidade = input('Cidade: ')
        estado = input('Estado: ')
        cep = input('CEP: ')
        buffer = (campo + '|' + endereco + '|' + cidade + '|' + estado + '|' + cep + '|')

        buffer = buffer.encode() #type: ignore
        tam = len(buffer)
        tam = tam.to_bytes(2) #type: ignore

        saida.write(tam + buffer) #type: ignore

        campo = input('Sobrenome ou ENTER para sair: ')
    saida.close()

if __name__ == '__main__':
    main()
