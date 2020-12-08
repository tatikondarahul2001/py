def reverse(s):
 if (len(s)==0):
  return s
 else:
  return reverse(s[1:]) + s[0]
s=input("enter:")
print ("The original data is : ",end="")
print (s)
print ("The reversed data is : ",end="")
print (reverse(s))
