def leia_reg(entrada):
    tam = entrada.read(2)
    tam = int.from_bytes(tam)

    if tam > 0:
        buffer = entrada.read(tam)
        buffer = buffer.decode()
        return buffer
    else:
        return ''

def main() -> None:
    try:
        nome_arq = input('Digite o nome do arquivo a ser lido: ')
        entrada = open(nome_arq, "rb")
    except FileNotFoundError:
        print('Arquivo não encontrado!')
    else:
        sobrenome = input('Sobrenome desejado: ')
        registro = leia_reg(entrada)
        achou = False
        while registro != '' and not achou:
            registro = registro.split(sep='|')
            if registro[0] == sobrenome:
                achou = True
            else:
                registro = leia_reg(entrada)
        if achou:
            print('Sobrenome encontrado! Seguem os campos:\n')
            for i in range(len(registro)-1):
                print(f'Campo {i+1}: {registro[i]}')
        else:
            print('Sobrenome não encontrado!')


if __name__ == '__main__':
    main()