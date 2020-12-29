class student:
 var=78
 def __init__(self,n):
  self.num1=n
  print(self.num1)
  print(id(self))
obj1=student(19)
print(id(obj1))
