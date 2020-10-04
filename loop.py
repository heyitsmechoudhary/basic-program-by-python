def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
a=float(input("enter 1st number"))
b=float(input("enter 2nd number"))
c=float(input("enter 3rd number"))
print(max_num(a,b,c))