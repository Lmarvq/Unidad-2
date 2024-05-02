from Clases import *
def main():
    while True:
        print("¡Bienvenido al Sistema X!\nEscoja la acción a ejecutar.")
        menu = int(input("1-Ingresar archivo Mat\n2-Ingresar archivo CSV\n3-Graficar señal\n4-Mostrar información\n5-Salir\nUsted ingresó: "))
        if menu == 1:
            info = s.LeerdatosM()
            s.AddDictM(info[0], info[1])
            e = ExcistanceM(info[1])
            if e == True:
                print("Operación exitosa")
            else: 
                print(("EL ELEMENTO SELECCIONADO NO CORRESPONDE A LA LLAVE ASIGNADA, O NO EXISTE"))
                #continue
        if menu == 2:
            info = s.LeerdatosC()
            s.AddDictC(info[0], info[1])
            e = ExcistanceC(info[1])
            if e == True:
                print("Operación exitosa")
            else: 
                print(("EL ELEMENTO SELECCIONADO NO CORRESPONDE A LA LLAVE ASIGNADA, O NO EXISTE"))
                continue
        
        if menu == 3:
            g = Graficadora()
            #d = RFG()
            g.G1()
            g.G2()
            g.G3()
            plt.show()
        
        if menu == 4:
            pass
        if menu == 5:
            break

main()