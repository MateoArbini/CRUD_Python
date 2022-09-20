#!/usr/bin/python3
'''
CRUD de datos con Python 
MAIN - Archivo de entrada a nuestro CRUD, en donde añadimos un menu que se mostrara
       al Usuario y que indicara las distintas opciones que tiene la agenda
'''

import os #Con esta libreria, se utilizaran las funcionalidades del sistema
import time #Con esta libreria, se utilizaran las funcionalidades de temas fechas
from classes.validations import Validations
from classes.contact import Contact
from prettytable import PrettyTable #Libreria para mostrar los contactos de una manera mas amigable
from classes.dbcontacts import DBContacts
validator = Validations()
db = DBContacts()


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
        create_contact() #Si la letra es C, se ejecuta la siguiente funcion
    elif command == 'L':
        list_contacts() #Si la letra es L, se ejecuta la siguiente funcion
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

def create_contact():
    '''Funcion que crea contactos en la agenda - C'''
    print('CREACIÓN DE CONTACTO')
    print('*' * 50)
    name = check_contact_data('Inserta el nombre:', 'name') #Chequea el nombre con la funcion check_contact_data()
    surname = check_contact_data('Inserta los apellidos:', 'surname') #Chequea el nombre con la funcion check_contact_data()
    email = check_contact_data('Inserta el email:', 'email') #Chequea el nombre con la funcion check_contact_data()
    phone = check_contact_data('Inserta el teléfono (9 cifras sin guiones ni puntos):', 'phone') #Chequea el nombre con la funcion check_contact_data()
    birthday = check_contact_data('Inserta la fecha de nacimiento (YYYY-MM-DD):', 'birthday') #Chequea el nombre con la funcion check_contact_data()
    #Pasamos por parametro el mensaje y el nombre del campo
    contact = Contact(None, name, surname, email, phone, birthday) #Creamos un objeto de tipo Contact con los datos pasados y chequeados
    if db.save_contact(contact): #En caso de que se haya guardado con exito mediante la funcion save_contact()
        print('Contacto insertado con éxito')
    else: #En caso de que no se haya podido guardar mediante la funcion
        print('Error al guardar el contacto')

def check_contact_data(message, data_name):
    '''Para esta funcion estamos pasando el mensaje que queremos mostrar al usuario y el nombre del campo'''
    print(message)
    input_data = input()
    try:
        getattr(validator, f'validate{data_name.capitalize()}')(input_data)
        return input_data # En este return, lo que estamos haciendo es enviar el dato a validar al validador.
    except ValueError as err:
        print(err)
        check_contact_data(message, data_name)

def list_contacts():
    '''Esta funcion se encargara de recuperar el listado de contactos, si no hay ninguno, muestra un mensaje. Si existen elementos
       para mostrar, se crea un objeto de tipo PrettyTable, en donde en el constructor le pasamos las cabeceras y despues recorremos el
       listado de contactos para añadirlos a la tabla.'''
    list_contacts = db.list_contacts()
    if not list_contacts:
        return print('Todavía no hay contactos guardados')
    table = PrettyTable(db.get_schema().keys())
    for contact in list_contacts:
        table.add_row([
            contact.id_contact,
            contact.name,
            contact.surname,
            contact.email,
            contact.phone,
            contact.birthday
        ])
    print(table) #Printeamos la tabla
    print('Pulsa intro para salir') #Detenemos la finalizacion de la funcion cuando el usuario presiona Enter.
    command = input()

if __name__ == "__main__": # Al utilizar esto, le decimos al interprete que lo que hay que ejecutar cuando se ejecuta el main
    run()                  # es la funcion run().