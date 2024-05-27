import random
import string

def pwrd(n):

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits)
    ]

    all_chars = lowercase + uppercase + digits 
    password += random.choices(all_chars, k=n-3)

    random.shuffle(password)
    
    return ''.join(password)

passw_num=int(input("How many passwords do you want to generate?:"))
if passw_num==1:
    print("Generating " +str(passw_num)+" password")
else:
    print("Generating " +str(passw_num)+" passwords")
print("Minimum length of password should be 3")
for i in range(passw_num):
    n=int(input("Enter the length of Password #" + str(i+1) + " "))
    if n < 3:
        p = 3
        print(pwrd(p))
    else:
        print(pwrd(n))
