# I/O File Handling   (I/O = Input/Output)
# Opening a file, reading or writing to it, and then closing it afterward.
# 1. Open the file
# 2. Read/Write in the file
# 3. Close the file

# READING A FILE

f = open('myfile.txt', 'r')
# print(f)
text = f.read()
print(text)
f.close()

# WRITING A FILE

f = open('myfile2.txt', 'w')
f.write('Hello World!')
f.close()

# # with automatically closes the file, no need to use close()

with open('myfile3.txt', 'a')as f:
    f.write('Hey I am inside with')
