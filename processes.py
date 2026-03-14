from validations import get_non_empty_text,get_positive_number

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

def display(inventory):
    print(inventory)

def search(inventory, message) :
    name= get_non_empty_text(message)
    for producto in inventory:
        if producto['Product']==name:
            return producto
    return None

def update_product(inventory, name, price=0, quantity=0):
    for product in inventory:
        if product['Product']== name :
            product['Price_per_unit']= price
            product['Amount']= quantity
            return("update successfully ✅", product)
    return "Any product was found"

def delete_product (inventory, name):
     for product in inventory:
        if product['Product'] == name :
            inventory.remove(product)
            return "The product was remove"
     return "Any product was found"

