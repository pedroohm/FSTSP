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

# print(os.curdir)
folders = os.listdir(TSPDReader1.directory)
for folder in folders: # Percorre os diretórios da pasta raiz
    reader = TSPDReader1()

    reader.read(folder)

    solver = Solver(reader.getTruckMatrix(), reader.getDroneMatrix(), reader.getNodes(), 1, 1, 20)

    startTime = time.time()

    solver.HVMP(3)

    solver.plotarSolucao(sheetName +' inicial')
    print("Solucao inicial: ", solver.getSolution())

    result = solver.RVND()
    endTime = time.time()

    #solver.plotarSolucao(sheetName +' final+drone', 2)
    print("Solucao Final: ", solver.getSolution())
    solver.plotarSolucao(sheetName+' final')

    sheet1.append((folder, result, endTime - startTime))
    sheet.save(sheetName + '.xlsx')
