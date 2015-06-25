import requests
from bs4 import BeautifulSoup

#Funcion que arregla en formato del precio de los productos, dejandolos como un int
def reducePrice(price):
    return int(((("".join(("".join(price)).split())).replace("$","")).replace(".","")).encode())

#Spider que recorrera los sitios web
def spider_lider(url):
    
    #Comienza por tomar uno de los url's a analizar
    for u in url:
        #Extrae todo el codigo fuente del url que sea capaz de ver
        source_code = requests.get(u)
        #Convierte el codigo fuente en texto plano
        plain_text = source_code.text
        #Convierte el documento de texto plano al formato de BS (Beautiful Soup)
        soup = BeautifulSoup(plain_text)
        title = ""
        price = ""

        #Buscar dentro del archivo BS todos las parametros de tipo span, que cumplan con la condicion dentro de los {}
        for link in soup.findAll('span', {'itemprop': 'name'}):
            title = link.string
        #Analogo al anterio, solo que ahora deben ser de tipo em y la condicion dentro de los {} es distinta
        for link in soup.find('em', {'class': 'oferLowPrice fixPriceOferUp  '}):
            price = link.string
        
        #Imprimir el resultado
        print(title + ' = ' + str(reducePrice(price)))
