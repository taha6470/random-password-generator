#ask user if they want to generate a password or not
#if no exit
#if yes ask the length of the password
#generate the password
#print the password
import string 
import random
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
def generate_password():
    password_length=int(input("Enter the length of the password : "))
    random.shuffle(characters)
    password=[]
    for x in range(password_length):
        password.append(random.choice(characters))
    random.shuffle(password)
    password="".join(password)
    print("Your password is {}".format(password))
while True:
    ans=input("Do you want to generate a password type (yes) to continue or (no) to stop : ")
    if ans.lower()=="no":
        break
    elif ans.lower()=="yes":
        generate_password()
    else:
        print("you selected an unkown option?")