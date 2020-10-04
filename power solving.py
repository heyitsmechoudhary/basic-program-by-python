def raise_to_power(base_num,pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
a=int(input("pelease enter 1st value : "))
b=int(input("please enter power : "))

print(raise_to_power(a,b))