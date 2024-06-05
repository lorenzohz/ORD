# Foi  visto  em  aula  um  programa  que  lê  um  arquivo  texto  e  o  escreve  em  tela  (slide  24  do  arquivo 
# “Operações em Arquivos.pdf”). Modifique esse programa para que ele leia os dados a partir da entrada 
# padrão, em vez de um arquivo, e os escreva em um arquivo, em vez da saída padrão. 

def main() -> None:
    # Solicitar o nome do arquivo ao usuário
    nomeArq = input('Digite o nome do arquivo: ')
    # Abrir o arquivo para escrita
    arq = open(nomeArq, 'w')
    # Escrever no arquivo
    escrita = input('Escreva algo no arquivo (*Enter* para parar): ')
    while escrita != '':
        arq.write(escrita)
        arq.write('\n')
        escrita = input('Escreva algo no arquivo (*Enter* para parar): ')
    # Fechar o arquivo
    arq.close()

if __name__ == '__main__':
    main()