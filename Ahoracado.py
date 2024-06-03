
# crear una lista con las palabras a adivinar
lista_palabras = ['frutilla','botella','television','flores','cafetera']

#importamos la funcion random
import random

#funcion para elegir una palabra al azar 
def elegir_palabra():
    return random.choice(lista_palabras)

# crear una funcion para ver si la letra ingresada esta en la palabra
def adivinar_palabra(palabra, letra):
    i = 0
    while i < len(palabra) and palabra[i] != letra:
        i= i + 1
        if i <= len(palabra):
            return i
        else:
            return -1

    #palabra = [] # crear una variable a la que se le asigne una cadena vacia
#    for letra in adivinar_letra: #recorrer cada letra de la palabra que esta en la lista 
#        if letra in letras_adivinadas: # condicional para verificar si la letra que el usuario ingreso se encuentra dentro de la palabra
#            palabra += letra  # si la letra está se agrega a la palabra en pantalla
#        else:
#            palabra += ' '  #si la letra no está se agrega un espacio vacio
#        print(palabra)

#declaramos la variable de la palabra que sale
palabra_seleccionada = elegir_palabra()

#aca comienza nuestro programa
arrancar = input("Desea jugar?")
while arrancar == "SI" or arrancar == "si":
    letra_ingresada = str(input("Ingrese una letra"))
    posicion = adivinar_palabra(palabra_seleccionada, letra_ingresada)
    print(posicion)
    print(palabra_seleccionada)

    
if arrancar == "No" or arrancar == "no":
    arrancar = input("Desea jugar?")
else: print("Ingrese un valor valido")
arrancar = input("Desea jugar?")
 


#letras_adivinadas = [] # crear una lista donde se van a guardar las letras que el usuario adivina
#cantidad_intentos = 7 # inicializar una variable con la cantidad  maxima de intentos que tiene el jugador

# crear un bucle para la cantidad de intentos que tiene el jugardor para adivinar:
# mientras que la cantidad de intentos sea mayor a 0, este dentro de la cantidad permitida (3)
# y el usuario no haya adivinado la palabra se ejecuta el bucle
# Y pedir al usuario que ingrese una letra
#while cantidad_intentos > 0 and cantidad_intentos < 3 :
#    letras_ingresadas = (input('Ingrese la letra: '))

# funcion(?) que chequee que la letra que ingreso el usuario se encuentra dentro de la palabra a adivinar
# si es una letra es repetida informarle que ya la ingreso y que pruebre con otra
# si la letra no se encuentra dentro de la palabra pedirle al usuario que ingrese otra letra 
# y se van reduciendo la cantidad de intentos
# si la letra se encuentra dentro de la palabra que hay que adivinar agregarla a la lista de 
# letras_adivinadas

#if letras_ingresadas in letras_ingresadas :
#    print('ESA LETRA YA FUE INGRESADA, PROBA CON OTRA')
#elif letras_ingresadas not in lista_palabras :
#    cantidad_intentos -= 1
#    print('PROBA CON OTRA LETRA')

# Imprimir la palabra con las letras que el usuario va adivinando (otro bucle?)

# Si el jugador acierta todas las letras imprimir un mensaje de victoria
# si el jugador gasta todos sus intentos imprimir un mensaje de derrota

#if letras_ingresadas :
#    print('FELICIDADES! GANASTE EL JUEGO')
#else:
#    print('TE QUEDASTE SIN INTENTOS! SUERTE EN LA PROXIMA')


# FIN DEL PROGRAMA






