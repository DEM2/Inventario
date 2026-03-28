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
      # By default, The inventory.csv file is where I store the information when the user selects the option 
      print(save_csv(inventory, "inventory.csv"))

# option : Upload CSV
def option_8(inventory):
    # By default, The new_inventory.csv file is where the information I want to upload is located 
    imported_inventory, contador = upload("new_inventory.csv")
     
    validate = True
    while validate:
        option = input(
        "\n If you want to overwrite the inventory information with the new data, type 'R'; if, on the other hand, you want to merge the information, type 'F':  "
         ).strip().upper()
        if option in ["R", "F"]:
            validate=False
        else:
            print("\n Please enter R or F")
    
    if option == "R":
        inventory.clear()
        inventory.extend(imported_inventory)
        print("\nThe replacement was successfully completed ✅")

    else:
        inventory_index = {item['Product']: item for item in inventory}

        for item in imported_inventory:
            product = item['Product']

            if product in inventory_index:
                inventory_index[product]['Price_per_unit'] = item['Price_per_unit']
                inventory_index[product]['Amount'] = item['Amount']
            else:
                inventory.append(item)
        print("\nThe data was successfully merged ✅")
                
    print(f" The number of invalid rows was: {contador} \n")
    print("*"*30)
    option_2(inventory)
    