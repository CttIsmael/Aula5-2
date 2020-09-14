def parcela(preco):
    for c in range(1, 25):
        prest = preco/c
        print(f'{c}x de R$ {prest:.2f}')

def main():
    p = int(input())
    parcela(p)

if __name__ == "__main__":
    main()
