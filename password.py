password=input()
specialcharacters=["!","@","#","$","%","^","&","*","(",")","_","+","<",">"]
l=len(password)
if(l<8):
    print("inavalid password..,,,")
upper=False
lower=False
digit=False
special=False
for i in password:
    if i.isdigit():
        digit=True
    elif i.isupper():
        upper=True
    elif i.islower():
        lower=True
    elif i in specialcharacters:
        special=True
if upper and lower and digit and special:
    print("valid password")
else:
    print("invalid password")
