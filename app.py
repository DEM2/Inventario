from archivos import guardar_csv
from servicios import record_sales, mostrar_inventario, buscar_producto, update_product, delete_product
from validations import  get_non_empty_text, get_positive_number

"""try:
   df=pd.read_csv('datos.csv')
   print("Datos Cargados")
except FileNotFoundError:
     df =pd.DataFrame(columns=['Producto', 'Precio', 'Cantidad'])
df.to_csv('datos.csv', index=False)

print(df)"""

inventory=[]
to_continue = True

while to_continue :

 print ("-"* 30)
 print ("      INVENTORY SYSTEM")
 print ("-"* 30)

 print("1. Register")
 print("2. Viw Inventory")
 print("3. Search Product")
 print("4. Update Product Information")
 print("5. Delete a record")
 print("6. Statistics")
 print("7. Save CSV")
 print("8. Upload CSV")
 print("9. Exit")

 try:
     opcion = int(get_positive_number("\n Select a menu option: "))
     if opcion in range(1,10):
        match opcion:
             case 1:
              record_sales(inventory) 
             case 2: 
              mostrar_inventario(inventory)
             case 3:
   
                  result= buscar_producto(inventory, "\n ¿What product are you looking for?: ")
                  if  result != None :
                      print(f"\n This is the information about your search: {result}")
                  else:
                     print("\n No information was found")

             case 4:
                  
                  name= get_non_empty_text("\n Enter the product name: ")
                  new_price = get_positive_number("\n Enter the new price per unit: ")
                  new_quantity = get_positive_number("\n How many units?: ")
                  print(update_product(inventory,name, new_price, new_quantity))
             case 5:
              name = get_non_empty_text("\n Name of the product to be remove: ")
              print(delete_product(inventory, name))
             case 7: 
              print()
             case 9:
              print("closing section ")
              to_continue=False
              break

     else: 
        print("The option is invalid ")
     
 except ValueError :
    print("Invalid value")

 