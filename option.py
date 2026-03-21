from processes import *
from csv_manager import upload,save_csv
from validations import get_non_empty_text,get_positive_number

def option_1 (inventory):
    record_sales(inventory) 

def option_2(inventory):
     if not inventory:
         print("The inventory is empty")
     else: 
         display(inventory)

def option_3(inventory):
    result= search(inventory, "\n ¿What product are you looking for?: ")
    if  result != None :
         print(f"\n This is the information about your search: {result}")
    else:
         print("\n No information was found")

def option_4(inventory):
    name= get_non_empty_text("\n Enter the product name: ")
    new_price = get_positive_number("\n Enter the new price per unit: ")
    new_quantity = get_positive_number("\n How many units?: ")
    print(update_product(inventory,name, new_price, new_quantity))

def option_5(inventory):
     name = get_non_empty_text("\n Name of the product to be remove: ")
     print(delete_product(inventory, name))

def option_7(inventory):
      print(save_csv(inventory, "inventory.csv"))

def option_8(inventory):
    imported_inventory, contador = upload("new_inventory.csv")
     
    validate = True
    while validate:
        option = input(
        "\n Would you like to overwrite the current inventory? Y for yes or N for no: "
         ).strip().upper()
        if option in ["Y", "N"]:
            validate=False
        else:
            print("\n Please enter Y or N")
    
    if option == "Y":
        inventory.clear()
        inventory.extend(imported_inventory)
        
    else:
        inventory_index = {item['Product']: item for item in inventory}

        for item in imported_inventory:
            product = item['Product']

            if product in inventory_index:
                inventory_index[product]['Price_per_unit'] = item['Price_per_unit']
                inventory_index[product]['Amount'] = item['Amount']
            else:
                inventory.append(item)
                
    print("\nLos datos se cargaron correctamente")
    print("La cantidad de filas inválidas es:", contador, "\n")