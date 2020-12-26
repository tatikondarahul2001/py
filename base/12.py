# function to convert given binary Value
# to an integer (decimal number)
def BinToDec(value):
  try:
    return int(value, 2)
  except ValueError:
    return "Invalid binary Value"

# Main code
input1 = "11110000"
input2 = "10101010"
input3 = "11111111"
input4 = "000000"
input5 = "012"

print(input1, "as decimal: ", BinToDec(input1))
print(input2, "as decimal: ", BinToDec(input2))
print(input3, "as decimal: ", BinToDec(input3))
print(input4, "as decimal: ", BinToDec(input4))
print(input5, "as decimal: ", BinToDec(input5))
