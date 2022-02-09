from random import choice, randint


choice= input("oui pour lance un dé non si tu veux pas")
while choice=="oui":
    print(f"vous avez dé de  {randint(1,30)}  ")
    choice= input("oui pour lance un dé non si tu veux pas: ")