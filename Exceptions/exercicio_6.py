
from cmath import exp


def main():
    try:
        number_1 = float(input("Insira um número: "))
        number_2 = float(input("Insira outro número: "))
        result = number_1 / number_2
        
        print("Resultado: {:.2f}".format(resultado))  
    except ValueError:
        print("Isso não é um número.")
    except ZeroDivisionError:
        print("Divisão por 0 indeterminada.")
    except:
        print("Algo deu errado.")

main()

# Algo deu errado
