
def input_handling():
    try:
        number = int(input("Digite um número: "))
        print("O número digitado foi: ", number)
    except ValueError:
        print("Valor inválido!")
        
input_handling()
