class PhoneBook:
    contacts = []

    def __init__(self, name, contacts_list=[]):
        self.name = name
        self.contacts = contacts_list

    def print_contacts(self):
        for contact in self.contacts:
            print(contact)

    def add_contact(self, cont):
        self.contacts.append(cont)
        print(f'~Добавлен контакт \n {cont}')

    def contact_del(self, phone_num):
        for contact in self.contacts:
            if contact.number == phone_num:
                self.contacts.remove(contact)
                print(f'Контакт {phone_num} удален')

    def find_fav(self):
        print('Контакты в избранном:')
        for contact in self.contacts:
            if contact.fav:
                print(contact)

    def find_name(self, name, surname):
        for contact in self.contacts:
            print(contact)
            if contact.name == name and contact.surname == surname:
                print(contact)
            else:
                print(f'Контакта с именем {name} и фамилией {surname} нету в телефонной книге :(')


class Contact(PhoneBook):
    info = []

    def __init__(self, name, surname, number, *args, fav=False, **kwargs):
        self.name = name
        self.surname = surname
        self.number = number
        if fav:
            self.fav = 'да'
        else:
            self.fav = 'нет'
        print(args)
        print(kwargs)
        if len(args) > 0:
            for arg in args:
                self.info.append(arg)
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                self.info.append({key: value})
        self.contact_info = {
            'Имя': self.name,
            'Фамилия': self.surname,
            'Телефон': self.number,
            'В избранных': self.fav,
            'Дополнительная информация': self.info
        }

    def __str__(self):
        info = ''
        for el in self.info:
            if isinstance(el, dict):
                for key, value in el.items():
                    info += '\t' + key + ':' + ' ' + value + '\n'
            else:
                info += '\t' + el + '\n'

        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Телефон: {self.number}\n' \
               f'В избранных: {self.fav}\n' \
               f'Дополнительная информация: \n{info}'
