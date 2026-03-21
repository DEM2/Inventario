from menu import menu
from validations import get_positive_number

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
     if opcion in menu:
        menu[opcion](inventory)
     elif opcion==9:
        print("\nClosing section... ")
        to_continue=False
     else: 
        print("The option is invalid ")
     
 except ValueError :
    print("Invalid value")

 