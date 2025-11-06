marks = int(input("Enter your marks: "))
if marks >= 70 and marks <= 100:
    print ("You have passed!")
elif marks <= 70:
    print ("You have failed")
else:
    print("Invalid Marks")

# 100 to 80 - A
# 80 to 70 - B
# 70 to 60 - C
# 60 below - Fail

if marks > 80 and marks <= 100:
    print ("Your grade is A. Passed")
elif marks < 80 and marks >= 70:
    print ("Your grade is B. Passed")