from phonebook_class import PhoneBook, Contact
from advanced_print import adv_print
if __name__ == '__main__':
    my_contacts = PhoneBook('Мои контакты')
    jhon = Contact('Jhon', 'Smith', '+71234567809', 'Живет с собакой', fav=True, telegram='@jhony', email='jhony@smith.com')
    my_contacts.add_contact(jhon)
    my_contacts.find_fav()
    my_contacts.find_name(jhon.name, jhon.surname)
    my_contacts.contact_del(jhon.number)
    adv_print('Hello darkness my old friend', 15, True)