def GCD(a,b):
    if(b==0):
        return a
    else:
        return GCD(a,a%b)
    
num1=int(input("Enter a number 1="))
num2=int(input("Enter a number 2="))
gcd=GCD(num1,num2)
print("The gcd of num1 and num2 is=",gcd)