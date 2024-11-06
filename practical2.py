#WAP to accept a number ‘n’ and

#a. Check if ’n’ is prime
n = eval(input("enter value "))
if n>1:
 for i in range(2,n):
    if n % i == 0:
      print(n,"not a prime number ")
      break
 else:
   print(n,"prime number")
else:
   print(n,"not a prime number ")


#b. Generate all prime numbers till ‘n’
n = eval(input("enter value "))
for num in range(1,n):
   if num > 1:
     for i in range (2,num):
      if num % i == 0:
       break
     else:
      print(num,end =',')

#c. Generate first ‘n’ prime numbers
      
n = eval(input("enter value "))
count = 0
number = 2
while count < n:
    for i in range(2,number):
       if number % i == 0:
        number += 1
        break
    else:
        print(number,end=',')
        count += 1
        number += 1
