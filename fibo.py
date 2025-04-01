#Write a Python program to print Fibonacci series
n=(int(input("Enter number:")))
i=0
a=0
b=1

while (i<n):

    if(i<=1):
        Next=i
    else:
        Next=a+b
        a=b
        b=Next
    print(Next)
    i=i+1
    

