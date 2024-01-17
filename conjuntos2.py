def main():

    conjunto = {i for i in range(0, 11)}
    print(remover_pares(conjunto))

def remover_pares(conjunto):
    novo_conjunto = set()
    for i in conjunto:
        if not (i % 2 == 0):
            novo_conjunto.add(i)
    return novo_conjunto
    
main()
