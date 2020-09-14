def bug(n, m, p):
    for i in range(n, m+1, p):
        print(f'{i} bugs no software, pegue onze deles e conserte...')
        print("Tecle" + '"Ctrl + F5"')

    print("Sem erros no software! Está estabilizado!")

def main():
    bug(99, 0, -11)

if __name__ == "__main__":
    main()
