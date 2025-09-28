#Concatenating two lists:

a = [1 ,2 ,3]
b = [4 ,5 ,6]
c = a + b

print(c)

#List Slicing

d = [4 ,5 ,6 ,9 ,-1 ,0]
print(d[1:3])
print(d[:])
print(d[:2])


ranged_list = range(1 ,10)
for i in ranged_list:
    print (i)



#Duplicated List
nums = [2 ,3 ,6 ,9 ,6 ,2 ,1 ,1 ,0 ,8 ,9 ,6 ,4 ,3 ,5 ,0 ,9 ,2 ,2 ,6 ,7 ,2 ,1 ,8]

#To print non duplicated contents
print(set(nums))

#To Check all available Methods to be used with a data type
print(dir(nums))

#nested lists

no_list = [
    [1 ,2 ,3],
    [4 ,5 ,6],
    [7 ,8 ,9],
    [0]
]

print(no_list[2][1])

for row in no_list:
    for column in row:
        print(column)