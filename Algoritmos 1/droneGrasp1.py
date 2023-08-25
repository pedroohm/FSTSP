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
    print('Inicio: ', folder) # Imprime o nome da pasta que está sendo lida

    solver = Solver(reader.getTruckMatrix(), reader.getDroneMatrix(), reader.getNodes(), 1, 1, 20)

    startTime = time.time()
    solver.HVMP(3)

    print("inicio da solucao", folder)
    
    #solver.plotarSolucao(folder + ' in ' + sheetName + ' inicial')

    arquivo.write("Solucao inicial para: "+ folder + '\n')
    solucao = solver.getSolution()
    for i in range(len(solucao)):
        arquivo.write(str(solucao[i])+' ')
    arquivo.write('\n')

    #solver.getDroneDeliveries()
    
    print("Create Representation")
    solver.createRepresentation()

    result = solver.droneGrasp(5,3)


    
    endTime = time.time()

    arquivo.write("Solucao final para: "+ folder + '\n')
    solucao = solver.getSolution()
    for i in range(len(solucao)):
        arquivo.write(str(solucao[i])+' ')
    arquivo.write('\n')

    solver.plotarSolucao(folder + ' in ' + sheetName + ' final')
    solver.plotarSolucao(folder + ' in ' + sheetName + ' final com drone', 2)

    sheet1.append((folder, result, endTime - startTime))
    sheet.save(sheetName + '.xlsx')

    print('Final: ', folder) # Imprime o nome da pasta que está sendo lida
arquivo.close()