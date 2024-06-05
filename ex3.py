# Faça  um  programa  que  solicite  ao  usuário o  nome  de  um  arquivo  de  texto  para  que  espaços  repetidos 
# sejam removidos. Um novo arquivo deve ser criado com o resultado da remoção.

def main() -> None:
    # Solicitar o nome do arquivo de texto ao usuário
    nome_arquivo = input("Digite o nome do arquivo de texto: ")

    try:
        # Abrir o arquivo de texto para leitura
        with open(nome_arquivo, 'r') as arquivo:
            # Ler o conteúdo do arquivo
            conteudo = arquivo.read()

        # Remover espaços repetidos
        while "  " in conteudo:
            conteudo = conteudo.replace("  ", " ")

        # Criar um novo arquivo com o resultado da remoção
        novo_nome_arquivo = f"novo_{nome_arquivo}"
        with open(novo_nome_arquivo, 'w') as novo_arquivo:
            novo_arquivo.write(conteudo)

        print(f"Espaços repetidos removidos. Novo arquivo criado: {novo_nome_arquivo}")

    except FileNotFoundError:
        print("Arquivo não encontrado.")

if __name__ == '__main__':
    main()