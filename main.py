from spider_lider import spider_lider
__author__ = 'dvillega'
#Arreglo conteniendo los url's a analizar
url_arrozpreparado = [
    "http://www.lider.cl/walmart/catalog/product/productDetails.jsp?cId=CF_Nivel3_000027&productId=PROD_1851946&skuId=1851946&pId=CF_Nivel1_000003&navAction=jump&navCount=6",
    "http://www.lider.cl/walmart/catalog/product/productDetails.jsp?cId=CF_Nivel3_000027&productId=PROD_310604&skuId=310604&pId=CF_Nivel1_000003&navAction=jump&navCount=6",
    "http://www.lider.cl/walmart/catalog/product/productDetails.jsp?cId=CF_Nivel3_000027&productId=PROD_956437&skuId=956437&pId=CF_Nivel1_000003&navAction=jump&navCount=6",
    "http://www.lider.cl/walmart/catalog/product/productDetails.jsp?cId=CF_Nivel3_000027&productId=PROD_5124244&skuId=5124244&pId=CF_Nivel1_000003&navAction=jump&navCount=6",
    "http://www.lider.cl/walmart/catalog/product/productDetails.jsp?cId=CF_Nivel3_000027&productId=PROD_1747164&skuId=1747164&pId=CF_Nivel1_000003&navAction=jump&navCount=6",
    "http://www.lider.cl/walmart/catalog/product/productDetails.jsp?cId=CF_Nivel3_000027&productId=PROD_335492&skuId=335492&pId=CF_Nivel1_000003&navAction=jump&navCount=6",
    "http://www.lider.cl/walmart/catalog/product/productDetails.jsp?cId=CF_Nivel3_000027&productId=PROD_310888&skuId=310888&pId=CF_Nivel1_000003&navAction=jump&navCount=6",
    "http://www.lider.cl/walmart/catalog/product/productDetails.jsp?cId=CF_Nivel3_000027&productId=PROD_1156089&skuId=1156089&pId=CF_Nivel1_000003&navAction=jump&navCount=6",
    "http://www.lider.cl/walmart/catalog/product/productDetails.jsp?cId=CF_Nivel3_000027&productId=PROD_1747812&skuId=1747812&pId=CF_Nivel1_000003&navAction=jump&navCount=6",
    "http://www.lider.cl/walmart/catalog/product/productDetails.jsp?cId=CF_Nivel3_000027&productId=PROD_5124237&skuId=5124237&pId=CF_Nivel1_000003&navAction=jump&navCount=6",
    "http://www.lider.cl/walmart/catalog/product/productDetails.jsp?cId=CF_Nivel3_000027&productId=PROD_956000&skuId=956000&pId=CF_Nivel1_000003&navAction=jump&navCount=6",
    "http://www.lider.cl/walmart/catalog/product/productDetails.jsp?cId=CF_Nivel3_000027&productId=PROD_955980&skuId=955980&pId=CF_Nivel1_000003&navAction=jump&navCount=6",
    "http://www.lider.cl/walmart/catalog/product/productDetails.jsp?cId=CF_Nivel3_000027&productId=PROD_334266&skuId=334266&pId=CF_Nivel1_000003&navAction=jump&navCount=6",
    "http://www.lider.cl/walmart/catalog/product/productDetails.jsp?cId=CF_Nivel3_000027&productId=PROD_955997&skuId=955997&pId=CF_Nivel1_000003&navAction=jump&navCount=6",
    "http://www.lider.cl/walmart/catalog/product/productDetails.jsp?cId=CF_Nivel3_000027&productId=PROD_960106&skuId=960106&pId=CF_Nivel1_000003&navAction=jump&navCount=6",
    "http://www.lider.cl/walmart/catalog/product/productDetails.jsp?cId=CF_Nivel3_000027&productId=PROD_3926673&skuId=3926673&pId=CF_Nivel1_000003&navAction=jump&navCount=6",
    "http://www.lider.cl/walmart/catalog/product/productDetails.jsp?cId=CF_Nivel3_000027&productId=PROD_958189&skuId=958189&pId=CF_Nivel1_000003&navAction=jump&navCount=6",
    "http://www.lider.cl/walmart/catalog/product/productDetails.jsp?cId=CF_Nivel3_000027&productId=PROD_1746549&skuId=1746549&pId=CF_Nivel1_000003&navAction=jump&navCount=6",
    "http://www.lider.cl/walmart/catalog/product/productDetails.jsp?cId=CF_Nivel3_000027&productId=PROD_1239782&skuId=1239782&pId=CF_Nivel1_000003&navAction=jump&navCount=6",
    "http://www.lider.cl/walmart/catalog/product/productDetails.jsp?cId=CF_Nivel3_000027&productId=PROD_957885&skuId=957885&pId=CF_Nivel1_000003&navAction=jump&navCount=6",
    "http://www.lider.cl/walmart/catalog/product/productDetails.jsp?cId=CF_Nivel3_000027&productId=PROD_1870053&skuId=1870053&pId=CF_Nivel1_000003&navAction=jump&navCount=26",
    "http://www.lider.cl/walmart/catalog/product/productDetails.jsp?cId=CF_Nivel3_000027&productId=PROD_3926635&skuId=3926635&pId=CF_Nivel1_000003&navAction=jump&navCount=26",
    "http://www.lider.cl/walmart/catalog/product/productDetails.jsp?cId=CF_Nivel3_000027&productId=PROD_881043&skuId=881043&pId=CF_Nivel1_000003&navAction=jump&navCount=26",
    "http://www.lider.cl/walmart/catalog/product/productDetails.jsp?cId=CF_Nivel3_000027&productId=PROD_5893164&skuId=5893164&pId=CF_Nivel1_000003&navAction=jump&navCount=26",
    "http://www.lider.cl/walmart/catalog/product/productDetails.jsp?cId=CF_Nivel3_000027&productId=Prod_225052&skuId=225052&pId=CF_Nivel1_000003&navAction=jump&navCount=26",
    "http://www.lider.cl/walmart/catalog/product/productDetails.jsp?cId=CF_Nivel3_000027&productId=PROD_5893140&skuId=5893140&pId=CF_Nivel1_000003&navAction=jump&navCount=26",
    "http://www.lider.cl/walmart/catalog/product/productDetails.jsp?cId=CF_Nivel3_000027&productId=PROD_5893157&skuId=5893157&pId=CF_Nivel1_000003&navAction=jump&navCount=26",
    "http://www.lider.cl/walmart/catalog/product/productDetails.jsp?cId=CF_Nivel3_000027&productId=PROD_1789652&skuId=1789652&pId=CF_Nivel1_000003&navAction=jump&navCount=26",
    "http://www.lider.cl/walmart/catalog/product/productDetails.jsp?cId=CF_Nivel3_000027&productId=PROD_5126194&skuId=5126194&pId=CF_Nivel1_000003&navAction=jump&navCount=26",
    "http://www.lider.cl/walmart/catalog/product/productDetails.jsp?cId=CF_Nivel3_000027&productId=PROD_4735212&skuId=4735212&pId=CF_Nivel1_000003&navAction=jump&navCount=26",
    "http://www.lider.cl/walmart/catalog/product/productDetails.jsp?cId=CF_Nivel3_000027&productId=PROD_5105601&skuId=5105601&pId=CF_Nivel1_000003&navAction=jump&navCount=26",
    "http://www.lider.cl/walmart/catalog/product/productDetails.jsp?cId=CF_Nivel3_000027&productId=Prod_1348231&skuId=1348231&pId=CF_Nivel1_000003&navAction=jump&navCount=26",
    "http://www.lider.cl/walmart/catalog/product/productDetails.jsp?cId=CF_Nivel3_000027&productId=PROD_6009991&skuId=6009991&pId=CF_Nivel1_000003&navAction=jump&navCount=26",
    "http://www.lider.cl/walmart/catalog/product/productDetails.jsp?cId=CF_Nivel3_000027&productId=PROD_5659951&skuId=5659951&pId=CF_Nivel1_000003&navAction=jump&navCount=26",
    "http://www.lider.cl/walmart/catalog/product/productDetails.jsp?cId=CF_Nivel3_000027&productId=PROD_3031612&skuId=3031612&pId=CF_Nivel1_000003&navAction=jump&navCount=26"
    ]
#Llamamos al Spider, entregandole el arreglo creado con anterioridad
spider_lider(url_arrozpreparado)
#spider_jumbo(url_jumbo)
