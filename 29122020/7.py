class ABC:
 cvar=0
 def __init__(self,var):
  ABC.cvar+=1
  self.var=var
  print("Object value is : ",var)
  print("Class value is : ",ABC.cvar)
obj1=ABC(10)
obj2=ABC(20)
obj3=ABC(30)
obj4=ABC(40)
obj5=ABC(50)
