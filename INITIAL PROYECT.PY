#Sprint I:
#1)Definir una temática para el trabajo✅
#2)Crear un menú con opciones para que el usuario pueda interactuar✅
#3)Crear un listado inicial de datos que sean string, ✅
#4)si manejan diccionarios también los pueden incluir ✅
#5)Agregar una opción en el menú que permita ver el listado de elementos✅
#Sprint II - desde 28/10:
#Reemplazar el uso de strings por el uso de diccionarios✅
#Pueden usar listas de diccionarios o diccionarios de diccionarios como vimos en la clase del viernes✅
#Arreglar el código para que siga funcionando la opción de ver todos los elementos✅
#Agregar una opción al menú para poder agregar un nuevo elemento✅
#Agregar una opción al menú para poder visualizar los datos filtrados✅
#Sprint III - desde 11/11:
#Agregar un campo de identificación única, como dni o id✅
#Agregar una opción al menú para poder eliminar un elemento✅
#Agregar una opción al menú para poder editar un elemento, alcanza con editar un solo campo
#Agregar más opciones de filtrado al menú




#1) Personal de escuela


#Variables


Sueldo_basico = float ()
Sueldo_calculado = float ()
Antiguedad = float ()
opcion_menu = int()
Nombre = str()
Apellido = str ()
Sueldo = float


#Programa
empleados= {
23618777:{"Nombre"  : "María", "Apellido": "Lopez", "Antiguedad":3, "Sueldo": 12000  },


    18444555:{"Nombre"  : "Rafael", "Apellido": "Suarez", "Antiguedad": 4, "Sueldo": 10000  },


    40333888:{"Nombre"  :"Silvina", "Apellido": "Rodriguez", "Antiguedad": 9, "Sueldo": 20000  },


    27816960:{"Nombre"  :"Elena","Apellido": "Perez", "Antiguedad": 10, "Sueldo": 25000  },


    28444889:{"Nombre"  : "Carlos", "Apellido": "Fernandez", "Antiguedad": 5, "Sueldo": 20000  }
   
}
opcion_menu = 1 # para que entre a la app
while opcion_menu != 0:
    print (""" **** SELECCIONE UNA OPCION ****
    1- Ver lista de personal 📃
    2- Ver datos de empleado 👨‍🦲
    3- Cargar nuevo empleado 💻
    4- Eliminar empleado ❌  
    5- Editar datos del empleado ⌨️
    6- Calcular Sueldo personal 💵    
    0- Salir 👋
    """)
 
    opcion_menu = int(input())
    dni= int
    dni_empleado= int
    match opcion_menu:
        case 1:
            print ("Listado de personal:")
            for empleado in empleados.items():
             print (empleado)
             
           
        case 2:
             dni_empleado = int (input("Ingrese DNI para ver los datos del empleado "))
             if empleados.get(dni_empleado) == None:
              print ("El DNI no corresponde a ningún empleado")
             else:
              print(empleados.get(dni_empleado))
        case 3:
            dni= int (input ("Ingrese el DNI del empleado: "))
            while dni in empleados.keys ():
                    dni= int (input("el DNI ya existe. Vuelva a intentar:  "))
                    continue
            Nombre= input ("Ingrese Nombre del empleado : ")
            Apellido = input ("Ingrese el Apellido: ")
            Antiguedad= float (input("Ingrese Antiguedad: "))
            Sueldo = float(input ("Ingrese Sueldo actual: "))
           
            empleados [dni] = {"Nombre": Nombre, "Apellido": Apellido, "Antiguedad": Antiguedad, "Sueldo": Sueldo}
             
         
            print (f' {dni}: El Nombre es:{empleados [dni]["Nombre"]} {empleados[dni]["Apellido"]}, tiene {empleados[dni]["Antiguedad"]} años de Antiguedad y su Sueldo es de $  {empleados[dni]["Sueldo" ]}')


        case 4:
             print ("Personal a eliminar")
             dni_aeliminar =int (input("Ingrese el DNI a eliminar: "))
             if dni_aeliminar in empleados.keys():
              empleados.pop (dni_aeliminar)
              print("❌❌❌Los datos fueron eliminados ❌❌❌")
              for empleado, datos in empleados.items():
               print (empleado,datos)
                         
             else:
                print ("El DNI no corresponde a un empleado ")    
       
        case 5:
             dni_empleado= int (input ("Ingrese DNI para ver los datos del empleado a modificar "))
             if dni_empleado in empleados.keys():
              Nombre_mod = str (input ("Ingrese el Nombre  correcto: "))
              empleados [dni_empleado] ["Nombre"]= Nombre_mod
              Apellido_mod = str(input ("Ingrese el Apellido  correcto: "))
              empleados [dni_empleado] ["Apellido"]= Apellido_mod
              Antiguedad_mod=float(input ("Ingrese la Antiguedad: "))
              empleados [dni_empleado] ["Antiguedad"]= Antiguedad_mod
              Sueldo_mod=float(input ("Ingrese el Sueldo: "))
              empleados [dni_empleado] ["Sueldo"]= Sueldo_mod
              for empleado, datos in empleados.items():
               print (empleado,datos)
             else:
              print("El DNI no está en la lista de empleados ")
             
               


        case 6:
             
             print ("Ingrese Sueldo basico del empleado")
             Sueldo_basico = float(input ())
   
             print ("Ingrese Antiguedad del empleado")
             Antiguedad = float(input())
   
             if Antiguedad >= 3 and Antiguedad <= 6:
                Sueldo_calculado = Sueldo_basico * 1.15
                print ("el Sueldo es de $", Sueldo_calculado)
             elif Antiguedad > 6:
                Sueldo_calculado = Sueldo_basico * 1.30
                print ("el Sueldo es de $", Sueldo_calculado)
             elif Antiguedad< 3:
                Sueldo_calculado = Sueldo_basico
                print (" el Sueldo es de $", Sueldo_calculado)    
           
        case 0:
            print ("Gracias por usar la aplicación  👋")












