import random
import math

total= 1000 #number of dart
hit=0 #number of dart fall inside the circle's part
ndart=0 #number of threw dart

for dart in range(0,total): #throw the dart
    Xrand = random.randint(0,1)
    Yrand = random.randint(0,1)
    ndart += 1
    # Check Condition
    if (Xrand**2)+(Yrand**2)<=1:
        hit += 1

print("Total : " +str(total))
piPercobaan = (hit/total)*4 
print("Jumlah hit " + str(hit))
print("Pi percobaan : " + str(piPercobaan))
print("Pi hasil analitik yaitu :  " + str(math.pi))
error=(piPercobaan/math.pi)*100
error= 100-error
if error <0 : #check if error below zero to turn it to positive number
    error*-1
print("Error : " + str(error) + "%") 
