#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#TODO:CONEJOS , SECUENCIA DE FIBONACCI
def fibo(s_num): #se crea la funcion
    if s_num < 2: #si el numero incial es menor que dos se cumple la condicion y continua
        return(s_num) #retorna el numero
    return fibo(s_num-1)+fibo(s_num-2) #dicho numero anteriormente retornado entra en la "formula de la sucecion de fibonnaci" y se retorna
    if s_num: #simplemente meti el s_num en un bucle para que haga el recorrido la cantidad de veces que quiero los pasos , en este caso serian 13
        return (s_num) # lo retorna y al cumplir el s_num , que es valor deseado se finaliza y ya
print(f" la cantidad de pares de crias que pued eponer a la venta el granjero a lo largo de un año es de :{fibo(13)}") #se imprime
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
class vehicle:
    def _init_(self,d_delivery, cost, model, year, owner):
        self.d_delivery = d_delivery
        self.cost = cost
        self.model = model
        self.year = year
        self.owner = owner
list = []

list.append(vehicle('13/09/2022', '20000','Mustang Match 1', '1969', 'Samuel'))
list.append(vehicle('15/09/2022', '12000','Tesla Model y', '2020', 'negro'))
list.append(vehicle('06/01/2022', '33000','Porsche Taycan', '2022', 'Paco'))

for obj in list:
    print(obj.d_delivery, obj.cost, obj.model, obj.year, obj.owner, sep=' ')  #(sep =' ') es el separador entre los argumentos para la función print()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class vehicle:
    def _init_(self, d_delivery, cost, model, year, owner):
        self.d_delivery = d_delivery
        self.cost = cost
        self.model = model
        self.year = year
        self.owner = owner
list_car = []
list_car.append(vehicle('13/09/2022', '20000','Mustang Match 1', '1969', 'Samuel'))
list_car.append(vehicle('15/09/2022', '12000','Tesla Model y', '2020', 'negro'))
list_car.append(vehicle('06/01/2022', '33000','Porsche Taycan', '2022', 'Paco'))
for obj in list_car:
    print(obj.d_delivery, obj.cost, obj.model, obj.year, obj.owner, sep=' ')  #(sep =' ') es el separador entre los argumentos para la función print()

class employee:
    def _init_(self, name, position, salary, car, document):
        self.name = name
        self.position = position
        self.salary = salary
        self.car = car
        self.document = document
list_emplo = []
list_emplo.append(employee('calos','secretario','200','Porsche','1003809076' ))
for obj_e in list_emplo:
    print(obj_e.name, obj_e.position, obj_e.salary, obj_e.car, obj_e.document, sep=' ')

class client:
    def _init_(self,name, document, car):
        self.name=name
        self.document = document
        self.car = car
list_client=[]
list_client.append(client('Maria','123321','Toyota'))
for obj_c in list_client:
    print(obj_c.name, obj_c.document, obj_c.car, sep=' ')
