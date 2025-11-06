# 100 to 80 - A
# 80 to 70 - B
# 70 to 60 - C
# 60 below - Fail
marks = int(input("Enter your marks: "))
if marks >= 100 or marks<=0:
    print("Invalid Marks")
elif marks>=80:
    print ("A Grade")
elif marks<80 and marks>=70:
    print ("B Grade")
elif marks<70 and marks>=60:
    print ("C Grade")
else:
    print("Invalid Marks")