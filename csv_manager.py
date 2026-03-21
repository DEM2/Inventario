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
      return f"\nInventory stored in: {route}"

   except FileExistsError :
      print("The csv file could not be saved")

def upload(route):
   invalid_rows=0
   csv_upload=[]
   try:
      with open(route,'r', encoding='utf-8') as csvfile:
         result= csv.reader(csvfile)
         header= next(result)
         if(header!=['Product','Price_per_unit','Amount']):
            print("The header of the CSV file does not contain what was expected ")
         else:
            for i, fila in enumerate(result, start=2):
               if len(fila)==3:
                   if not fila[0] or not fila[1] or not fila[2]:
                      invalid_rows+=1
                   else:
                      try:
                         register=dict(zip(header, fila))
                         register['Price_per_unit']=float(register['Price_per_unit'])
                         register['Amount']=int(register['Amount'])

                         if register['Amount']<=0 or register['Price_per_unit']<=0:
                            invalid_rows+=1
                            continue
                         
                         csv_upload.append(register)
                      except ValueError: 
                         invalid_rows+=1
                         continue              
               else: invalid_rows+=1
      return csv_upload, invalid_rows
   except FileNotFoundError:
      print("File not Found")
   
