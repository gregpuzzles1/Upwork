# python version = 3.3.5
# platform = win32

# Functions dealing with unranked databases
# These functions will either work on, or create, unranked databases

db = {}
simpledata = []

def read_file(filename):
	f = open(filename, 'r')
	data = sorted(f.readlines())
	#data = f.readlines()
	lines = len(data)

	sd = simplify_data(data, lines) # simplifies the data into a list

	for jj in range(0, len(sd)): 
		record = sd[jj]
		name = record[2]
		gender = record[1]
		year = record[0]
		count = record[3]

		add_name(db, name, gender, year, count)	# calls the add_name function

		for jj in range(0, len(sd)): 
			record = sd[jj]
			name = record[2]
			gender = record[1]
			year = record[0]
			count = record[3]

			#print ("TEST - Db[0] = ", db)
			for key, value in db:
				pass
				#print ("key = ", key)
				#print ("value = ", value)
	print ("data_base = ", db)
	print ("lEN of DB = ", len(db))
	return db

def get_genders():
	sd = simpledata
	genders = []
	for i in range(0, len(sd)):
		gender = sd[i][1]
		if gender not in genders:
			genders.append(gender)
	return genders

def get_years():
	sd = simpledata
	years = []
	genders = []
	for i in range(0, len(sd)):
		year = sd[i][0]
		if year not in years:
			years.append(sd[i][0])
	return years

"""def test(db):
	current = []

	for mainKey in db:
		print (mainKey)
		for key, val in db[mainKey].items():
			print (key,val[0])
			print (mainKey[0], key)
			current.append((mainKey[0], key))
	for item in sorted(current):
		print ("ITEM = ", item)
	years(current)"""


def simplify_data(data, lines):
	"""Loops thru the lines in .csv file and creates a list of 4 tuples for each baby"""
	#simpledata = []

	for line in range(0, lines):
		line = data[line].replace('"', '').split(',')
		line[3] = line[3].replace('\n', '')
		if line[0] == "YEAR":
			continue
		year = line[0]
		gender = line[1]
		name = line[2]
		count = line[3]

		s = year, gender, name, count
		simpledata.append(s)
	
	return (simpledata)


def add_name(db, name, gender, year, count):
	"""Adds name, gender, year, and count to dictionary database"""
	sd = simpledata

	baby_name = (name, gender)

	db[baby_name] = {} # Create main Database (unranked) keys

	for jj in range(0, len(sd)):
		record = sd[jj]
		year = record[0]
		name = record[2]
		gender = record[1]
		count = record[3]

		rank = None # set all ranking to None - unranked db
		popularity = (count, rank, name)
		baby_name = (name, gender)

		for key in db:
			if name == key[0]:
				db[baby_name][year] = popularity # Creates the inner Database (unranked)
			else:
				continue			

	return None

def new_names(db, gender, old_year, new_year):

	new = [] # initialize the list of new name
	for mainKey in db:

		years = [] # initialize the years list
		sorted_db = sorted(db[mainKey].items())

		for year, value in sorted_db:
			if year not in years:
				years.append(year) # create a years list
			else:
				continue

		#print ("KEYS = ", years)
		#print ("NAME = ", mainKey[0])
		for year, value in sorted_db:
			print ("Year = ", year)
			print ("value = ", value)
			print (old_year, new_year)
			if old_year == year:
				placeholder = True
			else:
				placeholder = False
			if new_year == year:
				placeholder1 = True
			else:
				placeholder1 = False

			if not placeholder and placeholder1:
				print ("mainKey[0], year = ", mainKey[0], year)
				newbie = (mainKey[0], year)
				new.append(newbie)
				print ("newbie = ", newbie)
				print ("new = ", new)
				break
			else:
				continue
	#print ("new = ", new)
	return new

	# return qualified names as a list of strings, alphabetically sorted

#################################################################################################

# Functions dealing with ranked databases

def rank_names_for_one_year(db, year):
	pass
	# this function should return None

def rank_names(db):
	pass
	# this function should return None

def popularity_by_name(rdb, name, gender):
	ranking = None 
	count = line[dbitem]
	popularity = (count, ranking)
	popularities.append(popularity)
	print ("popularitys = ", popularities, '\n')
	
	# It finds the popularity counts for all years included in the db for name,
	# assemble them in a list of tuples (year, rank), and return the list. If
	# db has no records for name, return []. Sort multiple years’ records (tuples) by year

def popularity_by_year(rdb, gender, year, top=10):
	pass
	# It finds for the specified year, the top popular names and returns them in
	# a list of tuples (rank, name). Sort multiple tuples in your return list by
	# rank most common first.

def always_popular_names(rdb, gender, years=None, top=10):
	pass
	# return list of strings

def increasing_rank_names(rdb, gender, old_year, new_year):
	pass
	# return list

def main():
	filename = "small.csv"
	x = read_file(filename)
	#print ("database = ", x)
	years = get_years()
	genders = get_genders()
	for i in range(0, len(years)):
		current_year = years[i]
		maxim = len(years)
		if current_year != years[maxim - 1]:
			old_year = years[i]
			new_year = years[i + 1]
			new_names(db, genders, old_year, new_year)
		else:
			break

if __name__ == '__main__':
	main()