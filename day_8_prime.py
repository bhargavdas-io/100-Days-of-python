
n = int(input("Enter a number: "))
def prime_checker(n):
    flag = True
    for i in range(2, n):
        if n % i == 0:
            flag = False
    if flag:
        print("Its Prime")
    else:
        print("Its not Prime")
   
prime_checker(n)