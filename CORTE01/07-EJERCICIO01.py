#PUNTO 1
def f_suma (a,b): #utilizamos una función definida como "f_suma" y las variables a,b
 print(a+b) #utilizamos la funcion print para imprimir el mensaje y colocamos la variable a y b con el simbolo de la suma 
 return(a+b) # se utiliza para establecer el resultado (o valor de retorno) de una función o para llamar la funcion.
assert f_suma(3,5) == 8 #el assert se utliza como metodo de validacion y asignacion de los valores a las variables 
assert f_suma(3,-5) == -2
assert f_suma(-7,-5) == -12

#PUNTO 2

def f_mod(a,b): #utilizamos una función definida como "f_mod" y las variables a,b
    print(b%a) #utilizamos la funcion print para imprimir el mensaje y colocamos la variable a,b invertida puesto que se quiere saber el modulo de B con A el simbolo del modulo "%"
    return(b%a) #se utiliza para establecer el resultado (o valor de retorno) de una función o para llamar la funcion
assert f_mod(3,5) #el assert se utliza como metodo de validacion y asignacion de los valores a las variables
assert f_mod(3,-5)
assert f_mod(4,10)
