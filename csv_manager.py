import csv

def save_csv(inventory, route, header=True):
   if not inventory: 
      print("No information has been saved")
      return
   try:
      with open(route,'w', newline='', encoding='utf-8') as csvfile:
         fieldnames=['Product','Price_per_unit','Amount']
         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
         if header : writer.writeheader()
         writer.writerows(inventory)
      return f"Inventory stored in: {route}"

   except FileExistsError :
      print("The csv file could not be saved")

