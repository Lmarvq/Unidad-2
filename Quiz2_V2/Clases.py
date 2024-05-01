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
    

    def AddDictC(self, llave, elem):
        self.__DictCSV[llave] = elem
    def AddDictM(self, llave, elem):
        self.__DictCSV[llave] = elem


    def LeerdatosM(self):
        dir = input("Ingrese la dirección del archivo: ")
        arch = sio.loadmat(dir)
        print(arch.values)
        key = input("Ingrese la llave del archivo a manipular")
        datos = np.array(arch[key])
        return datos and key
    def LeerdatosC(self):
        dir = input("Ingrese la dirección del archivo: ")
        k = input("Ingrese la clave a asignar para este archivo: ")
        dt = pd.read(dir)
        return dt and k
        
    def ExcistanceC(self, elem, llave):
        if elem in self.__DictCSV[llave]:
            return True
        else:
            return False
        #("EL ELEMENTO SELECCIONADO NO CORRESPONDE A LA LLAVE ASIGNADA, O NO EXISTE")
    def ExcistanceM(self, elem, llave):
        if elem in self.__DictMAT[llave]:
            return True
        else:
            return False