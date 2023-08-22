from TSPDReader import TSPDReader1
from Solver import Solver
from openpyxl import Workbook

import os
import time


sheetName = input("Digite o nome do arquivo com os resultados: ")
firstLine = ("Instância", "Tempo", "Tempo de execução")
sheet = Workbook()
sheet1 = sheet.active

sheet1.append(firstLine)

folders = os.listdir(TSPDReader1.directory)
for folder in folders: # Percorre os diretórios da pasta raiz

    print("inicio da solucao para ", folder)

    reader = TSPDReader1()

    reader.read(folder)

    solver = Solver(reader.getTruckMatrix(), reader.getDroneMatrix(), reader.getNodes(), 1, 1, 20)

    startTime = time.time()
    
    solver.HVMP(1)

    result = solver.RVND()
    endTime = time.time()   

    valores = [0, -10, 9, 5, 6, 3, 4, 2, -8, 11, 12, 7, -13, 1, 14]
    solver.setRepresentation(valores)
    solver.fillCvector()

    sheet1.append((folder, result, endTime - startTime))
    sheet.save('./saidas/' + sheetName + '.xlsx')

    print("termino da solucao para ", folder)