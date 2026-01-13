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