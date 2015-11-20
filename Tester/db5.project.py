# python version = 3.3.5
# platform = win32

# Functions dealing with unranked databases
# These functions will either work on, or create, unranked databases

db = {}
simpledata = []

def read_file(filename):
	"""Accepts a file, opens it, reads it line by line, simplifies the data, then adds names to the data base"""
	f = open(filename, 'r') # opens file for reading
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

	print ("data_base = ", db)
	print ("lEN of DB = ", len(db), '\n')
	return db

def get_years_male():
	"""Gets the years any male record is in the database"""
	sd = simpledata
	years_male = []
	for i in range(0, len(sd)):
		year = sd[i][0]
		if year not in years_male and sd[i][1] == "MALE":
			years_male.append(year)
	return years_male

def get_years_female():
	"""Gets the years any female record is in the database"""
	sd = simpledata
	years_female = []
	for i in range(0, len(sd)):
		year = sd[i][0]
		if year not in years_female and sd[i][1] == "FEMALE":
			years_female.append(year)
	return years_female

def get_all_years():
	sd = simpledata
	all_years = []
	for i in range(0, len(sd)):
		year = sd[i][0]
		if year not in all_years:
			all_years.append(year)
	return all_years


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

	for line in range(0, lines):
		line = data[line].replace('"', '').split(',') # strips off the quotes and splits items by the ','
		line[3] = line[3].replace('\n', '') # deletes the '\n' character at the end of each line
		if line[0] == "YEAR": 	# skips the first line
			continue			# skips the first line
		year = line[0]
		gender = line[1]
		name = line[2]
		count = line[3]

		s = year, gender, name, count
		simpledata.append(s) # adds a record to the list
	
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
		popularity = (count, rank)
		baby_name = (name, gender)

		for key in db:
			if name == key[0]:
				db[baby_name][year] = popularity # Creates the inner Database (unranked)
			else:
				continue			

	return None

def find_baby_years(baby_years, sorted_db):
	"""Finds all years for particular name"""
	for year, value in sorted_db:
		baby_years.append(year)
	return baby_years

def new_names(db, gender, old_year, new_year):
	"""Finds names that are new from year to year"""
	new = [] # initialize the list for new names

	if gender == "MALE":
		years = sorted(get_years_male())
	else:
		years = sorted(get_years_female())
	
	for i in range(1, len(years)):
		for mainKey in db:
			if mainKey[1] == gender:
				baby_years = []
				sorted_db = sorted(db[mainKey].items())
				find_baby_years(baby_years, sorted_db) # calls find_baby_years function 
				if old_year not in baby_years and new_year in baby_years:
					new_baby = (mainKey[0], new_year)
					new.append(new_baby)
				else:
					continue
			else:
				continue

		current_year = years[i]
		maxim = len(years)
		if current_year == years[maxim - 1]:
			break
		else:
			old_year = years[i]
			new_year = years[i + 1]

	print ("new names and year for {}S are = ".format(gender), sorted(new), '\n')
	return sorted(new)

	# return qualified names as a list of strings, alphabetically sorted

#################################################################################################

# Functions dealing with ranked databases

def rank_names_for_one_year(db, year):
	count_list = []
	for gender in ("MALE", "FEMALE"):
		for mainKey in db:
			#print (list(db[mainKey].values()))
			if mainKey[1] == gender:

				sorted_db = sorted(db[mainKey].items())
				for key, value in sorted_db:
					print (key, value[0])
					if year == key:
						print ("year / key = ", mainKey[0], year, key, value[0])
						baby_count = (mainKey[0], int(value[0]), year)
						count_list.append(baby_count)
					else:
						continue	

			else:
				continue

		print ("COUNT LIST = ", count_list)
		count_list.sort(key = getKey) #, reverse = True)
		print ("SORTED COUNT LIST = ", count_list)
		for jj in range(0, len(count_list)):
			#print ("XXXXXX", count_list[jj][1])
			x = count_list.pop()
			count = x[1]
			print ("count = ", count)
			print ("POP COUNT LIST = ", count_list)

	return None
	# this function should return None

def getKey(item):
	print ("item[1] = ", item[1])
	return item[1]

def counter():
	L = [("baby", 9999), ("aeuron", 100), ("pablo", 1234)]
	sorted(L, key=getKey)
	print ("L = ", L)

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
	filename = "small-modified.csv"
	x = read_file(filename) # calls the read_file function as sends it filename
	#print ("database = ", x)
	old_year = get_years_male()[0]
	new_year = get_years_male()[1]
	for gender in ("MALE", "FEMALE"):
		if gender == "MALE":
			old_year = get_years_male()[0]
			new_year = get_years_male()[1]
		else:
			old_year = get_years_female()[0]
			new_year = get_years_female()[1]

		new_names(db, gender, old_year, new_year)

	all_years = get_all_years()
	for jj in range(0, len(all_years)):
		year = all_years[jj]
		rank_names_for_one_year(db, year)
	#counter()
	#L = [("baby", 9999), ("aeuron", 100), ("pablo", 1234)]
	#sorted(L, key=getKey
	#print ("L = ", L)

if __name__ == '__main__':
	main()