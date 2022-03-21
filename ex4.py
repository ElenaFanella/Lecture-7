print("\n ----ESERCIZIO  4 -----")
import sys
import os
import random

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
     
        
print("Benvenuto in questo campionato! Quante squadre vuoi far giocare?")
n=input()
n=int(n)
names=[]
scores=[]
for i in range(n): 
  print("Inserisci il nome della squadra",i+1)
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