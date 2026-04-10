from EnvioSimples import EnvioSimples
from EnvioExpresso import EnvioExpresso
from EnvioInternacional import EnvioInternacional

def main():

    # Cria lista com diferentes tipos de envio
    envios = []
    envios.append(EnvioSimples(100))
    envios.append(EnvioExpresso(200, 10))
    envios.append(EnvioInternacional(300, 20, 50))

    # Imprime os custos dos fretes utilizando polimorfismo
    for envio in envios:
        print(f"Frete: {envio.calcular_frete()}")

if __name__ == "__main__":
    main()