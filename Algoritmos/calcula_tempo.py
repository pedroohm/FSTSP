import math
import numpy as np

class Calcula_tempo(object):

    def __init__(self):
        self.__nodes = []
        self.__truckMatriz = [[]]
        self.__droneMatriz = [[]]
        
    def distanciaEuclidiana(x, y, velocidade=20):
        distancia = math.sqrt((y[0] - x[0])**2 + (y[1] - x[1])**2)
        tempo = distancia / velocidade
        return tempo

    #usar absoluto do numpy
    def distanciaManhattan(self, x1, y1, x2, y2, velocidade=40):
        if x1>x2:
            x = x1-x2
        else:
            x = x2-x1
        if y1>y2:
            y = y1-y2
        else:
            y = y2-y1
        distancia = x + y
        tempo = distancia / velocidade
        return tempo


    def readNodes(self):
        file = open("nodes.csv", 'r')
        lines = file.readlines()
        normalize = False
        self.__nodes == []
        for line in lines:
            line = stringToIntArray(line)
            if(self.__nodes == []):
                firstId = int(line[0].strip())
                if(firstId == 1):
                    normalize = True
                    self.__nodes.append([firstId - 1, float(line[1].strip()), float(line[2].strip()), int(line[3].strip())])
                else:
                    self.__nodes.append([int(line[0].strip()), float(line[1].strip()), float(line[2].strip()), int(line[3].strip())])
    
            elif(normalize):
                self.__nodes.append([int(line[0].strip()) - 1, float(line[1].strip()), float(line[2].strip()), int(line[3].strip())])
            else:
                self.__nodes.append([int(line[0].strip()), float(line[1].strip()), float(line[2].strip()), int(line[3].strip())])
        
        self.__truckMatriz = [[]*len(self.__nodes)]
        self.__droneMatriz = [[]*len(self.__nodes)]

        self.fillTruckMatriz()

    def fillTruckMatriz(self):
        for i in range (len(self.__nodes)):
            x1 = float(self.__nodes[i][1])
            y1 = float(self.__nodes[i][2])
            for j in range (len(self.__nodes)-i):
                if i==j:
                    self.__truckMatriz = 0
                else:
                    x2 = float(self.__nodes[j][1])
                    y2 = float(self.__nodes[j][2])

                    self.__truckMatriz[i][j] = self.distanciaManhattan(x1, y1, x2, y2)
                    self.__truckMatriz[j][i] = self.__truckMatriz[i][j]

    
    def imprimeTruckMatriz(self):
        print(type(self.__truckMatriz))
        print("tempos do caminhao")
        print(self.__truckMatriz)
                

    
    def imprime(self):
        print(len(self.__nodes))
        print(self.__nodes)
        print(self.__truckMatriz)
        print(self.__droneMatriz)


# Funções auxiliares
def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

def stringToIntArray(str):
 str = str.strip('\n')
 str = str.split(',')
 str = remove_values_from_list(str,' ')
 str = remove_values_from_list(str,'')
 return str


nodos = Calcula_tempo()

nodos.readNodes()

nodos.imprime()
nodos.imprimeTruckMatriz()
