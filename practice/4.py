num = input()
for i in range(2, num//2):
    if(num % i ) == 0 :
        print(num ,"is not prime number")
        break 
    else:
        print(num , "is a prime number")
    x = int(input("Enter a number: "))
    to_uns(x)