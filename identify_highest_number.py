#Define the variables for the 5 digits and then ask the user to input them.

digit1 = float(input("Please input the first number: "))
digit2 = float(input("Please input the second number: "))
digit3 = float(input("Please input the third number: "))
digit4 = float(input("Please input the fourth number: "))
digit5 = float(input("Please input the fifth number: "))

#Compare digit 1 to the other four variables.
if digit1 > digit2 and digit1 > digit3 and digit1 > digit4 and digit1 > digit5:
  #If digit 1 is the highest number, print. 
  print("The highest number is: ", digit1)

#Compare digit 2 to the other four variables.
if digit2 > digit1 and digit2 > digit3 and digit2 > digit4 and digit2 > digit5:
  #If digit 2 is the highest number, print. 
  print("The highest number is: ", digit2)

#Compare digit 3 to the other four variables.
if digit3 > digit1 and digit3 > digit2 and digit3 > digit4 and digit3 > digit5:
  #If digit 3 is the highest number, print. 
  print("The highest number is: ", digit3)

#Compare digit 4 to the other four variables.
if digit4 > digit1 and digit4 > digit2 and digit4 > digit3 and digit4 > digit5:
  #If digit 4 is the highest number, print. 
  print("The highest number is: ", digit4)

#Compare digit 5 to the other four variables.
if digit5 > digit1 and digit5 > digit2 and digit5 > digit3 and digit5 > digit4:
  #If digit 5 is the highest number, print. 
  print("The highest number is: ", digit5)

#Compare digits 1 to 5 when two or more of them have the similar highest value.
if digit1 == digit2 or digit1 == digit3 or digit1 == digit4 or digit1 == digit5 or digit2 == digit3 or digit2 == digit4 or digit2 == digit5 or digit3 == digit4 or digit3 == digit5 or digit4 == digit5:
  #If two or more numbers are the highest, print that digit.
  print("The highest number is: ", digit1 or digit2 or digit3 or digit4 or digit5)
