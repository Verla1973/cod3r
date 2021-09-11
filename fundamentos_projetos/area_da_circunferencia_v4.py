# Importando o math e recebendo o raio pelo usuário
import math


raio = float(input('Digite o raio: '))
area_da_circunferencia = math.pi * raio ** 2
print(f'Área da circunferência: {area_da_circunferencia:.2f}')
