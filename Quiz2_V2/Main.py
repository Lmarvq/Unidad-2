from Clases import *

def main():
    while True:
        print("¡Bienvenido al Sistema X!\nEscoja la acción a ejecutar.")
        sis = Sistema()
        menu = int(input("1-Ingresar archivo Mat\n2-Ingresar archivo CSV\n3-Graficar señal\n4-Mostrar información\n5-Salir\nUsted ingresó: "))
        if menu == 1:
            info = sis.LeerdatosM()
            sis.AddDictM(info[0], info[1])
            e = sis.ExcistanceM(info[0],info[1])
            if e == True:
                print("Operación exitosa")
            else: 
                print(("EL ELEMENTO SELECCIONADO NO CORRESPONDE A LA LLAVE ASIGNADA, O NO EXISTE"))
                continue
        if menu == 2:
            info = sis.LeerdatosC()
            sis.AddDictC(info[0], info[1])
            e = sis.ExcistanceC(info[0],info[1])
            if e == True:
                print("Operación exitosa")
            else: 
                print(("EL ELEMENTO SELECCIONADO NO CORRESPONDE A LA LLAVE ASIGNADA, O NO EXISTE"))
                continue
        if menu == 5:
            break

main()