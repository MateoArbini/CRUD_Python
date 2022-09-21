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
        return self._create_object_contacts(list_contacts)

    def get_schema(self):
        '''Devuelve schema que creamos para la clase'''
        return SCHEMA

    def search_contacts(self, filters):
        '''Aqui comprobamos si al menos nos ha pasado un filtro, si no es asi, enviamos una excepcion, si pasa al menos un parametro de busqueda
        llamamos a la funcion get_by_filters y despues creamos un listado de objetos de tipo Contact con la funcion _create_object_contacts, funcion
        que se ha creado a partir de la funcion list_contacts en la que creaba el listado de objetos, ya que como lo utilizamos aqui tambien, la hemos
        extraido en una nueva funcion'''
        if 'NAME' not in filters and 'SURNAME' not in filters and 'EMAIL' not in filters:
            raise ValueError('Debes envíar al menos un filtro')
        list_contacts = self.get_by_filters(filters)
        return self._create_object_contacts(list_contacts)

    def _create_object_contacts(self, list_contacts):
        '''funcion que se ha creado a partir de list_contacts en la que creaba el listado de objetos, ya que como lo utilizamos aqui tambien, la hemos
        extraido en una nueva funcion'''
        if not list_contacts:
            return None
        object_contacts = []
        # Convertimos los datos a objectos de tipo contact
        for contact in list_contacts:
            c = Contact(contact['ID'], contact['NAME'], contact['SURNAME'], contact['EMAIL'], contact['PHONE'], contact['BIRTHDAY'])
            object_contacts.append(c)
        return object_contacts

    def update_contact(self, id_object, data):
        '''Validamos que se envie el id del contacto y un diccinario con al menos un dato y ya llamaremos a la funcion update que acabamos de crear'''
        if not id_object:
            raise ValueError('Debes envíar el id del contacto')
        if not data:
            raise ValueError('Debes envíar al menos un parámetro a actualizar')
        self.update(id_object, data)

    def delete_contact(self, id_object):
        '''Funcion que corrobora que nos haya enviado un id de contacto y llamamos a la funcion delete'''
        if not id_object:
            raise ValueError('Debes envíar el id del contacto')
        self.delete(id_object)