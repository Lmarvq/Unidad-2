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
    def ExcistanceM(self, llave):
        if llave in self.__DictMAT:
            return True
        else:
            return False
    

        
class Graficadora(Sistema):
    def __init__(self):
        super(Sistema).__init__()
        self.__fig = plt.figure()
        self.__G1 = self.__fig.add_subplot(3,2,1)
        self.__G2 = self.__fig.add_subplot(3,2,2)
        self.__G3 = self.__fig.add_subplot(3,2,6)

    def G1(self):
        s = Sistema()
        val = input("Ingrese la clave asociada al archivo MAT que desea graficar")
        if s.ExcistanceM(val) == True:
            info = s.ObtenerDictM()[val]
            canales = info.shape[0]
            puntos = info.shape[1]

            if info.ndim >2:
                epocas = info.shape[2]
                info = np.reshape(info, [canales, puntos*epocas])
            else: 
                pass

            print(f"El archivo correspondientes a la clave{val} tiene {canales} disponibles para la graficación de histogramas, todos se encuentran dentro de un rango de 0 a {puntos}")
            Sel_H = int(input("¿Cual canal desea escoger para la graficación?:\n Usted escogió:"))
            pmin = int(input("Ingrese el punto inicial de la sección a graficar: "))
            pmax = int(input("Ingrese el punto final de la sección a graficar: "))
            arreglo = np.reshape(info, [Sel_H, pmin:pmax])

        
        
