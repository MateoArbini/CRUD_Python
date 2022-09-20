#!/usr/bin/python3

import csv

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