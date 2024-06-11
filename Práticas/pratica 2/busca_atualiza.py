import os

def main() -> None:
    try:
        nome_arq = input('Insira o nome do arquivo (para ler ou criar): ')
        arq = open(nome_arq, 'r+b')
    except FileNotFoundError:
        arq = open(nome_arq, 'w+b')
        n_reg = 0
        arq.write(n_reg.to_bytes(4))
    finally:
        operacao = ''
        while operacao != '3':
            operacao = input('Operações: \n\n1. Inserir novo registro. \n2. Buscar registro por RRN para alterações. \n3.Terminar o programa \n\nEscreva a operação desejada: ')
            if operacao == '1': #inserir novo
                sobrenome = input('Sobrenome: ')
                nome = input('Nome: ')
                endereco = input('Endereço: ')
                cidade = input('Cidade: ')
                estado = input('Estado: ')
                cep = input('CEP: ')
                buffer = (sobrenome + '|' + nome + '|' + endereco + '|' + cidade + '|' + estado + '|' + cep + '|')
                buffer_bin = buffer.encode()
                buffer_bin = buffer_bin.ljust(64, b'\0')
                arq.seek(0, os.SEEK_END)
                arq.write(buffer_bin)
                #atualizar cabeçalho
                arq.seek(0, os.SEEK_SET)
                cabecalho = arq.read(4)
                n_reg = int.from_bytes(cabecalho)
                n_reg += 1
                cabecalho = n_reg.to_bytes(4)
                arq.seek(0, os.SEEK_SET)
                arq.write(cabecalho)

            elif operacao == '2': #buscar e alterar
                print('notimplemented')
            elif operacao == '3':
                print('código encerrado!')
            else:
                print("Operação Inválida!")


if __name__ == '__main__':
    main()