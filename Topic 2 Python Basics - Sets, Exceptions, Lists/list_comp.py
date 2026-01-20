classes_regiestered = ['ITEC 1150', 'ITEC 1100', 'ENGL 1340', 'MATCH 1100']

only_itec = [ c for c in classes_regiestered if c.startswith('ITEC')]

print(only_itec)

high_temps = [-1, 78, 72, 67, -1, 51, 87, 82, -1, 54, 67, 78, -1, 70]

only_real_measurements = [ temp for temp in high_temps if temp != -1]
print(only_real_measurements)

number_list = [2, 4, 6]
number_list_plus_one = [num + 1 for num in number_list]
print(number_list_plus_one)