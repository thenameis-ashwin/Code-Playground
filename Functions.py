# without argument without return-type

def sample1():
    a1 = 1
    b1 = 2
    sum1 = a1 + b1
    print("without argument without return-type")
    print("Sum :" + str(sum1) + "\n")


sample1()


# with argument without return-type

def sample2(a2, b2):
    sum2 = a2 + b2
    print("with argument without return-type")
    print("Sum :" + str(sum2) + "\n")


sample2(1, 2)


# without argument with return-type

def sample3():
    a3 = 1
    b3 = 2
    sum3 = a3 + b3
    return sum3


result3 = sample3()
print("without argument with return-type")
print("Sum :" + str(result3) + "\n")


# with argument with return-type

def sample4(a4, b4):
    sum4 = a4 + b4
    return sum4


result4 = sample4(1, 2)
print("with argument with return-type")
print("Sum :" + str(result4) + "\n")