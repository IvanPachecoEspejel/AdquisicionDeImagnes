import os
import requests

RUTA_WEB    = 1     #Flag to identify a web path  
RUTA_LOCAL  = 0     #Flag to identify a local path

import Util as Util

logger = Util.getLogger("Clasifica")

def tipoRuta(sourceRuta = ""):
    ''' Valida si la ruta existe y la clasifica como WEB o LOCAL '''
    
    try:
        requests.get(sourceRuta)
        return RUTA_WEB
    except:
        if os.path.isfile(sourceRuta):
            return RUTA_LOCAL
        raise Exception(Util.getMnsjIdioma("Clasifica", "Error_Ruta_Invalida"))

if __name__ == "__main__":
     
    logger.info("Pruebas Utinaras para el modulo Clasifca")
      
    logger.info("TEST def tipoRuta(sourceRuta = ""):")
    
    logger.info("TEST: RUTA DESCONOCIDA")
    try:
        print(tipoRuta("  "));
        
    except Exception as e:
        logger.error(e)
        
    logger.info("TEST: RUTA WEB")
    try:
        print(tipoRuta("http://blogs.computing.dcu.ie/wordpress/brogand2/wp-content/uploads/sites/183/2015/03/config-parser1.png"))
    except Exception as e:
        logger.error(e)
        
    logger.info("TEST: RUTA LOCAL")
    try:
        print(tipoRuta("/home/ivan/Imagenes/fondos/2_aritradas-sunset.jpg"))
    except Exception as e:
        logger.error(e)
        
        
