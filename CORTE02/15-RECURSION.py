#TODO: modificar esta función para que imprima todos los valores de manera ordenada
def f_contar(s_num): # se inicia la función, esta debe tener un parametro que sirva como memoria del sistema
    if s_num < 10: # si el número actual es menor que 10, aumentar en uno y volver a correr la función
        print(s_num, end = " ") #imprimimos el numero que va en secuencia nates de la suma , ejemplo= imprime el uno , cumple con la condiciomn y recorre la funcion , como se sumo a un 2 , imprime el 2 y hace el mismo recorrido y asi sucesivamente hasta cumplir la condicion
        s_num+=1
        return f_contar(s_num) # al correr nuevamente la función, ingresa con s_num + 1 como parametro por lo que cada vez incrementa
    else:
        return s_num # finalmetne cuando se cumple la condición se retorna el valor final
print(f_contar(1))
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
# TODO: modificar la función para que reciba dos parametros, el número inicial y el objetivo
def f_contar(s_num,s_objeto): # se inicia la función, esta debe tener 2  parametros que sirvan como memoria del sistema
    if s_num < s_objeto: # si el numero actual dado por el parametro es menor que el numero dado por el otro parametro , entonces realiza el recorrido en la funcion
        print(s_num, end = " ") #imprimimos el numero que va en secuencia nates de la suma , ejemplo= imprime el uno , cumple con la condiciomn y recorre la funcion , como se sumo a un 2 , imprime el 2 y hace el mismo recorrido y asi sucesivamente hasta cumplir la condicion
        s_num+=1
        return f_contar(s_num,s_objeto) # al correr nuevamente la función, ingresa con s_num + 1 como parametro por lo que cada vez incrementa
    else:
        return s_num # finalmetne cuando se cumple la condición se retorna el valor final
print(f_contar(1,12))
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
# TODO: modificar la función para que reciba 3 parametros el número inicial, el objetivo y los pasos entre números
def f_contar(s_num,s_objeto,s_pasos): # se inicia la función, esta debe tener 2  parametros que sirvan como memoria del sistema
    if s_num < s_objeto: # si el numero actual dado por el parametro es menor que el numero dado por el otro parametro , entonces realiza el recorrido en la funcion
        print(s_num, end = " ")#imprimimos el numero que va en secuencia nates de la suma , ejemplo= imprime el uno , cumple con la condiciomn y recorre la funcion , como se sumo a un 2 , imprime el 2 y hace el mismo recorrido y asi sucesivamente hasta cumplir la condicion
        s_num+=s_pasos  #se utiliza el parametro incial para realziar el recorrido y se le pide que sea la suma igual al parametro de los pasos
        return f_contar(s_num,s_objeto,s_pasos) # al correr nuevamente la función, ingresa con s_num + 1 como parametro por lo que cada vez incrementa
    else:
        return s_num # finalmetne cuando se cumple la condición se retorna el valor final
print(f_contar(1,12,2))
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# TODO: REVERSION DE LOS NUMEROS
def f_contar(s_num,s_objeto,s_pasos): # se inicia la función, esta debe tener 2  parametros que sirvan como memoria del sistema
    if s_num > s_objeto: # si el numero actual dado por el parametro es mayor que el numero dado por el otro parametro , entonces realiza el recorrido en la funcion
        print(s_num, end = " ")#imprimimos el numero que va en secuencia nates de la suma , ejemplo= imprime el uno , cumple con la condiciomn y recorre la funcion , como se sumo a un 2 , imprime el 2 y hace el mismo recorrido y asi sucesivamente hasta cumplir la condicion
        s_num-=s_pasos  #se utiliza el parametro incial para realziar el recorrido y se le pide que sea la suma igual al parametro de los pasos
        return f_contar(s_num,s_objeto,s_pasos) # al correr nuevamente la función, ingresa con s_num + 1 como parametro por lo que cada vez incrementa
    else:
        return s_num # finalmetne cuando se cumple la condición se retorna el valor final
print(f_contar(12,1,1))
#TODO:Torre de hanoi
def Torre(ficha,A1,B2,C3):
    if ficha ==1: #Estblecemos la sumatoria de una ficha a otra como es 1,2,3....
        print("la ficha se movera a ",A1,B2) #Aca Imprimiremos la ubicacion de la ficha de A1 a B2
        return #mientras colocamos una ficha a un espacio vacio colocamos otra ficha un espacio con fichas mayores a esta
    Torre(ficha - 1,A1,B2,C3) #Dentro de esta funcion lo que intentaremos hacer sera la ficha puesta le contaremos como le restaremos la ubicacion de cada una de estas
    print("la ficha ",ficha,"se movera ",A1 ,"a",C3) #Aca Imprimiremos el dialogo de como se movera de ubicacion la ficha
    Torre(ficha - 1,C3,B2,A1)#Dentro de esta funcion lo que intentaremos hacer sera la ficha puesta le contaremos como le restaremos la ubicaci pero teniendo en cuenta como esta estara alrevez
Torre(3,"A1","B2","C3") #Dentro de este ubicaremos el numero de fichas  jugar y la ubicacion a las cuales las fichas se moveran en las que estan definidas como A1,B2,C3
