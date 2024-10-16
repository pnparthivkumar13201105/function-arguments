def cube(number):
    return number*number*number

def div3(number):
    if number%3==0:
        return cube(number)
    else:
        return False
i=int(input("enter any number you want to cube which is dividsable by 3:--"))
print(div3(i))    