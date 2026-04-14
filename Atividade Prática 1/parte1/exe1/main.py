from Bolo import Bolo

def main():
    bolo1 = Bolo("Cenoura", "Brigadeiro", "Cenoura", True)
    bolo2 = Bolo("Formigueiro", "Brigadeiro", "Baunilha", False)


    bolo3 = Bolo("Cenoura", "Brigadeiro", "Cenoura", False)


    print(bolo1)
    print(bolo2)
    print(bolo3)
    bolo3 = bolo1
    bolo3.temCobertura = False


    print(bolo1)
    print(bolo2)
    print(bolo3)

if __name__ == "__main__":
    main()