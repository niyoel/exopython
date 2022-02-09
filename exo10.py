from itertools import count


password= input("crée votre mot de pass: ")
while len(password < 12):
  password = input("votre password est tre courte veuille entre un autre: ")
  