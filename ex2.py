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



