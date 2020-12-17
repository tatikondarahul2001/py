import re
string="she sells sea shells"
pat1="shells"
if re.search(pat1,string):
 print("found")
else:
 print("not found")

