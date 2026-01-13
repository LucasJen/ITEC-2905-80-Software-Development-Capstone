print("Hello Capstone!")
# Variables
school = "MCTC" # Pythong infers the data type
gpa = 3.7
students_in_class = 22 # Python prefers "snake case". Camel can be used, but is not convention


# if-statements
if gpa == 4: # no curly braces or semicolons. Python relies on indentation.
    print("WOW!")
elif gpa > 3:
    print("Awesome!")
else:
    print("sure!")


# lists
schools = ['MCTC', 'DCTC', 'North Hennepin Technical College']
if 'MCTC' in schools:
    print("MCTC is one of the schools in the list")

schools.sort() #sorts by alphabetical by default
print(schools)
schools.append('Century College') # appends value to end of list
print(schools)
schools.reverse() # returns None when printed. similar to null
print(schools)
# in operator

# strings
class_name = "Software Development Capstone"
print(class_name.upper()) #converts string to uppercase
print(len(class_name))
print(class_name.split()) # splits by default on blank space. Outputs a list of each word

if 'Capstone' in class_name: # looks for "capstone" within the classname string
    print("This must be the capstone")

#loops
#loops through a range
for x in range(10):
    print(x)

#loops - for loops over sequence
for s in schools: #loop over a list.
    print(s.upper())

for letter in school:
    print(letter * 10) #loops through each letter in the value of school and creats a single line with 10 of that letter.

data = [0] * 10
print(data)

more_data = [None] * 10 # could be used to create a place holder for future data to be added.
print(more_data)

# name = input('Enter your name ')
# while len(name) == 0: #condition to force user to input at least a single character
#     print('Please enter at least one character')
#     name = input('Enter your name ')

#empty strings are considered false
# not or ! can be used to check if something is untrue "while not name" or "while != name"

start_of_semester = True
winter = False

if winter: #true and false conditionals
    print('brr!')
else:
    print('it is not winter!')

#Dictionaries:

# Keys must be unique in key-value pairs

class_codes = { 2905: 'Capstone', 2560: 'Web', 2545: 'Java'} # The key is the class code, class name is the value

for code in class_codes: # loops over each key to output the value.
    print(code)
    print(class_codes[code])

for code, name in class_codes.items(): #creates a touple storing both the key and value.
    print(f'The class code is {code} and the name is {name}') # output is a formatted string

schools = ['MCTC', 'DCTC', 'North Hennepin Technical College']
first_two = schools[0:2] # first number is inclusive, second is exclusive. 
# includes element 0, 1, up to, but not including 2.
print(first_two)

last_school = school[-1]# prints the last item in the list
print(last_school)
last_two_schools = schools[-2:] # counts down from the end of the list, includes the last two elements.
print(last_two_schools)

school_name = 'Minneapolis Community and Technical College'
city = school_name[:11] #counts up to the 11th character
print(city)

# file IO
with open('data.txt') as f: #will read each line of the data file
    print(f.read())

with open('schools.txt', 'w') as f: # will output everything on a single line
    f.writelines(schools)

def get_name(): # creates a reusable function to collect a users name.
    print("Hello, pelae enter your name! ")
    name = input('your name is: ')
    return name

name = get_name()

#repo test