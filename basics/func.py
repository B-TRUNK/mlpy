#function with a While loop
def count(number):


    while(number >= 0):
        number -= 1
        print(number)
            


count(10)

print('\n\n')

animal_list = ['Dog' ,'Pigeon' ,'Wolf']

#function with a for loop
def animal_display(some_list):

    for animal in some_list:
        print(animal)

animal_display(animal_list)



input_name = input("Please Enter Your Name : ")
def say_hello(name):
    print(f"Hello , {name}")

say_hello(input_name)


def mul():
    num_1 = input("Please Input 1st Number for Multiplication :")
    num_2 = input("Please Input 2st Number for Multiplication :")

    multiplied_result = (num_1*num_2)
    return multiplied_result

mul()