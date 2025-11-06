# Introduction
print ("Hello! My name is Angelica and I will be assisting you with the calculation of your final grade.")
name = input(("Enter your name: "))
idnum = input(("Enter your ID number: "))
print (f'Hello {name}! ID #{idnum}, Kindly input your marks for each subject.')
print (" ")

# Input of Grade
bio = int(input("Enter total grade in Biology: "))
chem = int(input("Enter total grade in Chemistry: "))
eng = int(input("Enter total grade in English: "))
maths = int(input("Enter total grade in Mathematics: "))
phy = int(input("Enter total grade in Physics: "))
print (" ")

# Calculation of Average and Percentage
average = int((bio+chem+eng+maths+phy)/5)
print (f'Your final average this grading is: {average}')
percentage = average%200
print (f'With the percentage of {percentage}%.')
print (" ")

# Pass or Fail
if average > 70:
    print ("You have passed!")
else:
    print ("You have failed.")
print (" ")

print (f'Thank you for letting me assist you, {name} ID #{idnum}. See you next time!')