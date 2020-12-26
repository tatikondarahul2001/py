i = int(input("Input an integer: "))
o = str(oct(i))[2:]
h = str(hex(i))[2:]
h = h.upper()
b = str(bin(i))[2:]
d = str(i)
print("Decimal Octal Hexadecimal (capitalized), Binary")
print(d,'  ',o,' ',h,'                   ',b)
