print("\n\n ----ESERCIZIO 1----")
import math
class point3D:
   def __init__(self,x,y,z):
     self.x=x
     self.y=y
     self.z=z
     
   def coord(poin):
     pto=[poin.x,poin.y,poin.z]
     print(pto)

   def newcoord(newpoint,a,b,c):
     newpoint.x=a
     newpoint.y=b
     newpoint.z=c
     pto2=[newpoint.x,newpoint.y,newpoint.z]
     print(pto2)
   
   def dist(p1,p2):
     dist=(p1.x-p2.x)**2+(p1.y-p2.y)**2+(p1.z-p2.z)**2
     print(math.sqrt(dist))
     

p=point3D(1.4,2.4,3.4)
p.coord()
p.newcoord(5.3,7.3,8.3)
pt2=point3D(9.3,6.3,3.3)
p.dist(pt2)



print("\n ----ESERCIZIO 2 -----")
indata=open('ex2_data_python_4.txt','r')
righe=indata.readlines()
indata.close()
M1=[]
M2=[]
s=0
for el in righe:
 s=s+1
 valori=el.split()
 try:
   M1.append(float(valori[0]))
   M2.append(float(valori[1]))
 except ValueError:
   print("Ho saltato la riga" ,s,"perché non vi è una coppia di numeri")
 
 
print(M1)
print(M2)

def bar(X,Y):
   xg=0.0
   yg=0.0
   for i in range(len(X)):
     xg=xg+X[i]/len(X)
     yg=yg+Y[i]/len(Y)
   print("coordinate del baricentro  (",xg, ",", yg, ")")

bar(M1,M2)




print("\n ----ESERCIZIO 3 -----")

class point2D:
 def __init__(self,xi,yi):
   self.x=xi
   self.y=yi
    
 def coord(self):
   coords=[self.x,self.y]
   print(coords)
    
 def bari(self,P):
   bar.x=0.0
   bar.y=0.0
   for l in range(len(P)):
     bar.x=bar.x+(P[l].x)/len(P)
     bar.y=bar.y+(P[l].y)/len(P)
   return bar

 def baricoord(self):
   coord_bar=[bar.x,bar.y]
   print(coord_bar)
  

  
import math
import sys
print('scrivi il nome del file da cui leggere pti')
file=input()
indata=open(file,'r')
righe=indata.readlines()
indata.close()
Xi=[]
Yi=[]
s=0
for el in righe:
 s=s+1
 valori=el.split()
 try:
   Xi.append(float(valori[0]))
   Yi.append(float(valori[1]))
 except ValueError:
   print("Ho saltato la riga" ,s,"perché non vi è una coppia di numeri")
print(Xi)
print(Yi)

points=[]
for k in range(len(Xi)):
   newp=point2D(Xi[k],Yi[k])
   newp.coord()
   points.append(newp)
newp.bari(points)
newp.baricoord()



print("\n ----ESERCIZIO  4 -----")
class campionato_sportivo:
 def __init__(self,names,scores):
   self.squadre=names
   self.score=scores
  
 def add (self):
   newname=input("Vuoi aggiungere una squadra? Scrivi il nome \n")
   names.append(newname)
   scores.append(random.randint(0,70))
   self.squad=names
   self.score=scores

 def punteggio (self):
   squad_name=input("Di quale squadra vuoi sapere il punteggio?\n")
   while squad_name not in self.squad:
     squad_name=input("Non c'è una squadra con questo nome,scegline un altro \n")
   i=self.squad.index(squad_name)
   print("La squadra", self.squad[i],"ha totalizzato punti", self.score[i])

 
 def squalifica(self):
   eliminato=input("Quale squadra vuoi eliminiare?\n")
   while eliminato not in self.squad:
     eliminato=input("Non c'è una squadra con questo nome,scegline un altro \n")
   i=self.squad.index(eliminato)
   punti_eliminato=self.score[i]
   self.squad.remove(eliminato)
   self.score.remove(punti_eliminato)
   
 def winner(self):
   i=self.score.index(max(self.score))
   print("Vince la squadra" ,self.squad[i], "con un totale di punti",   max(self.score))

 def retrocessione(self):
   last_score=min(self.score)
   last_index=self.score.index(min(self.score))
   last_name=self.squad[last_index]
   names_new=self.squad.copy()
   scores_new=self.score.copy()
   scores_new.remove(last_score)
   names_new.remove(last_name)
   last2_score=min(scores_new)
   last2_index=scores_new.index(min(scores_new))
   last2_name=names_new[last2_index]
   names_new2=names_new.copy()
   scores_new2=scores_new.copy()
   scores_new2.remove(last2_score)
   names_new2.remove(last2_name)
   last3_score=min(scores_new2)
   last3_index=scores_new2.index(min(scores_new2))
   last3_name=names_new2[last3_index]
   print( "Ultime classificate: \n", n-2, "posto", last3_name,last3_score, "\n", n-1, "posto:",last2_name,last2_score, "\n",n,"posto e ultimo:",last_name, last_score,)
     
         
