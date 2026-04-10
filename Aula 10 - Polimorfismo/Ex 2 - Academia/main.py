from PlanoBasico import PlanoBasico
from PlanoPremium import PlanoPremium
from PlanoVIP import PlanoVIP

def main():

    # Cria lista com diferentes tipos de plano
    planos = []
    planos.append(PlanoBasico(100))
    planos.append(PlanoPremium(200, 10))
    planos.append(PlanoVIP(300, 10, 80))

    # Imprime os custos das mensalidades utilizando polimorfismo
    for plano in planos:
        print(f"Mensalidade: {plano.calcular_mensalidade()}")

if __name__ == "__main__":
    main()