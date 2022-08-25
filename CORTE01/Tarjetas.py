## Algoritmo para la validación de tarjetas de crédito
while True:
    # Ingreso del núero de la tarjeta de crédito
    str_numero = input('Ingrese el número de la tarjeta')
    # validación de longitud
    s_len = len(str_numero)
    # Validación de la longitud de la tarjeta
    if not(s_len==15 or s_len==13 or s_len==16):
        continue
    tot = ''
    # Calculo de los valores que se deben multiplicar por 2
    for i in range (s_len-2,-1,-2):
        s_num = int(str_numero[i])*2
        tot += str(s_num)
    sum = 0
    # Suma de todos los números en la cadena resultante
    for i in range(len(tot)):
        sum += int(tot[i])
    # Suma de los números no considerados inicialmente.
    for i in range(s_len - 1, -1, -2):
        sum += int(str_numero[i])

    # Validación de los números inicales para determinar la marca de la tarjeta
    if(sum%10 == 0):
        print('Tarjeta valida')
        if(str_numero.startswith('37')or str_numero.startswith('34')):
            print('American')
        elif(str_numero.startswith('51') or str_numero.startswith('52') or str_numero.startswith('53') or str_numero.startswith('54') or str_numero.startswith('55')):
            print('Master')
        elif(str_numero.startswith('4')):
            print('Visa')

    else:
        print('Tarjeta No valida')

