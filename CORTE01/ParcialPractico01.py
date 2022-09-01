## PARCIAL PRACTICO 01
'''
Este trabajo se debe subir tanto a la plataforma aula virtual como al github individual de cada uno
'''
##1. Encriptación de datos (2.0)
'''
En el siguiente elemento debe realizar un algoritmo que le permita encriptar un mensaje 
'''
def f_encript (str_msg):
    '''
    en el siguiente segmento debe realizar un algoritmo que le permita encriptar el mensaje ingresado por parametro
    :param str_msg: mensaje que se desea encriptar
    :return: str_encript: mensaje encriptado
            s_key: llave que permite desifrar el mensaje
    '''
    str_encript = ''
    s_key = []
    #TODO: realizar el punto 1 del parcial
    return str_encript,s_key

## 2. desencriptar un mensaje (2.0)
'''
En el siguiente elemento debe realizar un algoritmo que le permita desifrar un mensaje encriptado 
'''
def f_decript (str_encript, s_key):
    '''
    algoritmo que permite desisfrar un mensaje encriptado
    :param str_encript: mensaje encriptado
    :param s_key: llave que permite desifrar el mensaje
    :return: mensaje desifrado
    '''
    # TODO: realizar el punto 2 del parcial
    str_msg = ''
    return str_msg
## 3. encontrar una llave (1.0)
'''
en el siguente punto deben desarrollar un algorimo que le permita encontrar la llave de un cifrado haciendo uso de 
una parte del mensaje y la decriptación de este. 
'''

def f_getKey (str_decript, str_msg):
    '''
    código que permite encontrar el cifrado de un mensaje dado un segmento del mensaje
    :param str_decript: mensaje encriptado
    :param str_msg:  mensaje original
    :return s_key: llave que permite desifrar el mensaje
    '''
    s_key = []
    return s_key