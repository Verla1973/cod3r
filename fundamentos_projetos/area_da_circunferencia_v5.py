# testando se é o módulo principal
import math


if __name__ == "__main__":
    raio = float(input('Digite o raio: '))
    area_da_circunferencia = math.pi * raio ** 2
    print(f'Área da circunferência: {area_da_circunferencia:.2f}')
