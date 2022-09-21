#!/usr/bin/python3

import csv
from tempfile import NamedTemporaryFile
import shutil
import re

class DBbyCSV:
    def __init__(self, schema, filename):
        self._filename = f'./{filename}.csv'
        try:
            # Verificamos si ya existe el archivo
            f = open(self._filename)
            f.close()
        except IOError:
            # Si el archivo no existe creamos la cabecera
            with open(self._filename, mode='w', encoding='utf-16') as csv_file:
                data_writer = csv.writer(csv_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
                data_writer.writerow(schema.keys()) #Le pasamos las claves del diccionario, que seran las cabeceras del archivo
    '''Con quoting=csv.QUOTE_MINIMAL indicaremos que las comillas solo las añada a los textos que tengan caracteres especiales
       Con lineterminator le indicamos que termine la línea con el salto de línea "\n"'''
    
    def insert(self, data):
        '''Funcion para insertar contactos
           Obtiene el id mas alto mediante la funcion get_last_id, y crea una lista con el identificador mas alto +1 y los datos del contacto
           y luego mediante el writer, los añade al csv.'''
        id_contact = self.get_last_id() + 1
        line = [id_contact] + data

        with open(self._filename, mode='a', encoding='utf-16') as csv_file: # Utilizamos el modo a, para añadir elementos al archivo, si utilizamos el modo w, los sobreescribiriamos.
            data_writer = csv.writer(csv_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            data_writer.writerow(line)
        return True

    def get_last_id(self):
        '''Funcion que recorre el csv guardando todos los identificadores, y luego los ordena de mayor a menor, y por ultimo
           retorna el primer elemento de la lista. En caso de que la misma este vacia, retorna 0'''
        list_ids = []
        with open(self._filename, mode='r', encoding='utf-16') as csv_file: #Modo r es modo lectura
            csv_reader = csv.reader(csv_file, delimiter=';') #Lee el archivo
            is_header = True
            for row in csv_reader:
                if is_header:
                    is_header = False
                    continue
                if row:
                    list_ids.append(row[0])
        if not list_ids:
            return 0 #Retorna 0 si la lista esta vacia
        # Ordenamos la lista de mayor a menor y retornamos el elemento de mayor tamaño
        list_ids.sort(reverse = True) 
        return int(list_ids[0]) #Retorna primer elemento
    
    def get_all(self):
        '''Funcion que devuelve el listado de todos los contactos guardados en el CSV como diccionario, en donde las keys son los textos de la
           cabecera y los valores son los valores de cada contacto.'''
        list_data = []
        list_header = []
        with open(self._filename, mode='r', encoding='utf-16') as csv_file: #Modo r, modo lectura
            csv_reader = csv.reader(csv_file, delimiter=';') #Lee el archivo
            is_header = True
            for row in csv_reader:
                if is_header:
                    list_header = row
                    is_header = False
                    continue
                if row:
                    file = {}
                    for key, value in enumerate(row):
                        file[list_header[key]] = value
                    list_data.append(file)
        return list_data

    def get_by_filters(self, filters):
        '''Funcion que puede recibir por paramtros de busqueda, tanto el mail como el nombre o el apellido/s.
        Despues de que lee el csv que utlizamos para guardar los datos, y utiliza una expresion regular para
        buscar coincidencias entre nuestros filtros y los campos del csv, si hacemos match al menos con uno de los
        filtros, lo guardamos en una lista que posteriormente retornaremos al usuario'''
        list_data = []
        list_header = []
        with open(self._filename, mode='r', encoding='utf-16') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            is_header = True
            for row in csv_reader:
                if is_header:
                    list_header = row
                    is_header = False
                    continue

                if row:
                    file = {}

                    for key, value in enumerate(row):
                        file[list_header[key]] = value
                    
                    for key_filter, value_filter in filters.items():
                        matches = re.search(rf"{value_filter}", file[key_filter], re.IGNORECASE)
                        if matches:
                            list_data.append(file)
                            break
        return list_data

    def get_by_id(self, id_object):
        '''Funcion que recibira un id y luego lee el CSV, si se encuentra una coincidencia devolvera un diccionario con los datos del contacto,
        de lo contrario devolvera un diccionario vacio'''
        list_header = []
        with open(self._filename, mode='r', encoding='utf-16') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            is_header = True
            for row in csv_reader:
                if is_header:
                    list_header = row
                    is_header = False
                    continue
                if row:
                    file = {}
                    for key, value in enumerate(row):
                        file[list_header[key]] = value
                    if file['ID'] == id_object:
                        return file
        return {}

    def update(self, id_object, data):
        return self.modify_file(id_object, data, 'update')
    
    def delete(self, id_object):
        return self.modify_file(id_object, {}, 'delete')

    def modify_file(self, id_object, data, action):
        '''Funcion que evita la duplicacion de codigo, ya que el borrado es muy similar al update. Enviaremos por parametros el id del contacto,
        los datos a actualizar y si procede, y la accion que sera update o delete. El proceso sera igual que en el update, pero cuando esta recorriendo
        el CSV comprobara si el action es update o delete. Si es update, actualizamos la fila cuando haga match, si no, cuando encuentra la coincidencia,
        la ignoraremos esa linea y no la insertaremos en el archivo temporal'''
        data_csv = self.get_by_id(id_object)
        if not data_csv:
            raise Exception('No se ha encontrado el objecto con el id enviado')
        for key, value in data.items():
            data_csv[key] = value
        tempfile = NamedTemporaryFile(mode='w', delete=False, encoding='utf-16')
        list_header = []
        with open(self._filename, mode='r', encoding='utf-16') as csv_file, tempfile:
            csv_reader = csv.reader(csv_file, delimiter=';')
            data_writer = csv.writer(tempfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            is_header = True
            for row in csv_reader:
                if is_header:
                    list_header = row
                    is_header = False
                    data_writer.writerow(row)
                    continue
                # Si es update, actualizamos cuando hacemos match
                if row and action == 'update':
                    file = {}
                    for key, value in enumerate(row):
                        file[list_header[key]] = value
                    if file['ID'] != data_csv['ID']:
                        data_writer.writerow(row)
                        continue
                    for key, value in data_csv.items():
                        file[key] = value
                    data_writer.writerow(file.values())
                # Si es delete cuando hacemos match continuamos para saltarnos el insertado de esa línea
                elif row and action == 'delete':
                    file = {}
                    for key, value in enumerate(row):
                        file[list_header[key]] = value
                    if file['ID'] == data_csv['ID']:
                        continue
                    data_writer.writerow(row)
        shutil.move(tempfile.name, self._filename)
        return True