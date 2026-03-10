import csv

def guardar_csv(inventario, ruta, incluir_header=True):

   if not inventario: 
      print("No se ha agregado ninguna informmacion")
      return
   try:
    with open(ruta,'w', newline=',', encoding='utf-8')as file:
        writer = csv.DictWriter(file)
        writer.writeheader()
        writer.writerows(inventario)
    return "Inventario guardado en: {ruta}"

   except FileExistsError :
      print("No se pudo guardar el csv")

