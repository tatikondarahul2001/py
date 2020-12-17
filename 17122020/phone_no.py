import re
phn="342-232-4545"
if re.search("w{3}-w{3}-w{4}",phn):
 print("valid phone number !!!")
else:
 print("not a valid number !!!")
