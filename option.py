from processes import *
from csv_manager import upload,save_csv
from validations import get_non_empty_text,get_positive_number

# option : Register
def option_1 (inventory):
    record_sales(inventory) 

# option : Viw Inventory
def option_2(inventory):
     if not inventory:
         print("The inventory is empty")
     else: 
         display(inventory)

# option : Search Product
def option_3(inventory):
    result= search(inventory, "\n ¿What product are you looking for?: ")
    if  result != None :
         print(f"\n This is the information about your search:")
         print(f" Product: {result['Product']} | Price per unit: {result['Price_per_unit']} | Amount: {result['Amount']}")
    else:
         print("\n No information was found")

# option : Update Product Information
def option_4(inventory):
    name= get_non_empty_text("\n Enter the product name: ")
    new_price = get_positive_number("\n Enter the new price per unit: ")
    new_quantity = get_positive_number("\n How many units?: ")
    print(update_product(inventory,name, new_price, new_quantity))

# option : Delete a record
def option_5(inventory):
     name = get_non_empty_text("\n Name of the product to be remove: ")
     print(delete_product(inventory, name))

# option : Statistics
def option_6(inventory):
   if inventory:
       total, quantity, expensive_product, larger_inventory = statistics(inventory)
       print("\n STATISTICS")
       print("="*20)
       print(f" Total for all units: {quantity}")
       print(f" Total sales: {total}")
       print(f" Most expensive product:  Product: {expensive_product['Product']} | Price: {expensive_product['Price_per_unit']}")
       print(f" The product with the highest inventory:  Product: {larger_inventory['Product']} | Amount: {larger_inventory['Amount']}")
   else:
       print("\n The inventory is empty")

# option : Save CSV"
def option_7(inventory):
      print(save_csv(inventory, "inventory.csv"))

# option : Upload CSV
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
                
    print("\n The data has been uploaded successfully ✅")
    print(f" The number of invalid rows was: {contador} \n")