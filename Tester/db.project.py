# python version = 3.3.5
# platform = win32

# Functions dealing with unranked databases
# These functions will either work on, or create, unranked databases

db = {}

#lines = 0

def read_file(filename):
	f = open(filename, 'r')
	#data = sorted(f.readlines())
	data = f.readlines()
	lines = len(data)

	sd = simplify_data(data, lines)

	ranking = None # set all ranking to None - unranked db

	for jj in range(0, len(sd)): # Create main Database (unranked) keys
		record = sd[jj]
		year = record[0]
		name = record[2]
		gender = record[1]
		count = record[3]
		baby_name = (name, gender)

		db[baby_name] = {}
		#add_name(db, name, gender, year, count, lines)
	print ("DATA BASE UPPER = ", db)

	for jj in range(0, len(sd)):
		record = sd[jj]
		year = record[0]
		name = record[2]
		gender = record[1]
		add_name(db, name, gender, year, count, lines)		

	print ("data_base = ", db)
	print ("lEN of DB = ", len(db))
	#return db

def simplify_data(data, lines):

	simpledata = []

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

def get_len_of_simplified_data():
	pass


def add_name(db, name, gender, year, count, lines):
	for key in db:
		#for jj in range(0, lines):
		popularity = (count, None, name)
		baby_name = (name, gender)

		if name == key[0]:
			db[baby_name][year] = popularity			

	return None

def new_names(db, gender, old_year, new_year):
	pass
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


if __name__ == '__main__':
	main()
