search = list()

choice - ''
while choice != 'done':
	choice = input('what ingredients?: ')
	if choice != 'done':
		search.append(choice)
w = tuple(search)
elements = ((1, 'salmon potato salt'), (2, 'meat pasta salt'), (3, 'milk eggs salt'), (4, 'fish'))
for name, ingredients in elements:
	if any(x in ingredients for x in w):
		#print ('Name: {}, Ingredients: {}'.format(name, ingredients))
		print (name, ingredients)
	else:
        continue
