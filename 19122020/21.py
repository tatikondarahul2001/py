
import os 
i = 1
  
# Write the path where to create the directories 
path ="/home / parrot/ Desktop / rahul/ py/"
try: 
    while i<5: 
        os.mkdir(path+"file"+str(i)) 
        i+= 1
except OSError: 
    print("File creation failed !!") 
