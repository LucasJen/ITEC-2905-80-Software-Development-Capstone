def camelcase(sentence):
    """ Convert sentence to camelCase, for example: " Display all books " is convert to "displayAllBooks" """
    title_case = sentence.title()
    # removes spaces
    upper_camel_cased = title_case.replace(' ','') 
    return upper_camel_cased[0:1].lower() + upper_camel_cased[1:]

def instructions():
    """ Provide instructions for the user """
    print('Enter a sentence and this program will convert it to camelcase.')

def main():
    banner()
    instructions()
    sentence = input('Enter your sentence: ')
    output = camelcase(sentence)
    print(output)

def banner():
    """ Display program name """
    message = "Awesome camelcase program!"
    stars = '*' * len(message)
    print(f'\n{stars} \n{message} \n{stars}\n')

if __name__ == '__main__':
    main()