import sys
import os
import random
print("Benvenuto in questo campionato! Quante squadre vuoi far giocare?")
n=input()
n=int(n)
names=[]
scores=[]
for i in range(n): 
  print("Inserisci il nome della squadra",i)
  squadra=input()
  while squadra in names:
   squadra=input("Questa squadra sta già giocando, scegli un altro nome \n")
  names.append(squadra)
  scores.append(random.randint(0,70))
  
campionato=campionato_sportivo(names,scores)
campionato.add()
campionato.punteggio()
campionato.squalifica()
campionato.winner()
campionato.retrocessione()



print("\n\n-------ESERCIZIO 5--------")
def dotpro(l1,l2):
  if len(l1)!=len(l2):
    raise TypeError("Le due liste devono avere stessa lunghezza")
  else:
    pro=0
    for i in range(0, len(l1)):
      pro=pro+l1[i]*l2[i]
  return pro


def matrix_product(X, Y):
   if len(X[0])!= len(Y) :
     raise NoneType
     print("Le matrici devono essere di dimensioni MXN NXP")
   else:
     result = [[0,0,0,0], [0,0,0,0], [0,0,0,0]]
     for i in range(len(X)):
      for j in range(len(Y[0])):
        for k in range(len(Y)):
          result[i][j] += X[i][k] * Y[k][j]
     return result



list1=[2.0,4.5,7.2,6.2]
list2=[0.5,7.5,2.4,7.0]
list3=[6.3,4.0,4.0]
A = [[12-0,7.3,3.5],[4.4 ,5.3,6.4],[7.4 ,8.3,9.3]]
B = [[5.3,8.6,1.2,2.4],[6.4,7.1,3.2,0.45],[4.3,5.3,9.3,1.3]]

dp=dotpro(list1,list2)
#dp2=dotpro(list1,list3)
mp=matrix_product(A,B)

def print_matrix(matrix):
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      print(str((matrix[i][j]))+"\t", end='')
    print("\n")

print("prodotto scalare",dp)
print("matrice prodotto")
print_matrix(mp)


print("-------ESERCIZIO 6-------- \n la risposta teorica è un commento nel codice")

"""
Le funzioni lambda sono funzioni senza nome, che svolgono operazioni semplici definite in un'unica linea di comando, e restituiscono un unico valore.

- lambda a: a+10 
incrementa di 10 unità il valore di a.
Esempio:
f= lambda a: a+10
print(f(2))
Risutato: 12

-f = lambda animale: animale.capitalize()
f è una funzione che rende maiuscola l'iniziale di una stringa di caratteri.
Esempio:
animali = ['cani', 'gatti', 'scoiattoli', 'alci']
f = lambda animale: animale.capitalize()
for animale in animali:
 print(f(animale))
Risultato:
Cani 
Gatti
Scoiattoli
Alci
"""

f= lambda a,b: (a+b)*0.5
media=f(5.0,0.7)
print(media)