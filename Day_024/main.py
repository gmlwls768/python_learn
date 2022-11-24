# file = open('Day_024/my_file.txt')
# file.close()
# with open("/Users/ocean/Desktop/my_file.txt") as file:  # absolute path
# with open("../../../Desktop/my_file.txt") as file:  # relative path
with open("Day_024/my_file.txt") as file:  # instead this can not use close
    contents = file.read()
    print(contents)

# with open("Day_024/my_file.txt", "a") as file:  # mode "w" is write "a" is append
#     file.write(" \n New text.")

with open("Day_024/new_file.txt", "w") as file:
    file.write("new file txt")  # is like touch if not exist file make new file
    # and is work only "w" mode
