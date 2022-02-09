# from re import T


# a=6
# b=6
# c=a+b
# print(c)
# print(" la valeur de la somme est",c)
# d= "hello my friend"
# print(d)
# L=[1,2,3,4,5,'hello']
# print(L)
# print(L[1])
# print(L[0])
# L1=L[1:3]
# print(L1)
# L2=L[:2]
# print(L2)
# L3=L[2:]
# print(L3)
# T=2,6,3,5,
# P=1,"S",5,5
# S=P+T
# print (S)

# K= len(T)
# print (K)
# m=6
# n=4
# if(m>n):
#     print(m, "est plus grand que", n)
# else:
#      print(n, "est plus grand que", m)

# for i in T:
#     c= i*i
#     print(c)
# Q=[i*i for i in T]
# print(Q)

# def carre(x):
#     return x*x
# x= carre(6)
# print(x)
# i=0
# while i<len(T):
#      o= 10*T[i]*T[i]
#      print(o)
#      i= i+1

from multiprocessing.sharedctypes import Value
from this import d
H= [1,2,3,4,5,6,7,9]

i=0
while i<len(H):
   r=2*H[i]-4
   print(r)
   i=i+1

Y= [2*k-
4 for k in H]
print(Y)


for i in H:
    a=2*i-4
    print(a)
D={"Belgique":"Bruxelle","Alemagne":"Belrin","Hollande":"Amsterdam"}
for key, Value in D.items():
       print(key,":",Value)
print(D["Belgique"])   
