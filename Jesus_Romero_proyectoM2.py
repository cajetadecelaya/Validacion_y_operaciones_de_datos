##########Longuitud de una frase
print('Longuitud de una frase')

palabra = input('Ingrese una palabra que contenga entre 4 y 8 letras: ')
"""Ingresamos el dato solicitado"""

while  palabra.isdigit():
    print('!DATO INVALIDO¡')
    palabra = input('Ingrese una palabra que contenga entre 4 y 8 letras: ')
    """Con este ciclo ?while? se verifica que se ingresen letras, de lo contrario  arrojara !DATO INVALIDO¡ 
    y solicitara ingresar datos de nuevo."""

while  True:
    if len(palabra) > 3:
            if len(palabra) <9:
                print(f'La palabra es correcta.\nSe ingresaron "{len(palabra)}" letras.')
                break    
            else:
                print(f'Sobran letras. Tienes {len(palabra)} letras.') 
                palabra = input('Ingrese una palabra que contenga entre 4 y 8 letras: ')
                while  palabra.isdigit():
                     print('!DATO INVALIDO¡')
                     palabra = input('Ingrese una palabra que contenga entre 4 y 8 letras: ')

    elif len(palabra) <4:
            print(f'Hacen falta letras. Tienes {len(palabra)} letras')      
            palabra = input('Ingrese una palabra que contenga entre 4 y 8 letras: ')
            while  palabra.isdigit():
             print('!DATO INVALIDO¡')
             palabra = input('Ingrese una palabra que contenga entre 4 y 8 letras: ')
    """Este bloque de codigo recibie el dato ingresado y se verifica que cuente con los 
    caracteres solicitados, de lo contrario arojara '!DATO INVALIDO¡' y solicitara ingresar el dato de nuevo. """

########Encuentra el cuadrante

print('\n\nEncuentra el cuadrante')
while True:
    try:
        x = int(input('Ingrese X: '))
        if x !=0:
            break
        else:
            print('Valor a 0 no es permitido!')

    except ValueError:
        print('Dato invalido.')  
"""Se verifica  que se este introduciento un numero(x) diferente a 0. """


while True:
    try:
        y = int(input('Ingrese Y: '))
        if y !=0:
         break
        else:
           print('Valor a 0 no es permitido!') 

    except ValueError:
         print('Dato invalido.')   
"""Se verifica  que se este introduciento un numero(y) diferente a 0. """

if x >0 and y >0:
    print('El punto se encuentra en el cuadrante 1')
elif x < 0 and y> 0:
    print('El punto se encuentra en el cuadrante 2')
elif x < 0 and y < 0:  
    print('El punto se encuentra en el cuadrante 3') 
elif x > 0 and y < 0:  
    print('El punto se encuentra en el cuadrante 4') 
"""Este bloque de condicionales definiran en que cuadrante del plano cartesiano se encuentra el numero"""