import numpy as np

arrCerca = np.array([1,2,3,4,5,4,4])

arrIndici = np.where(arrCerca == 4)
print(arrIndici)

arrSort = np.array([5,6,1,2,4,7,2,8,9,5,7])

arrOrdinamento = np.sort(arrSort)
print(arrOrdinamento)

arrSort_2D = np.array([[5,6,1,2],
                       [4,7,2,8],
                       [9,5,10,7]])
arrOrdinamento_2D = np.sort(arrSort_2D)
print(arrOrdinamento_2D)

arrFiltareStatico = np.array([1,2,3,4])

filtroPari = [False, True, False, True]
arrFiltro = arrFiltareStatico[filtroPari]
print(arrFiltro)

arrFiltareDinamico = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

filtroPari = []

for numero in arrFiltareDinamico:
    if numero % 2 == 0:
        filtroPari.append(True)
    else:
        filtroPari.append(False)
        
arrFiltro1 = arrFiltareDinamico[filtroPari]
print(arrFiltro1)

arrFiltareScociatoria = np.array([1,2,3,4])

filtroPari = arrFiltareScociatoria % 2 == 0
arrFiltro = arrFiltareScociatoria[filtroPari]
print(arrFiltro)