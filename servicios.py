inventario=[]

def agregar_producto(nombre, precio, cantidad):
    inventario.append ({
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad
    })
    return

def mostrar_inventario():
    print(inventario)

def buscar_producto(nombre) :
    for producto in inventario:
        if producto['nombre']== nombre :
            return producto
    return None

def actualizar_producto(nombre, nuevo_precio=None, nueva_cantidad=None):
    for producto in inventario:
        if producto['nombre']== nombre :
            if nuevo_precio!= None : producto['precio']= nuevo_precio
            if nueva_cantidad!= None: producto['cantidad']= nueva_cantidad
            return("producto actualizado", producto)
    return "producto no encontrado"

def eliminar_producto (nombre):
     for producto in inventario:
        if producto['nombre'] == nombre :
            inventario.remove(producto)
            return "el producto ha sido eliminado"
     return "producto no encontrado"