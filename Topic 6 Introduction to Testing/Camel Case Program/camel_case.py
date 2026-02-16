def camel_case(sentence):
    # do some stuff
    words = sentence.split(' ')
    return words[0].lower() + ''.join(word.capitalize() for word in words[1:])

def main():
    sentence = input('Enter your sentence: ')
    camelcased = camel_case(sentence)
    print(camelcased)

if __name__ == '__main__':
    main()
    
