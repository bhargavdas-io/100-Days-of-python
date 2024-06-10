import random
letters = ['a','b','c','d','e','f','g','h','i','j','k',
           'l','m','n','o','p','q','r','s','t','u','v','w',
           'x','y','z','A','B','C','D','E','F','G','H','I',
           'J','K','L','M','N','O','P','Q','R','S','T','U',
           'V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','(',')','*','+']
print ("Welcome to my Python Password generator.")


print (''' 
 ad8888888888ba
 dP'         `"8b,
 8  ,aaa,       "Y888a     ,aaaa,     ,aaa,  ,aa,
 8  8' `8           "88baadP""""YbaaadP"""YbdP""Yb
 8  8   8              """        """      ""    8b
 8  8, ,8         ,aaaaaaaaaaaaaaaaaaaaaaaaddddd88P
 8  `"""'       ,d8""
 Yb,         ,ad8"    
  "Y8888888888P"5
       ''')


inp_letters = int(input("How many letters would you like in your password? \n"))
inp_symbols = int(input("How many symbols would you like in your password? \n"))
inp_numbers = int(input("How many numbers would you like in your password? \n"))

password_list = []

for l in range(1,inp_letters+1):
    password_list += random.choice(letters)

for s in range(1,inp_symbols+1):
    password_list += random.choice(symbols)

for n in range(1,inp_numbers+1):
    password_list += random.choice(numbers)

random.shuffle(password_list)

generated = ''
for char in password_list:
    generated += char
print(f"Your password is : {generated}")
