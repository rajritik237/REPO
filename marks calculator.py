marks = int(input("Enter your marks :"))
if marks>=90:
    print("Excellent")
elif marks<90 and marks>=80:
    print("Good")
elif marks<80 and marks>=70:
    print("Average")
elif marks<70:
    print("Faild !")
else:
    print("Invalid Input!!!")
    