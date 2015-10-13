import os

import Util as Util


logger = Util.getLogger("Clasifica")

def tipoRuta(sourceRuta = ""):
    ''' Valida si la ruta existe y la clasifica como WEB o LOCAL '''
    
    protocolos = Util.getMnsjConf('Validacion', 'ProtocolosImgs').split(" ")
    
    for protocolo in protocolos:
        if sourceRuta.startswith(protocolo+"://"):
            return Util.RUTA_WEB
    
    if os.path.sep in sourceRuta or '/' in sourceRuta:
        return Util.RUTA_LOCAL
            
    raise Exception(Util.getMnsjIdioma("Clasifica", "Error_Ruta_Invalida")%sourceRuta)

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
        print(tipoRuta("http://image.slidesharecdn.com/desarrollodeaplicacioneswebii-150422032827-conversion-gate02/95/desarrollo-de-aplicaciones-web-ii-61-638.jpg"))
        print(tipoRuta("http://asdfasdfadf.jpg"))
    except Exception as e:
        logger.error(e)
        
    logger.info("TEST: RUTA LOCAL")
    try:
        print(tipoRuta("/home/ivan/Imagenes/fondos/2_aritradas-sunset.jpg"))
    except Exception as e:
        logger.error(e)
        
        
