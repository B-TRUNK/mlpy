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