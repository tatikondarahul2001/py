import re
string="she sells sea shells on sea shore"
pat="sea"
rep="ocean"
newstr=re.sub(pat,rep,string)
print(newstr)
