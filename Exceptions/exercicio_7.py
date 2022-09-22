
def main():
    try:
        file = open("file.txt", "r")
        file_lines = file.readline()
        file.close()
    except FileNotFoundError:
        print("O arquivo selecionado não foi encontrado!")

main()