def main() -> None:
    nome_arq = input('Nome do Arquivo: ')
    sobrenome = input('Sobrenome ou ENTER para sair: ')
    saida = open(nome_arq, 'w')
    while sobrenome != '':
        nome = input('Nome: ')
        endereco = input('Endereço: ')
        cidade = input('Cidade: ')
        estado = input('Estado: ')
        cep = input('CEP: ')
        saida.write(sobrenome + '|' + endereco + '|' + cidade + '|' + estado + '|' + cep + '|')
        sobrenome = input('Sobrenome ou ENTER para sair: ')

    saida.close()

if __name__ == '__main__':
    main()
