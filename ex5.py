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
