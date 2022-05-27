a = int(input("Enter the dividend"))
b = int(input("Enter the divisor"))

#exception handling
#try-catch block

try:
    div = a/b
    print(str(div))
    print("try completed")

except ZeroDivisionError:
    print("Can't divide with divisor 0 value")

print("Program Completed")