import re
pat=r"[a-z A-Z]+\d+"
matches=re.findall(pat,"LXI 2013,VXI 2015,VDI 2015,VDI 20104,Maruthi suzuki cars in india")
for match in matches:
 print(match,end=" ")
