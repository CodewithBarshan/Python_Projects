#a-z
#0-9
#. --One time
#@ --One time
# . will be in 2 to 3 index position

import re
email_condition=r"^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

user_email=input("Please Enter Your email: ")

if re.search(email_condition,user_email):
    print("Right Email")
else:
    print("Wrong Email")    