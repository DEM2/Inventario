from validations import get_non_empty_text,get_positive_number

# This feature is used to record each sale in the inventory list
def  record_sales (inventory):

    product = get_non_empty_text("\n Enter the product name: ")
    price = get_positive_number ("\n Enter the price per unit: ")
    quantity= get_positive_number("\n How many units?: ")
                
    inventory.append({
        'Product': product,
        'Price_per_unit': float(price),
        'Amount': quantity
        })
            
    print("\n Sale recorded successfully ✅")

# This feature allows you to view all records 
def display(inventory):
    print("\n INVENTARIO")
    print("="*20)
    for product in inventory:
        print(f" Product: {product['Product']} | Price per unit: {product['Price_per_unit']} | Amount: {product['Amount']}")
        
# This feature is used to search for a product
def search(inventory, message) :
    name= get_non_empty_text(message)
    for producto in inventory:
        if producto['Product']==name:
            return producto
    return None

# This feature is used to update a registered product 
def update_product(inventory, name, price=0, quantity=0):
    for product in inventory:
        if product['Product']== name :
            product['Price_per_unit']= price
            product['Amount']= quantity
            return(f"\n {product['Product']} update successfully ✅")
    return "\n Any product was found"

# This feature is used to remove a product from inventory 
def delete_product (inventory, name):
     for product in inventory:
        if product['Product'] == name :
            inventory.remove(product)
            return "\n The product was remove"
     return "\n Any product was found"

# This feature allows you to calculate statistics for inventory records 
def statistics (inventory):
     total=0
     quantity=0
     
     for product in inventory:
       total+= product['Price_per_unit'] * product['Amount']
       quantity+= product['Amount']

     expensive_product=max(inventory, key= lambda product: product['Price_per_unit'])
     larger_inventory=max(inventory, key=lambda product: product['Amount'])

     return total, quantity, expensive_product, larger_inventory
     