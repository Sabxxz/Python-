num1 = input("enter the first number")
num2 = input("enter the second number")


def addi(a,b):   
    addi_result = int(a)+int(b)
    return addi_result
    


sum = int(num1)+int(num2)
print(sum)
print(f"the sum of {num1} and {num2} is {sum}")

a = input("enter valuue for a")
b = input("enter value for b")
addi_result1 = addi(a,b)
print(f"the result of math between {a} and {b} is {addi_result1}")
