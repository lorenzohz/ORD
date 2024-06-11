import os

def main() -> None:
    try:
        nome_arq = input('Insira o nome do arquivo: ')
        entrada = open(nome_arq, 'rb')
    except FileNotFoundError:
        print('Arquivo não encontrado!')
    else:
        cab = entrada.read(4) # lê cabeçalho
        num_reg = int.from_bytes(cab)
        rrn = int(input('Digite o número do registro à ser lido pelo programa: '))
        if rrn > num_reg:
            print('Arquivo não existe!')
        else:
            offset = (rrn * 64) + 4
            entrada.seek(offset, os.SEEK_SET)
            registro = entrada.read(64)
            registro = registro.decode() #type: ignore
            registro = registro.split('|') #type: ignore
            for i in range(len(registro)-1):
                print(f'Campo {i+1}: {registro[i]}')
            


if __name__ == '__main__':
    main()