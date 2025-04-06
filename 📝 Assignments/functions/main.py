#  Functions   (code block that does a task)
# A Function is a block of code that performs a specific task, We can call functions multiple times without repeating the code.


def calculateGmean(a, b):
    mean = (a * b)/(a + b)
    print(mean)

def isGreater(a, b):
    if(a > b):
        print("First number is graeter")
    else:
        print("Second number is greater or equal")

def isLesser(a, b):
    pass

a = 9
b = 8
isGreater(a, b)
calculateGmean(a, b)
# gmean1 = (a * b)/(a + b)
# print(gmean1)

c = 7 
d = 6
isGreater(c, d)
calculateGmean(c, d)
# gmean2 = (a * b)/(a + b)
# print(gmean2)

