contacts = []

class Contact:
  def __init__(self, name, lastname, mail, phone, address):
    self.name = name
    self.lastname = lastname
    self.mail = mail
    self.phone = phone
    self.address = address

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

while True:
  m = str(input("Wybierz funkcje:\n1 - dodaj nowy kontakt\n2 - edytuj kontakt\n3 - usun kontakt\n4 - pokaz wszystkie kontakty\n5 - wyszukaj kontakt\n"))
  if m == "1":
    add()
    pass
  elif m == "2":
    # edycja kontaktu
    pass
  elif m == "3":
    # usuwanie kontaktu
    pass
  elif m == "4":
    # pokazanie listy
    pass
  elif m == "5":
    # wyszukanie kontaktu
    pass
  else:
    print("niepoprawna opcja")
