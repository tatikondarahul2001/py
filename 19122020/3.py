l1=[11,21,34,12,31]
l2=[23,25,54,24,20,27]
print("\nTest Input: **********\n Input List (1) : "+str(l1))
print(" Input List (2) : "+str(l2))
t3=[]
a=len(l1)<len(l2) and l1 or l2
t3= [l1[i]+l2[i] for i in range(len(a))]
print ("\nTest Result: **********\n Smaller list is : " + str(a))
print (" Resultant list is : " + str(t3))
