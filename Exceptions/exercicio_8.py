
def main():
    file = open("file.txt", "r")
    try:
        file.write("Exemplo de texto")
    except IOError:
        print("Não foi possível escrever no arquivo.")
    finally:
        print("Liberando arquivo da memória...")
        file.close()
        
main()
