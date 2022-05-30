# # Reading an entire file
# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
# print(file_object)
# print(contents)


# # Reading a file line by line
# filename = 'pi_digits.txt'
# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())


# Making the file object available out of the with block
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())