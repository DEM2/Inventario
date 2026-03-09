import pandas as pd

try:
   df=pd.read_csv('datos.csv')
   print("Datos Cargados")
except FileNotFoundError:
     df =pd.DataFrame(columns=['Producto', 'Precio', 'Cantidad'])
df.to_csv('datos.csv', index=False)

print(df)
