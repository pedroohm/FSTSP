import math
import numpy as np
import csv

class Calcula_tempo(object):

    def __init__(self):
        self.__nodes = []
        self.__truckMatrix = [[]]
        self.__truckMatrix = []
        
    def distanciaEuclidiana(self, x1, x2, y1, y2, velocidade=40):
        distancia = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        tempo = distancia / velocidade
        return tempo

    def distanciaManhattan(self, x1, y1, x2, y2, velocidade=40):
        distancia = abs(x2-x1) + abs(y2-y1)
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
    
    def inicializar_matriz(self, linha, coluna):
        matriz = [[i+ 1 for i in range(coluna)] for j in range(linha)]
        return matriz    


    def fillTruckmatrix(self):
        n = len(self.__nodes)
        
        self.__truckMatrix = self.inicializar_matriz(n,n)
        
        for i in range(n):
            x1 = float(self.__nodes[i][1])
            y1 = float(self.__nodes[i][2])

            if i==n-1:
                for j in range(n):
                    self.__truckMatrix[i][j] = 0
                continue
            
            for j in range(n):
                if i==j:
                    self.__truckMatrix[i][i] = 0
                else:
                    x2 = float(self.__nodes[j][1])
                    y2 = float(self.__nodes[j][2])

                    self.__truckMatrix[i][j] = self.distanciaManhattan(x1, y1, x2, y2)
                    self.__truckMatrix[j][i] = self.__truckMatrix[i][j]
            
        return self.__truckMatrix
    
    def fillDronematrix(self):
        n = len(self.__nodes)
        self.__droneMatrix = self.inicializar_matriz(n,n)
        for i in range(n):
            x1 = float(self.__nodes[i][1])
            y1 = float(self.__nodes[i][2])

            if i==n-1:
                for j in range(n):
                    self.__truckMatrix[i][j] = 0
                continue
            
            for j in range(n):
                if i==j:
                    self.__droneMatrix[i][i] = 0
                else:
                    x2 = float(self.__nodes[j][1])
                    y2 = float(self.__nodes[j][2])
                    self.__droneMatrix[i][j] = self.distanciaEuclidiana(x1, x2, y1, y2)
                    self.__droneMatrix[j][i] = self.__droneMatrix[i][j]
        return self.__droneMatrix

    def saveTruckmatrix(self):
        caminho_arquivo = 'tau.csv'

        with open(caminho_arquivo, 'w', newline='') as arquivo_csv:
            writer = csv.writer(arquivo_csv)
            writer.writerows(self.__truckMatrix)
    
    def saveDroneMatrix(self):
        caminho_arquivo = 'tauprime.csv'

        with open(caminho_arquivo, 'w', newline='') as arquivo_csv:
            writer = csv.writer(arquivo_csv)
            writer.writerows(self.__droneMatrix)
    

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
nodos.fillTruckmatrix()
nodos.fillDronematrix()
nodos.saveTruckmatrix()
nodos.saveDroneMatrix()