from math import sqrt


def calc_square_root(number: int):
    try:
        print(sqrt(number))
    except ValueError:
        print("Não é possível calcular a raiz quadrada de um número menor que 0!")
    

def main(): 
    exit = False
    while exit == False:
        try: 
            input_number = int(input("Insira um número: "))
            calc_square_root(input_number)
            exit = True
        except KeyboardInterrupt:
            print("\nEncerrando programa...")
            exit = True
        except ValueError:
            print("Valor inválido!")    
main()
