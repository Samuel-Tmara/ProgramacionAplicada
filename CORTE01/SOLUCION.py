## 12-TALLER 01
'''
El presente taller tiene como objetivo evaluar las habilidades adquiridas hasta el momento a lo largo del curso,
así como repasar los conceptos e introducir nuevas herramientas.
'''
# Recordatorio, el archivo lo deben subir a su repositorio en la fecha indicada.
## 1. Persistencia (1.0)
l_paises = ['Colombia','Mexico','Turquía','Polonia','serbia','dinamarca','holada','Alemania']
#escriba un programa que le permina escribir de manera automatica los nombres de estos paises en un archivo txt (csv)
str_paises = ''
for pais in l_paises:
    str_paises += pais.capitalize()
    str_paises += ','
with open('Paises.txt','w') as f:
    f.write(str_paises)
#NOTA: todos los nombres deben tener una mayuscula al comienzo
#       el archivo se ecuentra en formato csv
## 2. Lectura de archivos (1.0)
#escriba un programa que le permita leer e imprimir el archivo generado anteriormente
with open('.\Paises.txt') as f:
    lines = f.readlines()
    lines = lines[0]
    v_paises = lines.split(',')
    print(v_paises)
## 3. números binario (1.5)
def f_int2bin (s_int):
    '''
    function to convert the integer part of a number to the  binary representation
    :param s_int: integer to convert
    :return: string containing the values
    '''
    str_num = ''
    while not(s_int==0):
        s_act =  s_int%2
        str_num = str(s_act) + str_num
        s_int = s_int//2
    return  str_num

def f_frac2bin(s_frac):
    s_cont = 0
    str_num = '.'
    while not(s_frac==0) and s_cont <=10:
        str_frac = str(s_frac*2)
        str_num +=str_frac[0]
        str_frac = '0.'+str_frac[2:]
        s_frac = float(str_frac)
        s_cont+=1
    return  str_num

def f_calBin (s_num):
    '''
    Calculadora que permite encontrar la representación en binario de un número entero o decimal que ingresa por parametro
    :param s_num: número que se desea convertir a binario int o float
    :return: valor número en binario
    '''
    #escribir la sección del codigo para las conversiones
    s_bin = 0  # deben asignal el valor binario en esta variable
    str_num =str(s_num)
    b_dec = str_num.__contains__('.')
    l_num = str_num.split('.')
    s_elem = len(l_num)
    if s_elem == 2:
        str_int = f_int2bin(int(l_num[0]))
        str_frac = f_frac2bin(float('0.'+l_num[1]))
        s_bin = float(str_int+str_frac)
    else:
        if b_dec:
            str_frac = f_frac2bin(float(l_num[1]))
            s_bin = float('0' + str_frac)
        else:
            str_int = f_int2bin(int(l_num[0]))
            s_bin = int(str_int)
    return s_bin

#Test

assert f_calBin (1) == 1
assert f_calBin (4) == 100
assert f_calBin (10) == 1010
assert f_calBin (1.25) == 1.01

## 4. Valores estadisticos (1.5)
import numpy as np
def f_stat (l_valores):
    '''
    función que toma una lista de valores y retorna el promedio, la mediana y la desviación estandar
    :param l_valores: lista con los valores a utilizar
    :return:
    '''
    s_mean, s_median, s_mode = 0,0,0
    ord = np.sort(l_valores)
    s_median = ord[len(ord)//2]
    s_mean = np.sum(ord)/len(ord)
    s_cont = 0
    s_max = 0
    for num in ord:

    return s_mean,s_median,s_mode

## 5. BONO (0.5)
#TODO: realizar la verificación del punto aterior haciendo uso de la función assert (pytest)

