# Lê registros fixos de tamanho 128 Bytes; exercício 8 da lista 3

nome_arq = input('Nome do Arquivo: ')

def main() -> None:
    try:
        arq = open(nome_arq, 'rb')
        cab = arq.read(8)
        n_reg = int.from_bytes(cab)
        campo_cont = 1
        reg_cont = 1
        buffer = arq.read(128)
        for i in range(n_reg):
            print("\n")
            buffer_dec = buffer.decode()
            registro = buffer_dec.split(sep='|')
            print(f'Registro #{reg_cont}')
            for campo in registro[:-1]:
                print(f'Campo #{campo_cont}: {campo}')
                campo_cont += 1
            campo_cont = 1
            reg_cont += 1
            buffer = arq.read(128)
    except FileNotFoundError:
        print('Falha em abrir o arquivo!')
    


if __name__ == '__main__':
    main()
    