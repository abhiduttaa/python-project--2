import random
import string
# print(string.punctuation)
pass_len= 8
charval= string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(pass_len):
     password= password + random.choice(charval)

print("Your random Password is:",password)
# print(string.digits)

# val=random.choice(["a","b","c","e"])
# print(val)
# print(random.choice("hello"))

