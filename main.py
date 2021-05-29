contacts = []

class Contact:
  def __init__(self, name, lastname, mail, phone, address):
    self.name = name
    self.lastname = lastname
    self.mail = mail
    self.phone = phone
    self.address = address

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
    # wyszukanie kontaktu
    pass
  else:
    print("niepoprawna opcja")
