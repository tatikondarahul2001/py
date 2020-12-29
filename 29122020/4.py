class student:
 var=10
 def cal(self,x):
  self.num=x
  print(self.var,self.num)
obj1=student()
print(obj1.var)
obj1.cal(20)
obj2=student()
obj2.cal(30)
