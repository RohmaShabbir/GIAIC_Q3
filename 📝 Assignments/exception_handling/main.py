#  Exception Handling
# Exception = An error that occurs during the run-time of a program (while the program is running)
# Exception Handling = A mechanism that prevents the program from crashing by using try, except, else, and finally.
# try	       Write the code where an error might occur.
# except	   If an error occurs, control comes here.
# else	       If no error occurs, this part runs.
# finally	   This always runs, whether there's an error or not.

a = input("Enter the number: ")
print(f"Multiplication table of {a} is: ")

try:
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print("Invalid Input")

print("End of program!")

