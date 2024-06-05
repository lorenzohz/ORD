def leia_reg(entrada):
    tam = entrada.read(2)
    tam = int.from_bytes(tam)

    if tam > 0:
        buffer = entrada.read(tam)
        buffer = buffer.decode()
        return buffer
    else:
        return ''

nome_arq = input('Nome do Arquivo: ')

def main() -> None:
    try:
        entrada = open(nome_arq, 'rb')
        buffer = leia_reg(entrada)
        campo_cont = 1
        reg_cont = 1
        while buffer != "":
            buffer = buffer.split(sep='|')
            print(f'Registro #{reg_cont}')
            for campo in buffer[:-1]:
                print(f'Campo #{campo_cont}: {campo}')
                campo_cont += 1
            campo_cont = 1
            reg_cont += 1
            buffer = leia_reg(entrada)
    except FileNotFoundError:
        print('Falha em abrir o arquivo!')
    except:
        print('Erro Inesperado!')

if __name__ == '__main__':
    main()
    