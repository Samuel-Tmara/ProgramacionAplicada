## Juego de scrabble
# Inicializar el diccionario con todos los valores de las letras
dic = {'A':1,'B':3,'C':3,'D':2,'E':1,'F':4,'G':2,'H':4,'I':1,'J':8,'K':5,'L':1,'M':3,'N':1,'O':1,'P':3,'Q':10,'R':1,'S':1,'T':1,'U':1,'V':4,'W':4,'X':8,'Y':4,'Z':10}
# icialización de las variables
v_puntos = [0,0]
v_jug = ['Jug1','Jug2']

def puntos (str_jugador):
    '''
    Se pide la palabra al jugador y retorna el número de puntos que vale la palabra
    :param str_jugador: nombre del jugador actual
    :return: total de puntos hechos
    '''
    str_msj = 'inserte su palabra '+str_jugador
    pal = input(str_msj).upper() # Solicitud de palabra al jugador
    tot = 0
    # Calculo del puntaje
    for let in pal:
        tot += dic[let]
    return tot

# Ejecución para los dos jugadores
for i in range(len(v_jug)):
    v_puntos[i] = puntos(v_jug[i])
    str_msj = 'puntos '+ v_jug[i] +'='+str(v_puntos[i])
    print(str_msj)

#obtención del indice el maximo valor de puntajes
index_max = max(range(len(v_puntos)), key=v_puntos.__getitem__)
# Impresión del ganador (no se considera la situación de empate)
str_msj = 'ganador ='+v_jug[index_max]
print(str_msj)
