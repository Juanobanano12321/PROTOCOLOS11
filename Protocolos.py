import os

a = 0
print('''

INGRESA UNA DE LAS SIGUIENTES OPCIONES: \n
''')


def menu():
    print('''
    OPCIONES:
    
    [1] CREAR PROTOCOLO
    [2] AGREGAR PASOS Y SUBPASOS
    [3] BORRAR PROTOCOLO
    [4] VISUALIZAR PROTOCOLO

''')
def pasos():
    esc = "S"
    while (esc == "s" or esc == "S"):
        a =+ 1

        print("\n")
        instruccion = input("ESCRIBA LA INSTRUCCION:\n ")
        protocolo.write(str(a) + "-" + instruccion + "\n")

        sub = input("¿DESEA AGREGAR UNA SUBINSTRUCCION? s/n\n")
        if (sub == "s" or sub == "S"):
            cantsub = int(input("¿CUÁNTAS SUBINSTRUCCIONES DESEA AGREGAR?"))
            for i in range(cantsub):
                subinstruccion = input("ESCRIBA LA SUBINSTRUCCION : \n")
                protocolo.write("    " + str(a) + "."+str(i)+"-" + subinstruccion + "\n")

        esc = input("¿DESEA ESCRIBIR LA SIGUIENTE INSTRUCCION? s/n\n ")
    protocolo.close()

menu()
bandera = "S"
if (bandera == "S" or bandera == "s"):

    print("ESCRIBE EL NÚMERO DE LA OPCION: \n")
    while (bandera == "s" or bandera == "S"):
        opcion = int(input("¿CUÁL DESEA ELEGIR?"))

        if opcion == 1:
            print("\n")
            name = input("ESCRIBE EL NOMBRE DE TU PROTOCOLO: ")
            protocolo = open(name + ".txt", 'w')
            protocolo.write(name + '''\n \n''')
            pasos()

        elif opcion == 2:
            print("\n")

            name = input("ESCRIBE EL NOMBRE DEL PROTOCOLO PARA AGREGARLE PASOS\n")
            protocolo = open(name + ".txt", 'a')

            pasos()


        elif opcion == 3:
            print("\n")
            name = input("ESCRIBE EL NOMBRE DEL PROTOCOLO A BORRAR: \n")
            os.remove(name + ".txt")

        elif opcion == 4:
            print("\n")
            name = input("NOMBRE DEL PROTOCOLO QUE DESEA VER: \n")
            protocolo = open(name + ".txt")
            print(protocolo.read())
            protocolo.close()

        bandera = input("¿DESEA REALIZAR ALGUN OTRO CAMBIO? s/n\n ")
        if (bandera == "s" or bandera == "S"):
            menu()
            continue
        else:
            break
else:
    print(" ")
