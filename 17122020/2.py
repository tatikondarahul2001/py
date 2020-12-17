import re
string="she sells sea shells"
pat1="sea"
if re.match(pat1,string):
 print("found")
else:
 print("not found")
