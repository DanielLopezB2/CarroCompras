carrito = {}


def agregar_producto():

    print ("||| AGREGAR PRODUCTO |||\n")
    nombre = input("Nombre del producto: ")

    if nombre.capitalize() in carrito:

        print ("||| El producto ya existe |||")

        nombre = input("Nombre del producto: ")

        if nombre.capitalize() not in carrito:
            precio = float(input("Precio: $"))
            carrito[nombre.capitalize()] = precio

            nuevo = carrito.setdefault(nombre, precio)

    else:

        precio = float(input("Precio: $"))
        carrito[nombre.capitalize()] = precio

        

    print()

def borrar_producto():

    print ("||| QUITAR PRODUCTO |||\n")
    nombre = input("Nombre del producto que desea quitar: ")

    try:

        del carrito[nombre.capitalize()]
        print()
        print("||| Producto eliminado |||\n")

    except KeyError:

        print()
        print("El producto que está intentado quitar, no existe \n")


def modificar_producto():

    print ("||| MODIFICAR PRODUCTO |||\n")
    nombre = input("Nombre del producto que desea modificar: ")

    if nombre.capitalize() in carrito:

        del carrito[nombre.capitalize()]

        nombre = input("Actualizar nombre del producto: ")
        precio = float(input("Precio: $"))

        carrito[nombre.capitalize()] = precio

        print("||| Producto modificado |||\n")

    else:

        print()
        print("El producto que está intentado modificar, no existe \n")

def ver_carrito():

    print ("||| CARRITO DE COMPRAS TIENDAPP |||\n")

    if len(carrito) == 0:

        print("El carrito está vacío :(")

    

    for key in carrito:

        print("Producto: ",key, "- Precio: $",carrito[key])

    print()

    total = 0

    for producto in carrito:

        total += carrito[producto]

    print(f"Total: ${total}")

    print()
    

def pagar():

    print ("||| PAGAR |||\n")
    
    total = 0

    for producto in carrito:

        total += carrito[producto]

    print(f"Total: ${total}")

    print()


print()
print("╬╬╬╬╬╬╬╬╬╬ Bienvenidos a TiendApp ╬╬╬╬╬╬╬╬╬╬".upper())
print()

while True:
    
	try:
		print("1.- AGREGAR PRODUCTO")
		print("2.- QUITAR PRODUCTO")
		print("3.- MODIFICAR PRODUCTO")
		print("4.- VER CARRITO")
		print("5.- PAGAR")
		print("6.- SALIR")

		opcion = int(input("Seleccione una opción: "))
		print()
  
  
	except ValueError:
     
		print("¡¡¡¡ FAVOR INGRESAR SOLO NUMEROS !!!\n")
  
	else:
		
		if opcion < 0 or opcion > 6:
			print ("¡¡¡ NO ES UNA OPCION VALIDA !!!\n")
			continue
		
		if opcion == 1:
			agregar_producto()

		elif opcion == 2:
			borrar_producto()

		elif opcion == 3:
			modificar_producto()
   
		elif opcion == 4:
			ver_carrito()
        
		elif opcion == 5:
			pagar()

		else:
			break


print("||| ||| ||| ||| ||| ||| ||| ||| ||| ||| ||| ||| ||| ||| ||| |||")
print("|||||||||||| GRACIAS POR COMPRAR EN LA TIENDAPP ||||||||||||")
print("||||||||||||||||||||| HASTA LA PROXIMA |||||||||||||||||||||||")
print("||| ||| ||| ||| ||| ||| ||| ||| ||| ||| ||| ||| ||| ||| ||| |||\n")
