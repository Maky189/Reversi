def main():
    conjunto1 = {"branco", "preto", "azul", "vermelho", "verde"}
    conjunto2 = {"verde", "amarelo", "azul", "castanho", "preto"}
    
    print(f"cores presentes em ambos: {conjunto1.intersection(conjunto2)}")
    print(f"uniao dos dois conjuntos: {conjunto1.union(conjunto2)}")
main()