import math

def tempoDistanciaEuclidiana(x, y, velocidade):
    distancia = math.sqrt((y[0] - x[0])**2 + (y[1] - x[1])**2)
    tempo = distancia / velocidade
    return tempo

def tempoDistanciaManhattan(x, y, velocidade):
    distancia = abs(y[0] - x[0]) + abs(y[1] - x[1])
    tempo = distancia / velocidade
    return tempo