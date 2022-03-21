print("\n ----ESERCIZIO 3 -----")
import math
import sys
class point2D:
 def __init__(self,xi,yi):
   self.x=xi
   self.y=yi
    
 def coord(self):
   coords=[self.x,self.y]
   print(coords)
    
 def bari(self,P):
   bar=point2D(0,0)
   for l in range(len(P)):
     bar.x=bar.x+(P[l].x)/len(P)
     bar.y=bar.y+(P[l].y)/len(P)
   return bar

 def baricoord(self):
   coord_bar=[bar.x,bar.y]
   print(coord_bar)
  

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
bar=newp.bari(points)
newp.baricoord()
