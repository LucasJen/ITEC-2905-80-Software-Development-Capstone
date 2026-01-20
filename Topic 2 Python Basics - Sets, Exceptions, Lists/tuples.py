# sets

cats = set()
cats.add('Lion')
cats.add('Tiger')
print(cats)
cats.add('Cheetah')
print(cats)
cats.add('Cheetah')
print(cats)

# sets are not ordered, and are used to prevent duplicates

birds = {'robin', 'owl', 'swan'} # elements can be added at the creation of a set

#lists can be converted to sets to remove duplicates
# when converted to a set, the order is lost
#can be converted back into a set if preferred after duplicates are removed.