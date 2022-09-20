#!/usr/bin/python3

from .contact import Contact
from .dbcsv import DBbyCSV

'''Creamos una variable SCHEMA que sera un diccionario que contendra los nombres de nuestros datos
   y ciertas reglas definidas.'''
SCHEMA = {
    'ID': {
        'type': 'autoincrement',
    }, 
    'NAME': {
        'type': 'string',
        'min_length': 3,
        'max_length': 50
    }, 
    'SURNAME': {
        'type': 'string',
        'min_length': 5,
        'max_length': 100
    }, 
    'EMAIL': {
        'type': 'string',
        'max_length': 254
    }, 
    'PHONE': {
        'type': 'int'
    }, 
    'BIRTHDAY': {
        'type': 'date'
    }
}

class DBContacts(DBbyCSV):
    def __init__(self):
        #Con el super, lo que se hara es que podamos acceder al constructor padre y pasamos por parametros tanto el schema como el nombre que le queremos dar al archivo
        super().__init__(SCHEMA, 'contacts')

    def save_contact(self, contact):
        '''Funcion que guarda los contactos, los convierte en una lista y que luego pasa a la funcion insert() para guardarlo en el CSV'''
        data = [contact.name, contact.surname, contact.email, contact.phone, contact.birthday]
        return self.insert(data)
    
    def list_contacts(self):
        '''Esta funcion lo que hara, es traer todos los elemetnos de la funcion get_all(), y generara a partir de cada diccionario, un objeto
           de tipo Contact, los guardara en una lista y los devolvera.'''
        list_contacts = self.get_all()
        if not list_contacts:
            return None
        object_contacts = []
        # Convertimos los datos a objectos de tipo contact
        for contact in list_contacts:
            c = Contact(contact['ID'], contact['NAME'], contact['SURNAME'], contact['EMAIL'], contact['PHONE'], contact['BIRTHDAY'])
            object_contacts.append(c)
        return object_contacts

    def get_schema(self):
        '''Devuelve schema que creamos para la clase'''
        return SCHEMA