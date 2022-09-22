
def calc_division(m: int, n: int):
    try:
        print(m / n)
    except ZeroDivisionError:
        print("Não é possível dividir por 0!")
        
        
def main(): 
    exit = False
    while exit == False:
        try: 
            m = int(input("Insira um numerador: "))
            n = int(input("Insira um denominador: "))
            calc_division(m, n)
            exit = True
        except KeyboardInterrupt:
            print("\nEncerrando programa...")
            exit = True
        except ValueError:
            print("Valor inválido!")    
main()