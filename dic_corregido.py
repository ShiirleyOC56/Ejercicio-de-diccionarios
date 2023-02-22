# Se tienen los siguientes diccionarios:
# PROGRAMA PRINCIPAL
"""
Productos = {1:'Pantalones', 2:'Camisas', 3:'Corbatas', 4:'Casacas'}
Precios = {1:200.00, 2:120.00, 3:50.00, 4:350.00}
Stock = {1:50, 2:45, 3:30, 4:15}"""
# Elaborar un programa que muestre los diccionarios, y programar las siguientes acciones:
# [1] Agregar
# [2] Eliminar
# [3] Actualizar
# [4] Salir
"""========================================
Lista de Productos:
========================================
1 Pantalones 200.0 50
2 Camisas 120.0 45
3 Corbatas 50.0 30
4 Casacas 350.0 15
========================================"""
#[1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir
#Elija opción:


class store:
    def __init__(self):
        self.Productos = {1:'Pantalones', 2:'Camisas', 3:'Corbatas', 4:'Casacas'}
        self.Precios = {1:200.00, 2:120.00, 3:50.00, 4:350.00}
        self.Stock = {1:50, 2:45, 3:30, 4:15}
    
    def mostrar(self):
        print("="*40)
        print("Lista de Productos:")
        print("="*40)

        for i in self.Productos:
            print(i,self.Productos[i],self.Precios[i],self.Stock[i])
        
        print("="*40)

    def agregar(self,id,producto,precio,stock):
        self.Productos[id]=producto
        self.Precios[id]=precio
        self.Stock[id]=stock
    
    def eliminar(self,id):
        ids = list(self.Productos.keys())
        if id in ids:
            del self.Productos[id]
            del self.Precios[id]
            del self.Stock[id]
            return True
        else:
            return False
            
    def actualizar(self,id,atributo,nuevo):
        if(atributo == 1):
            self.Productos[id]= nuevo
            return True
        elif (atributo == 2):
            self.Precios[id]= nuevo
            return True
        elif (atributo == 3): 
            self.Stock[id]= nuevo
            return True
        else:
            return False
    
    def salir(self):
        return
    
    def menu(self):
        
        opciones = {1:"Agregar",2:"Eliminar",3:"Actualizar",4:"Salir"}

        opcion = None
        while opcion != 4:
            print("\n MENU DE OPCIONES")
            for i in opciones:
                print("[",i,"]"," ",opciones[i])
        
            opcion = int(input("Ingrese su opcion: "))

            if opcion == 1:
                try:
                    id = int(input("Ingrese el [id] del producto: "))
                    ids = list(self.Productos.keys())

                    if id in ids:
                        print("Ya existe el id")
                    else:
                        producto = input("Ingrese el [nombre] del producto: ")
                        precio = float(input("Ingrese el [precio] del producto: "))
                        stock = int(input("Ingrese el [stock] del producto: "))

                        if precio >= 0 and stock >= 0:                
                            self.agregar(id,producto,precio,stock)
                            print("Se agrego el producto")
                            self.mostrar()
                        else:
                            print("El precio y stock ingresado no pueden ser negativos")
                except:
                    print("¡El id del producto debe ser un numero y el precio un numero decimal, ingrese de nuevo!")
                
            elif opcion == 2:
                try:
                    id = int(input("Ingrese el [id] del producto que desea eliminar: "))
                    
                    res_eliminar = self.eliminar(id)
                    if res_eliminar == True:
                        print("El producto se ha eliminado con exito")
                        self.mostrar()
                    else:
                        print("No existe el producto")
                except:
                    print("¡El id a eliminar debe ser un numero, intente de nuevo!")

            elif opcion == 3:
                try:

                    id = int(input("Ingrese el [id] del producto que desea Actualizar: "))
                    print("\n1. Actualizar producto")
                    print("2. Actualizar precio")
                    print("3. Actualizar stock")

                    atributo = int(input("Elija la opcion a actualizar"))
                    if atributo == 1:
                        producto = input("Ingrese el nuevo [nombre] del producto: ")
                        self.actualizar(id,atributo,producto)
                        self.mostrar()

                    elif atributo == 2:
                        try:
                            precio = float(input("Ingrese el nuevo [precio] del producto: "))
                            if precio >= 0:                
                                self.actualizar(id,atributo,precio)
                                self.mostrar()
                            else:
                                print("El precio ingresado no puede ser negativo")
                        except:
                            print("¡El precio ingresado debe ser numero decimal, intente de nuevo!")

                    elif atributo == 3:
                        try:
                            stock = int(input("Ingrese el [stock] del producto: "))
                            if stock >= 0:
                                self.actualizar(id,atributo,stock)
                                self.mostrar()
                            else:
                                print("El stock ingresado debe ser un numeros positivo")
                        except:       
                            print("¡El stock ingresado debe ser un numero positivo, intente de nuevo!")
                    else:
                        print("Opcion incorrecta)")
                except:
                    print("¡El id del producto debe ser un numero, intente de nuevo!")
               

            elif opcion == 4:
                print("Exit... good bye")
                self.salir()
            
            else:
                print("Opcion incorrecta")


        


s = store()
s.mostrar()
s.menu()
    
