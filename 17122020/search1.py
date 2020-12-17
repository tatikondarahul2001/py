import re
pat=r"hi(de)="
if re.search(pat,"hidedede"):
 print("match hidedede")
if re.search(pat,"hi"):
 print("match hi")
