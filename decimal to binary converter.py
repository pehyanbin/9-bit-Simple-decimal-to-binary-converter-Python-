def ToBinary(number):
  n2_8 = n2_7 = n2_6 = n2_5 = n2_4 = n2_3 = n2_2 = n2_1 = n2_0 = 0 
  if number >= 256:
    number -= 256
    n2_8 += 1
    
  if number >= 128:
    number -= 128
    n2_7 += 1

  if number >= 64:
    number -= 64
    n2_6 += 1

  if number >= 32:
    number -= 32
    n2_5 += 1

  if number >= 16:
    number -= 16
    n2_4 += 1

  if number >= 8:
    number -= 8
    n2_3 += 1

  if number >= 4:
    number -= 4
    n2_2 += 1

  if number >= 2:
    number -= 2
    n2_1 += 1

  if number >= 1:
    number -= 1
    n2_0 += 1

  print(n2_8, end=" ")
  print(n2_7, end=" ")
  print(n2_6, end=" ")
  print(n2_5, end=" ")
  print(n2_4, end=" ")
  print(n2_3, end=" ")
  print(n2_2, end=" ")
  print(n2_1, end=" ")
  print(n2_0)


while True :
  continueCounter = int(input("Type 1 to start new operation and 0 to end operation. "))

  print("\n")

  if continueCounter == 0:
    break
  else :
    number = int(input("Enter a number ( range 0 - 511 ) : "))
    
    if number > 511:
        print("Number entered exceed limit for this program. Only type in number ranging from 0 - 511.")
        continue

    ToBinary(number)

    print("\n\n-----------------------------------------------------------\n")

print("======================================================\n")
print("End of operation. ")