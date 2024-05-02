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
        key = input("Ingrese la llave del archivo a manipular: ")
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

s = Sistema()
def ExcistanceC( llave):
        if llave in s.ObtenerDictC():
            return True
        else:
            return False
        #("EL ELEMENTO SELECCIONADO NO CORRESPONDE A LA LLAVE ASIGNADA, O NO EXISTE")
def ExcistanceM( llave):
        if llave in s.ObtenerDictM():
            return True
        else:
            return False
    
"""""
def RFG(): #Reshape for graphing
    s = Sistema()
    val = input("Ingrese la clave asociada al archivo MAT que desea graficar")
    if s.ExcistanceM(val) == True:
        info = s.ObtenerDictM()[val]
        canales = info.shape[0]
        puntos = info.shape[1]
        d = [val, ]
        if info.ndim >2:
            epocas = info.shape[2]
            info = np.reshape(info, [canales, puntos*epocas])
            d.append(info)
            return d
        else: 
            d.append(info)
            return d
"""

        
class Graficadora():
    def __init__(self):
        self.__fig = plt.figure()
        self.__G1 = self.__fig.add_subplot(3,2,1)
        self.__G2 = self.__fig.add_subplot(3,2,2)
        self.__G3 = self.__fig.add_subplot(3,2,6)

    def G1(self):
        val = input("Ingrese la clave asociada al archivo MAT que desea graficar: ")
        print(ExcistanceM(val))
        if ExcistanceM(val) == True:
            info = s.ObtenerDictM()[val]
            canales = info.shape[0]
            puntos = info.shape[1]
            if info.ndim >2:
                epocas = info.shape[2]
                info = np.reshape(info, [canales, puntos*epocas])
            else: 
                pass

            print(f"El archivo correspondientes a la clave{val} tiene {canales} disponibles, todos se encuentran dentro de un rango de 0 a {puntos}")
            Sel_H = int(input("¿Cual canal desea escoger para la graficación?:\n Usted escogió:"))
            t = input("Ingrese el título de la gráfica")
            lx = input("Ingrese el nombre del eje X")
            ly = input("Ingrese el nombre del eje Y")
            seccion = np.copy(info)


            self.__G1.hist(seccion[Sel_H, :],  label = (f"Canal{Sel_H}"))
            self.__G1.set_xlabel(lx)
            self.__G1.set_ylabel(ly)
            self.__G1.set_title(t)
            self.__G1.grid(True)
            self.__G1.legend()
            
    
    def G2(self):
        val = input("Ingrese la clave asociada al archivo MAT que desea graficar: ")
        if ExcistanceM(val) == True:
            info = s.ObtenerDictM()[val]
            canales = info.shape[0]
            puntos = info.shape[1]
            if info.ndim >2:
                epocas = info.shape[2]
                info = np.reshape(info, [canales, puntos*epocas])
            else: 
                pass

            print(f"El archivo correspondiente a la clave {val} tiene {canales} disponibles, todos se encuentran dentro de un rango de 0 a {puntos}")
            pmin = int(input("Ingrese el punto inicial de la sección a graficar: "))
            pmax = int(input("Ingrese el punto final de la sección a graficar: "))
            t = input("Ingrese el título de la gráfica")
            lx = input("Ingrese el nombre del eje X")
            ly = input("Ingrese el nombre del eje Y")
            sección = np.copy(info)
            x = np.array(sección[:, pmin:pmax])
            self.__G2.scatter(x,sección[:, pmin:pmax])
            self.__G2.set_xlabel(lx)
            self.__G2.set_ylabel(ly)
            self.__G2.set_title(t)
            self.__G2.grid(True)
            self.__G2.legend()
            

    
    def G3(self):
        val = input("Ingrese la clave asociada al archivo MAT que desea graficar: ")
        if ExcistanceM(val) == True:
            info = s.ObtenerDictM()[val]
            canales = info.shape[0]
            puntos = info.shape[1]
            if info.ndim >2:
                epocas = info.shape[2]
                info = np.reshape(info, [canales, puntos*epocas])
            else: 
                pass

            x = np.random.randn(info.shape[1])
            print(f"El archivo correspondiente a la clave {val} tiene {canales} disponibles, todos se encuentran dentro de un rango de 0 a {puntos}")
            Sel_C = int(input("¿Cual canal desea escoger para la graficación?:\n Usted escogió:"))
            t = input("Ingrese el título de la gráfica")
            lx = input("Ingrese el nombre del eje X")
            ly = input("Ingrese el nombre del eje Y")

            self.__G3.plot(x, info[Sel_C, :], label = (f"Canal{Sel_C}"))
            self.__G3.set_xlabel(lx)
            self.__G3.set_ylabel(ly)
            self.__G3.set_title(t)
            self.__G3.grid(True)
            self.__G3.legend()
            
