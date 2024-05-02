import numpy as np 
import pandas as pd
import scipy.io as sio
import matplotlib.pyplot as plt

class Sistema():
    def __init__(self):
        self.__DictCSV = {}
        self.__DictMAT = {}

    def ObtenerDictC(self):
        return self.__DictCSV
    def ObtenerDictM(self):
        return self.__DictMAT
    

    def AddDictC(self, elem, llave):
        self.__DictCSV[llave] = elem
    def AddDictM(self, elem, llave):
        self.__DictMAT[llave] = elem


    def LeerdatosM(self):
        dir = input(r"Ingrese la dirección del archivo: ")
        arch = sio.loadmat(dir)
        llaves = sio.whosmat(dir)
        print(llaves)
        key = input("Ingrese la llave del archivo a manipular")
        datos = np.array(arch[key])
        info = [datos, key]
        op1 = int(input("¿Desea visualizar el arreglo? (Forma matricial): 1.Si\n 2.No\n Usted eligió: "))
        if op1 == 1:
            print(datos)
            return info
        else:
            return datos, key
    def LeerdatosC(self):
        dir = input(r"Ingrese la dirección del archivo: ")
        k = input("Ingrese la clave a asignar para este archivo: ")
        dt = pd.read_csv(dir)
        info = [dt, k]
        return info
        
    def ExcistanceC(self, llave):
        if llave in self.ObtenerDictC():
            return True
        else:
            return False
        #("EL ELEMENTO SELECCIONADO NO CORRESPONDE A LA LLAVE ASIGNADA, O NO EXISTE")
    def ExcistanceM(self, elem, llave):
        if elem in self.__DictMAT[llave]:
            return True
        else:
            return False
    