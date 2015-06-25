from spider import spider
from spider_jumbo import spider_jumbo

__author__ = 'dvillega'
#Arreglo conteniendo los url's a analizar
url = [
    "http://www.lider.cl/walmart/catalog/product/productDetails.jsp?cId=CF_Nivel2_000021&productId=PROD_5913&skuId=5913&pId=CF_Nivel1_000004&navAction=jump&navCount=12",
    "http://www.lider.cl/walmart/catalog/product/productDetails.jsp?cId=CF_Nivel2_000021&productId=PROD_2325&skuId=2325&pId=CF_Nivel1_000004&navAction=jump&navCount=6",
    "http://www.lider.cl/walmart/catalog/product/productDetails.jsp?cId=CF_Nivel2_000021&productId=Prod_672122&skuId=672122&pId=CF_Nivel1_000004&navAction=jump&navCount=7",
    "http://www.lider.cl/walmart/catalog/product/productDetails.jsp?cId=CF_Nivel2_000021&productId=PROD_314572&skuId=314572&pId=CF_Nivel1_000004&navAction=jump&navCount=8",
    "http://www.lider.cl/walmart/catalog/product/productDetails.jsp?cId=CF_Nivel2_000021&productId=Prod_1593211&skuId=1593211&pId=CF_Nivel1_000004&navAction=jump&navCount=8"
    ]
url_jumbo = ["http://www.jumbo.cl/FO/MiCarro"]
#Llamamos al Spider, entregandole el arreglo creado con anterioridad
spider(url)
#spider_jumbo(url_jumbo)
