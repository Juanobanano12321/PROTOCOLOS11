
import os

a=0
print('''

INGRESA UNA DE LAS SIGUIENTES OPCIONES
''')
def menu():
    print('''
-------------------------
    Opciones
    1.-CREAR
    2.-AGREGAR
    3.-BORRAR
    4.-VISUALIZAR
-------------------------
''')
menu()
bandera=input("¿DESEA REALIZAR ALGUNA DE LAS OPCIONES DADAS? s/n ")
if (bandera == "N" or bandera == "s" or bandera == "S" or bandera == "n"):

    print("ESCRIBE EL NÚMERO")
    while (bandera == "s" or bandera == "S"):
        opcion=int(input("¿CUÁL DESEA ELEGIR?"))
        
        if opcion == 1:
            print("-----------------")
            name=input("ESCRIBE EL NOMBRE DE TU PROTOCOLO: ")
            protocolo = open(name + ".txt", 'w')
            protocolo.write(name+ '''\n \n''')
            
            esc=input("¿DESEA ESCRIBIR LAS INSTRUCCIONES? s/n ")
            while (esc == "s" or esc=="S"):
                a=a+1

                print("-------------")
                instruccion=input("ESCRIBA LA "+str(a)+"° INSTRUCCION: ")
                protocolo.write(str(a) +"-"+ instruccion + '''\n''')
                
                sub=input("¿DESEA ESCRIBIR UNA SUBINSTRUCCION? s/n")
                
                if (sub == "s" or sub=="S"):
                    
                    subinstruccion=input("ESCRIBA LA SUBINSTRUCCION ")
                    protocolo.write("    "+str(a)+".1-"+subinstruccion+'''\n''')
                    
                esc=input("¿DESEA ESCRIBIR LA SIGUIENTE INSTRUCCION? s/n ")
            print("HEMOS TERMINADO EL PROTOCOLO")
            protocolo.close()
            
        elif  opcion == 2:
            print("-----------------")
            
            name=input("ESCRIBE EL NOMBRE DEL PROTOCOLO PARA AGREGAR PASOS ")
            protocolo = open(name + ".txt",'a')
            
            esc=input("¿DESEA ESCRIBIR UNA INSTRUCCION? s/n ")
            while (esc == "s" or esc=="S"):

                print("-------------")
                instruccion=input("ESCRIBA LA INSTRUCCION ")
                protocolo.write("-"+ instruccion + '''\n''')
                
                sub=input("¿DESEA ESRIBIR UNA SUBINSTRUCCION? s/n")
                
                if (sub == "s" or sub=="S"):
                    
                    subinstruccion=input("ESCRIBA LA SUBINSTRUCCION ")
                    protocolo.write(".   -"+subinstruccion+'''\n''')
                    
                esc=input("¿DESEA ESCRIBIR LA SUBINSTRUCCION? s/n ")
            print("hemos terminado el cambio en el protocolo "+name)
            protocolo.close()
            
            
        elif  opcion == 3:
            print("-----------------")
            name=input("ESCRIBE EL NOMBRE DEL PROTOCOLO A BORRAR: ")
            os.remove(name + ".txt")
            print("EL PROTOCOLO HA SIDO ELIMINADO")
            
        elif  opcion == 4:
            print("-----------------")
            name=input("NOMBRE DEL PROTOCOLO QUE DESEA VER: ")
            protocolo = open(name + ".txt")
            print(protocolo.read())
            protocolo.colse()
                   
        bandera=input("¿DESEA REALIZAR LAS OPCIONES DADAS? s/n ")
        if (bandera=="s" or bandera=="S"):
            continue
        else:
            break
    
else:
    print("Fin")
