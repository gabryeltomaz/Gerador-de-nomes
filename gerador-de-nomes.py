import random

# Listas de sílabas ou partes de palavras
prefixos = ["Zan", "Mor", "El", "Gor", "Val", "Fen", "Tar", "Riv", "Lun", "Kas", "Bra", "Lou", "jin", "Uoi"]
sufixos = ["dor", "mar", "ton", "ros", "var", "len", "gorn", "rin", "lek", "mon", "son", "lun", "bin", "xin"]
meios = ["a", "e", "i", "o", "u", "ar", "en", "il", "or", "un", "in", "ou", "liu", "po", "jah", "qui"]

def gerar_nome():
    prefixo = random.choice(prefixos)
    sufixo = random.choice(sufixos)
    meio = random.choice(meios)
    return prefixo + meio + sufixo

def main():
    print("\n\nGerador de Nomes Aleatórios para Jogos\n\n")
    while True:
        num_nomes = input("Quantos nomes vc quer gerar? (Digite 'sair' para sair): ")
        if num_nomes.lower() == 'sair':
            break
        try:
            num_nomes = int(num_nomes)
            for _ in range(num_nomes):
                print(gerar_nome())
        except ValueError:
            print("Digite um numero valido ou 'sair'.")

if __name__ == "__main__":
    main()
