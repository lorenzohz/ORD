import os
# Escreve registros fixos de tamanho 128 Bytes; exercício 8 da lista 3

def main() -> None:
    nome_arq = input('Nome do Arquivo: ')
    campo = input('Sobrenome ou ENTER para sair: ')
    arq = open(nome_arq, 'wb')
    n_reg = 0
    cab = n_reg.to_bytes(8)
    arq.write(cab)
    while campo != '':

        nome = input('Nome: ')
        endereco = input('Endereço: ')
        cidade = input('Cidade: ')
        estado = input('Estado: ')
        cep = input('CEP: ')
        buffer = (campo + '|' + nome + '|' + endereco + '|' + cidade + '|' + estado + '|' + cep + '|')

        buffer = buffer.encode() #type: ignore

        registro = buffer.ljust(128, b"\0") # type: ignore

        arq.write(registro) #type: ignore
        n_reg += 1

        campo = input('Sobrenome ou ENTER para sair: ')
    arq.seek(0, os.SEEK_SET)
    cab = n_reg.to_bytes(8)
    arq.write(cab)
    arq.close()

if __name__ == '__main__':
    main()
