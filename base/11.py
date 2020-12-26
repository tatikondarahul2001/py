# input number in binary format and 
# converting it into decimal format

try:
  num = int(input("Input binary value: "), 2)
  print("num (decimal format):", num)
  print("num (binary format):", bin(num))  
except ValueError:
  print("Please input only binary value...")
