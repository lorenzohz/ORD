from sys import argv
import io
# CONSTANTES
VALOR_BAIXO = ''
VALOR_ALTO = '~'

def inicialize(numListas: int) -> tuple[list[str], list[str], list[io.TextIOWrapper], io.TextIOWrapper, bool, int]:
    anteriores = []
    nomes = []
    listas = []
    for i in range(numListas):
        anteriores.append(VALOR_BAIXO)
        nomes.append(VALOR_BAIXO)

        nomearq = "lista"+str(i)+".txt"
        descritor = open(nomearq, "r")
        listas.append(descritor)
    saida = open("listamergedkway.txt", "w")
    existem_mais_nomes = True
    numEOF = 0

    return anteriores, nomes, listas, saida, existem_mais_nomes, numEOF

def finalize(listas: list[io.TextIOWrapper], saida: io.TextIOWrapper, numListas: int) -> None:
    for lista in listas:
        lista.close()
    saida.close()

def leia_nome(lista: io.TextIOWrapper, nome_ant: str, existem_mais_nomes: bool, numListas: int, numEOF: int) -> tuple[str, str, bool, int]:
    nome = lista.readline()
    if not nome:
        nome = VALOR_ALTO
        numEOF += 1
        if numEOF == numListas:
            existem_mais_nomes = False
    elif nome <= nome_ant:
        raise ValueError('Erro de Sequência!')
    nome_ant = nome
    return nome, nome_ant, existem_mais_nomes, numEOF

def kwaymerge(numListas: int) -> None:
    anteriores, nomes, listas, saida, existem_mais_nomes, numEOF = inicialize(numListas)
    for i in range(numListas):
        nomes[i] = listas[i].readline()
    while existem_mais_nomes:
        menor = 0
        for i in range(numListas):
            if nomes[i] < nomes[menor]:
                menor = i

        saida.write(nomes[menor])
        nomes[menor], anteriores[menor], existem_mais_nomes, numEOF = leia_nome(listas[menor],anteriores[menor], existem_mais_nomes, numListas, numEOF)
    finalize(listas, saida, numListas)


def main() -> None:
    if len(argv) < 2:
        raise TypeError('Número Incorreto de argumentos!')
    kwaymerge(int(argv[1]))


if __name__ == '__main__':
    main()
