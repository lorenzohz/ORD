def leia_campo(entrada):
    campo = ''
    c = entrada.read(1)
    while c != '' and c != '|':
        campo += c
        c = entrada.read(1)
    return campo

def main() -> None:
    nome_arq = input('Nome do Arquivo: ')
    try:
        entrada = open(nome_arq, 'r')
        campo = leia_campo(entrada)
        contador = 1
        while campo != "":
            print(f'Campo #{contador}: {campo}')
            contador += 1
            campo = leia_campo(entrada)
    except FileNotFoundError:
        print('Falha em abrir o arquivo!')
    except:
        print('Erro Inesperado!')

if __name__ == '__main__':
    main()
