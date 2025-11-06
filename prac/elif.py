while True:
    marks = int (input("Enter your marks: "))
    if marks >= 0 or marks <= 100:
        if marks >= 90:
            print ("Grade A.")
        elif marks >= 80:
            print ("Grade A.")
        else:
            print ("Below A Grade.")
    else:
        print ("Invalid Marks")

    a = 30
    while (a==30):
        print ("You are in loop")
        break
