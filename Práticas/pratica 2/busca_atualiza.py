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
                rrn = int(input("Número do registro à ser modificado: "))
                achou = busca_rrn(arq, rrn)
                if not achou:
                    print("Erro, não foi possível encontrar o registro desejado!")
                else:
                    confirmacao = input("\nDeseja modificar esse registro (S/N): ")
                    if confirmacao == "S":
                        sobrenome = input('Sobrenome: ')
                        nome = input('Nome: ')
                        endereco = input('Endereço: ')
                        cidade = input('Cidade: ')
                        estado = input('Estado: ')
                        cep = input('CEP: ')
                        buffer = (sobrenome + '|' + nome + '|' + endereco + '|' + cidade + '|' + estado + '|' + cep + '|')
                        buffer_bin = buffer.encode()
                        buffer_bin = buffer_bin.ljust(64, b'\0')
                        offset = (rrn * 64) + 4
                        arq.seek(offset, os.SEEK_SET)
                        arq.write(buffer_bin)

            elif operacao == '3':
                print('Código encerrado. Arquivo criado/atualizado!')
            else:
                print("Operação Inválida!")
        arq.close()


def busca_rrn(entrada ,rrn: int) -> bool:
    '''
    Recebe o arquivo e o endereço RRN e printa as informações do campo caso exista, enviando uma mensagem de erro caso contrário.
    Retorna True caso o endereço exista e False caso não.
    '''
    entrada.seek(0, os.SEEK_SET)
    cab = entrada.read(4) # lê cabeçalho
    num_reg = int.from_bytes(cab)
    if rrn > num_reg:
        return False
    else:
        offset = (rrn * 64) + 4
        entrada.seek(offset, os.SEEK_SET)
        registro = entrada.read(64)
        registro = registro.decode() #type: ignore
        registro = registro.split('|') #type: ignore
        for i in range(len(registro)-1):
            print(f'Campo {i+1}: {registro[i]}')
        return True



if __name__ == '__main__':
    main()