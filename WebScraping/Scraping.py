'''
Created on 29 oct. 2019

@author: antonny
'''
from bs4 import BeautifulSoup
import requests
from conexion import mydb


URL = "https://listado.mercadolibre.com.co/celular-xiaomi#D[A:Celular%20Xiaomi]"

# Petición a la web
req = requests.get(URL)

# Comprobamos que la petición nos devuelve un Status Code = 200
status_code = req.status_code
if status_code == 200:

    # Pasando el contenido HTML de la web a un objeto BeautifulSoup()
    html = BeautifulSoup(req.text, "html.parser")

    # Obtenemos el listado del la busqueda en los li
    contenido = html.find_all('li', {'class': 'results-item highlighted article stack product'})

    # Recorrer todo el contenido para extraer el titulo y el precio
    for i, cont in enumerate(contenido):
        # Con el método "getText()" no retorna el HTML
        precio = cont.find('span', {'class': 'price__fraction'}).getText()
        titulo = cont.find('h2', {'class': 'item__title list-view-item-title'}).getText()
        vendidos = cont.find('div', {'class':'item__condition'}).getText()
        envio = cont.find('p', {'class': 'stack-item-info'}).getText()

        print (i + 1, titulo, precio,vendidos, envio)  
        
    #def update(self):
        sql = "insert into consultas (producto, precio, vendidos, envio) values (?, ?, ?, ?)" 
        mycursor = mydb.cursor(prepared=True)
        val = (titulo, precio, vendidos, envio)
        result = mycursor.execute(sql, val)

        mycursor.execute(sql, val)
        mydb.commit()

        print(mycursor.rowcount, "Insercion satisfactoria.")
        
        def consultar(self):
            sql = mycursor = mydb.cursor()
            mycursor.execute("Select * from consultas")
            mycursor = mydb.cursor(prepared = True)    
            for datos in mycursor:
                 print(datos) 

#else:
    #print (status_code)