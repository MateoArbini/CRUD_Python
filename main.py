#!/usr/bin/python3
'''
CRUD de datos con Python 
MAIN - Archivo de entrada a nuestro CRUD, en donde añadimos un menu que se mostrara
       al Usuario y que indicara las distintas opciones que tiene la agenda
'''

import os #Con esta libreria, se utilizaran las funcionalidades del sistema
import time #Con esta libreria, se utilizaran las funcionalidades de temas fechas
from classes.validations import Validations, check_birthday, check_email, check_name, check_phone, check_surname, check_name
from classes.contact import Contact
from prettytable import PrettyTable
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
    name = check_contact_data() #Chequea el nombre con la funcion check_name() definida en validation.py
    surname = check_contact_data() #Chequea el nombre con la funcion check_surnname() definida en validation.py
    email = check_contact_data() #Chequea el nombre con la funcion check_email() definida en validation.py
    phone = check_contact_data() #Chequea el nombre con la funcion check_phone() definida en validation.py
    birthday = check_contact_data() #Chequea el nombre con la funcion check_birthday() definida en validation.py
    contact = Contact(None, name, surname, email, phone, birthday)
    if db.save_contact(contact):
        print('Contacto insertado con éxito')
    else:
        print('Error al guardar el contacto')

def check_contact_data(message, data_name):
    print(message)
    input_data = input()
    try:
        getattr(validator, f'validate{data_name.capitalize()}')(input_data)
        return input_data
    except ValueError as err:
        print(err)
        check_contact_data(message, data_name)

def list_contacts():
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
    print(table)
    print('Pulsa intro para salir')
    command = input()

if __name__ == "__main__": # Al utilizar esto, le decimos al interprete que lo que hay que ejecutar cuando se ejecuta el main
    run()                  # es la funcion run().