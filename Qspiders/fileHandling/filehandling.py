import os
# os.chdir(r'/Users/prasxor/Developer/Learnings/Qspider-Python')
# print(os.listdir())
# os.mkdir("fileHandling files")
os.chdir(r'/Users/prasxor/Developer/Learnings/Qspider-Python/fileHandling files')

# modes 
# r - read
# w - write
# a - append
# x - create


# x - mode 

# f_obj = open("file1.txt", "x")
# print(f_obj)

# w - mode 
# f_obj = open("file1.txt", "w")
# print(f_obj)

# a - mode 
# f_obj = open("file1.txt", "a")
# print(f_obj)

# read the files 

with open("file1.txt", "r") as f_ob:
    print(f_ob.read())

with open("file1.txt", "a") as f_ob1:
    f_ob1.writelines(["Rain pattered on the window, a gentle lullaby.\n",
                    "Lost in thought, she absentmindedly twirled her hair.\n",
                    "The first snowflake landed, announcing winter's arrival.\n"])

with open("file1.txt", "r") as f_ob:
    print(f_ob.read())
    
    
# closed vs close()
# closed --> it checks the file is closed or not
# close() --> it will close the file