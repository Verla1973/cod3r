# Usando funções
import math


def circulo(raio):
    print(f'Área da circunferência: {math.pi * raio ** 2:.2f}...')

raio = float(input('Digite o raio: '))
circulo(raio)
