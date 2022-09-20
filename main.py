#!/usr/bin/python3
'''
CRUD de datos con Python 
MAIN - Archivo de entrada a nuestro CRUD, en donde añadimos un menu que se mostrara
       al Usuario y que indicara las distintas opciones que tiene la agenda
'''

import os #Con esta libreria, se utilizaran las funcionalidades del sistema
import time #Con esta libreria, se utilizaran las funcionalidades de temas fechas

def print_options():
    '''Funcion que mostrara las distintas acciones de nuestra agenda
       Para que el usuario pueda ejecutar una de estas acciones, debera indicar
       la letra correspondiente'''
    print('AGENDA DE CONTACTOS')
    print('*' * 50)
    print('Selecciona una opción:')
    print('[C]rear contacto')
    print('[L]istado de contactos')
    print('[M]odificar contacto')
    print('[E]liminar contacto')
    print('[B]uscar contacto')
    print('[S]ALIR')

def run():
    '''Funcion MAIN de nuestro CRUD'''
    print_options() # Ejecutamos la función print, para mostrarle al usuario las acciones disponibles.
    command = input() # El comando input() le pide al usuario la letra de la accion a realizar.
    command = command.upper() # El comando upper(), convierte el texto recibido en el imput a mayuscula.

    if command == 'C':
        pass
    elif command == 'L':
        pass
    elif command == 'M':
        pass
    elif command == 'E':
        pass
    elif command == 'B':
        pass
    elif command == 'S': # Ejecuta la accion SALIR y se vuelve a la consola.
        os._exit(1)
    else:
        print('Comando inválido') # Si no coincide ninguna letra, el comando ingresado por el usuario no es valido
        time.sleep(1) # se duerme el script por un segundo
        run() # Se vuelve a ejecutar el comando de nuevo.

if __name__ == "__main__": # Al utilizar esto, le decimos al interprete que lo que hay que ejecutar cuando se ejecuta el main
    run()                  # es la funcion run().