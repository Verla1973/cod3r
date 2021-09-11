# Usando funções com retorno
import math


def circulo(raio):
    return math.pi * raio ** 2

raio = float(input('Digite o raio: '))
area = circulo(raio)
print(f'Área da circunferência: {area:.2f}')
