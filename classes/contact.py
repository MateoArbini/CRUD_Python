#!/usr/bin/python3

class Contact:
    def __init__(self, id_contact, name, surname, email, phone, birthday):
        self._name = name # Todos las variables de la clase son PRIVADAS.
        self._surname = surname
        self._email = email
        self._phone = phone
        self._birthday = birthday
        self._id_contact = id_contact

    '''Una vez definida la clase, agregamos los getters y setters'''
    @property #Getter ID_CONTACT
    def id_contact(self):
        return self._id_contact

    @id_contact.setter # Setter ID_CONTACT
    def id_contact(self, id_contact):
        self._id_contact = id_contact

    @property # Getter NAME
    def name(self):
        return self._name

    @name.setter # Setter NAME
    def name(self, name):
        self._name = name

    @property # Getter SURNAME
    def surname(self):
        return self._surname

    @surname.setter # Setter SURNAME
    def surname(self, surname):
        self._surname = surname

    @property # Getter EMAIL
    def email(self):
        return self._email

    @email.setter # Setter EMAIL
    def email(self, email):
        self._email = email

    @property # Getter PHONE
    def phone(self):
        return self._phone

    @phone.setter # Setter PHONE
    def phone(self, phone):
        self._phone = phone

    @property # Getter BIRTHDAY
    def birthday(self):
        return self._birthday

    @birthday.setter # Setter BIRTHDAY
    def birthday(self, birthday):
        self._birthday = birthday