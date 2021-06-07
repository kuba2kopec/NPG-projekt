contacts = []

class Contact:
  def __init__(self, name, lastname, mail, phone, address):
    self.name = name
    self.lastname = lastname
    self.mail = mail
    self.phone = phone
    self.address = address

def search () -> str:
  m = str(input("Wybierz jak chcesz wyszukać kontakt:\n1 - imie \n2 - nazwisko \n3 - mail \n4 - telefon \n5 - adres\n"))
  zmienna = ""
  if m == "1":
    zmienna = str(input("Podaj imie osoby szukanej:\n"))
  if m == "2":
    zmienna = str(input("Podaj nazwisko osoby szukanej:\n"))
  if m == "3":
    zmienna = str(input("Podaj mail osoby szukanej:\n"))
  if m == "4":
    zmienna = str(input("Podaj telefon osoby szukanej:\n"))
  if m == "5":
    zmienna = str(input("Podaj ades osoby szukanej:\n"))
  else:
    zmienna = "Not Defined"
    return "Nieprawidłowa akcja"
  found = 0
  for contact in contacts:
    if zmienna == contact.name:
      found = 1
      print('contact.name contact.lastname contact.mail contact.phone contact.address'.format(contact=contact))
    if zmienna == contact.lastname:
      found = 1
      print( 'contact.name contact.lastname contact.mail contact.phone contact.address'.format(contact=contact))
    if zmienna == contact.mail:
      found = 1
      print( 'contact.name contact.lastname contact.mail contact.phone contact.address'.format(contact=contact))
    if zmienna == contact.phone:
      found = 1
      print('contact.name contact.lastname contact.mail contact.phone contact.address'.format(contact=contact))
    if zmienna == contact.address:
      found = 1
      print('contact.name contact.lastname contact.mail contact.phone contact.address'.format(contact=contact))
  if found == 0:
    return "Nie ma takiego kontaktu"

while True:
  m = str(input("Wybierz funkcje:\n1 - dodaj nowy kontakt\n2 - edytuj kontakt\n3 - usun kontakt\n4 - pokaz wszystkie kontakty\n5 - wyszukaj kontakt\n"))
  if m == "1":
    # dodanie kontaktu
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
    search()
    pass
  else:
    print("niepoprawna opcja")
