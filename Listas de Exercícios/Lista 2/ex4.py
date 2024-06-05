# Faça um programa que receba do usuário um arquivo de código em python e produza um novo arquivo 
# contendo o mesmo código, mas com todos os comentários de linha removidos. Um comentário de linha 
# começa com ‘#’ em qualquer posição de uma linha e se estende até o final dela.

def main() -> None:
    # Solicitar o nome do arquivo de código Python ao usuário
    nome_arquivo = input("Digite o nome do arquivo de código Python: ")

    try:
        arq = open(nome_arquivo, 'r')
        conteudo = arq.readlines()
        arq.close()

    except FileNotFoundError:
        print("Arquivo não encontrado.")
    
    else:
        novo_nome = f"sem_comentarios_{nome_arquivo}"

        with open(novo_nome, 'w') as novo_arquivo:
            for linha in conteudo:
                for i in range(len(linha)):
                    if linha[i] == '#':
                        linha = linha[:i] + '\n'
                        break
                novo_arquivo.write(linha)

        print(f"Comentários de linha removidos. Novo arquivo criado: {novo_nome}")


if __name__ == '__main__':
    main()