#!/usr/bin/python3

import re # Libreria para utilizar las Expresiones Regulares
import datetime # Libreria para utilizar los formatos de las fechas

regex_email = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$' #Link: https://www.genbeta.com/desarrollo/expresiones-regulares-regex-herramientas-online-para-probarlas
regex_phone = '^[0-9]{9}$'

class Validations:
    def __init__(self):
        pass

    def validateName(self, name): #Funcion para validar el NAME pasado por el usuario
        if len(name) < 3 or len(name) > 50: #El mismo debe ser mayor a 3 caracteres y menor a 50
            raise ValueError(f'El nombre debe tener como mínimo 3 caractares y un máximo de 50 caracteres, tamaño actual: {len(name)}') #Mensaje de retorno en caso de error
        return True

    def validateSurname(self, surname): #Funcion para validar el SURNAME pasado por el usuario
        if len(surname) < 5 or len(surname) > 100: #El mismo debe ser mayor a 5 y menor a 100
            raise ValueError(f'Los apellidos deben tener como mínimo 5 caractares y un máximo de 100 caracteres, tamaño actual: {len(surname)}') #Mensaje de retorno en caso de error
        return True


    def validateEmail(self, email): #Funcion para validar el EMAIL pasado por el usuario
        if not re.search(regex_email, email): #Si el EMAIL no cumple con los requisitos establecidos en la variable regex_email
            raise ValueError('El formato del email no es válido')
        return True

    def validatePhone(self, phone): #Funcion para validar el PHONE pasado por el usuario
        if not re.search(regex_phone, phone): #Si el PHone pasado no cumple con los requisitos establecidos en la variable regex_phone (que sea un numero de 9 cifras)
            raise ValueError('El formato del teléfono no es válido, debe ser un número de 9 cifras sin guiones ni puntos') #Mensaje de error
        return True


    def validateBirthday(self, birthday): #Funcion para validar el BIRTHDAY pasado por el usuario
        try:
            datetime.datetime.strptime(birthday, '%Y-%m-%d') #Intenta formatear el estilo de la fecha pasada por el usuario
        except ValueError:
            raise ValueError('El formato de la fecha es incorrecta, debe ser YYYY-MM-DD') #En caso de que no coincida el formato, salta mensaje de error.
        return True

def check_name():
        print('Inserta el nombre:')
        name = input()
        try:
            validator.validateName(name)
            return name
        except ValueError as err:
            print(err)
            check_name()
    
def check_surname():
    print('Inserta los apellidos:')
    surname = input()
    try:
        validator.validateSurname(surname)
        return surname
    except ValueError as err:
        print(err)
        check_surname()

def check_email():
    print('Inserta el email:')
    email = input()
    try:
        validator.validateEmail(email)
        return email
    except ValueError as err:
        print(err)
        check_email()

def check_phone():
    print('Inserta el teléfono (9 cifras sin guiones ni puntos):')
    phone = input()
    try:
        validator.validatePhone(phone)
        return phone
    except ValueError as err:
        print(err)
        check_phone()

def check_birthday():
    print('Inserta la fecha de nacimiento (YYYY-MM-DD):')
    birthday = input()
    try:
        validator.validateBirthday(birthday)
        return birthday
    except ValueError as err:
        print(err)
        check_birthday()