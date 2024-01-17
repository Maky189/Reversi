def main():
    conjunto1 = {i for i in range(1, 11, 2)}
    conjunto2 = {i for i in range(2, 11, 2)}
    
    print(conjunto1.intersection(conjunto2))
    
main()