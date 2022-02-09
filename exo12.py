from random import randint

while True:
 mot=input("entre un mot: ")
 if mot=="dice":
    print(randint(1,6))
 elif mot=="sum":
    sum= 0
    for i in range(101):
        sum= sum+i
    print(sum)
 elif mot=="password":
    nb= randint(10,15)
    for i in range(nb):
      print (randint(0,9))
 elif mot=="quit":
    exit()
 else:
     print("vous n'avais pas compris veille reussayer")
     mot= input("entre un mot:" )
   