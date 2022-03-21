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





