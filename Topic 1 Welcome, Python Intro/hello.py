# Part 1

# data type is implied
name = input("What is your name? ") # variable to store user's name.
monthOfBirth = input("What month were you born in? ") # Variable to store users birth month

print("Welcome, " + name)
print("You have " + str(len(name)) + " letters in your name.")

if monthOfBirth == "January":
    print("Happy Birth Month")
else:
    print("It is not your birth month.")

#Part 2 -- Lists of classes

class_list = [] # creates an empty list to store future data
class_name = input('Input a class that you are taking this semester. Enter to quit. ')
while class_name: # loop through to add elements to the list
    class_list.append(class_name)
    class_name = input('Input a class that you are taking this semester. Enter to quit. ')
print(class_list) # print entire list

for c in class_list: # loop through and print each class name, one per line.
    print(c) #print list, one per line.