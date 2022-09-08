#exercise 2
import random

names_string = input("Give me everybody's names, separated by a comma. ")

names = names_string.split(", ")

size = len(names)
random_name = random.randint(0,size-1)


print(names[random_name])


