import json
from json.decoder import JSONDecodeError

contacts = []

class Contact:
  def __init__(self, name, lastname, mail, phone, address):
    self.name = name
    self.lastname = lastname
    self.mail = mail
    self.phone = phone
    self.address = address
  
  def get_data(self):
    return {
      "name": self.name,
      "lastname": self.lastname,
      "mail": self.mail,
      "phone": self.phone,
      "address": self.address,
    }

  def edit(self,property,value):
    if property == "1":
      self.name = value
    elif property == "2":
      self.lastname = value
    elif property == "3":
      self.mail = value
    elif property == "4":
      self.phone = value
    elif property == "5":
      self.address = value

try:
  f = open("database.json", "r")
  data = json.loads(f.read())
  f.close()
  for contact in data:
    contacts.append(Contact(contact["name"], contact["lastname"], contact["mail"], contact["phone"], contact["address"]))
except FileNotFoundError:
  f = open("database.json", "x")
  f.close()
except JSONDecodeError:
  pass

def add():
  numer = str(input("Podaj numer do którego chcesz przypisać kontakt: "))
  if len(numer) != 9:
    print("Numer nieprawidłowy!")
    return
  for contact in contacts:
    if numer == contact.phone:
      print("Taki kontakt już istnieje!")
      return
  name = str(input("Podaj imie: "))
  lastname = str(input("Podaj nazwisko: "))
  mail = str(input("Podaj maila: "))
  address = str(input("Podaj adres: "))
  newcontact = Contact(name,lastname,mail,numer,address)
  contacts.append(newcontact)

def edit():
  numer = str(input("Podaj numer który zamierzasz edytować:"))
  for contact in contacts:
    if numer == contact.phone:
      m = str(input("Wybierz co chcesz edytować:\n1 - imie \n2 - nazwisko \n3 - mail \n4 - telefon \n5 - adres\n"))
      x = str(input("Wybierz nową wartość"))
      contact.edit(m,x)
      return
  print ("Nie znaleziono takiego kontaktu")


def search () -> str:
  m = str(input("Wybierz jak chcesz wyszukać kontakt:\n1 - imie \n2 - nazwisko \n3 - mail \n4 - telefon \n5 - adres\n"))
  zmienna = ""
  if m == "1":
    zmienna = str(input("Podaj imie osoby szukanej:\n"))
  elif m == "2":
    zmienna = str(input("Podaj nazwisko osoby szukanej:\n"))
  elif m == "3":
    zmienna = str(input("Podaj mail osoby szukanej:\n"))
  elif m == "4":
    zmienna = str(input("Podaj telefon osoby szukanej:\n"))
  elif m == "5":
    zmienna = str(input("Podaj ades osoby szukanej:\n"))
  else:
    print("Nieprawidłowa akcja")
    return
  found = 0
  for contact in contacts:
    if m == "1" and zmienna == contact.name:
      found = 1
      print('{contact.name} {contact.lastname} {contact.mail} {contact.phone} {contact.address}'.format(contact=contact))
    elif m == "2" and zmienna == contact.lastname:
      found = 1
      print( '{contact.name} {contact.lastname} {contact.mail} {contact.phone} {contact.address}'.format(contact=contact))
    elif m == "3" and zmienna == contact.mail:
      found = 1
      print( '{contact.name} {contact.lastname} {contact.mail} {contact.phone} {contact.address}'.format(contact=contact))
    elif m == "4" and zmienna == contact.phone:
      found = 1
      print('{contact.name} {contact.lastname} {contact.mail} {contact.phone} {contact.address}'.format(contact=contact))
    elif m == "5" and zmienna == contact.address:
      found = 1
      print('{contact.name} {contact.lastname} {contact.mail} {contact.phone} {contact.address}'.format(contact=contact))
  if found == 0:
    print("Nie ma takiego kontaktu")

def save_on_close():
  data = []
  for contact in contacts:
    data.append(contact.get_data())
  f = open("database.json", "w")
  f.write(json.dumps(data))
  f.close()

while True:
  m = str(input("Wybierz funkcje:\n1 - dodaj nowy kontakt\n2 - edytuj kontakt\n3 - usun kontakt\n4 - pokaz wszystkie kontakty\n5 - wyszukaj kontakt\nCokolwiek innego aby zakończyć działanie programu\n"))
  if m == "1":
    add()
    pass
  elif m == "2":
    edit()
    # edycja kontaktu
    pass
  elif m == "3":
    # usuwanie kontaktu
    pass
  elif m == "4":
    # pokazanie listy
    pass
  elif m == "5":
    search()
    pass
  else:
    save_on_close()
    break
