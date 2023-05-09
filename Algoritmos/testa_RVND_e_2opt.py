from TSPDReader import TSPDReader1
from Solver import Solver
from openpyxl import Workbook

import os
import time


sheetName = input("Digite o nome do arquivo com os resultados: ")
arquivo = open('./saidas/'+sheetName+'.txt', 'w')
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
    solver.HVMP(1)

    print("inicio da solucao", folder)
    solver.plotarSolucao(folder + ' in ' + sheetName + ' inicial')
    arquivo.write("Solucao inicial para: "+ folder + '\n')
    solucao = solver.getSolution()
    for i in range(len(solucao)):
        arquivo.write(str(solucao[i])+' ')
    arquivo.write('\n')

    #result = solver.localSearch2OPT()
    result = solver.RVND()
    endTime = time.time()

    #solver.plotarSolucao(sheetName +' final+drone', 2)
    arquivo.write("Solucao final para: "+ folder + '\n')
    solucao = solver.getSolution()
    for i in range(len(solucao)):
        arquivo.write(str(solucao[i])+' ')
    arquivo.write('\n')

    solver.plotarSolucao(folder + ' in ' + sheetName + ' final')
    print("termino da solucao", folder)

    sheet1.append((folder, result, endTime - startTime))
    sheet.save('./saidas/' + sheetName + '.xlsx')
arquivo.close()
