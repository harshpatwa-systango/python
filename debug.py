import pdb
def function1(num):
    pdb.set_trace()
    return num + num
def function2(num):
    return int(num) * int(num)

number=int(input("Enter Number:"))
result1= function1(number)
result2= function2(result1)

print(result2)