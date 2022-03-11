# part 1
bad_fruits = []
good_fruits = []
fruits_list=[
    {'name':'apple','shape':'square', 'mass':470},
    {'name':'mango','shape':'square', 'mass':491},
    {'name':'lemon','shape':'square', 'mass':450},
    {'name':'orange','shape':'circle', 'mass':470}
]

# part 2
for fruit in fruits_list:
    if fruit['shape']=='square' and fruit['mass']<490:
        good_fruits.append(fruit['name'])
    else:
        bad_fruits.append(fruit['name'])
        
# part 3
for fruit in good_fruits:
    print(fruit+" is a good fruit")

for fruit in bad_fruits:
    print(fruit+" is a bad fruit")
