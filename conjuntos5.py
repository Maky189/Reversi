import sys

def main():
    pares_ordenados = {(1, 2), (2, 3), (1, 3)}
    transitiva = True
    for i, j in pares_ordenados:
        for x, y in pares_ordenados:
            if j == x and not (i, y) in pares_ordenados:
                transitiva = False
        if not transitiva:
            break
            
    if transitiva:
        print("transitiva")
    else:
        print("nao transitiva")
        
main()