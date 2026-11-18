"""Exemplo didático com temperaturas fictícias, sem sensor conectado."""


def main():
    temperaturas = [23.5, 24.0, 24.5]
    print("TesteIOT - leituras fictícias de temperatura")
    for numero, temperatura in enumerate(temperaturas, start=1):
        print(f"Leitura {numero}: {temperatura:.1f} °C")
    print("Exemplo concluído.")


if __name__ == "__main__":
    main()
