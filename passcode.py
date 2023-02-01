#importing modules
import random
import string
import os

#printing out my introduction string
print("Hello, this is your password generator")

#prompting length of passcode
length = int(input("\nPlease enter the length of your password: "))

#passcode data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

#combining all passcode data
all = lower + upper + num + symbols

#adding random sample and combining all passcode data with the length
#and joining them at the end
temp = random.sample(all,length)

password = "".join(temp)

print(password)

#I am pausing my cmd prompt to get the password
os.system("pause")

#I am sending this password to a txt file in this path
with open('password.txt', 'w') as f:
    f.write(password)
