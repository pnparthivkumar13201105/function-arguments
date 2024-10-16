def factor(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factor(n-1)
    
num=int(input("enter the number which you want to factorize:--"))
if num<0:
    print("foctorial of negitive number does not exist")
else:
    print(f"factorial of {num} is {factor(num)}")        