p=int(input("enter percentage of student:"))
if p>90:
    print("FIRST CLASS")
elif p>=70 or p<90:
    print("SECOND CLASS")
elif p>60  or p<70:
    print ("THIRD CLASS")
else:
    print("PASS")
