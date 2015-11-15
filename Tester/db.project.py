# python version = 3.3.5
# platform = win32

# Functions dealing with unranked databases
# These functions will either work on, or create, unranked databases


def read_file(filename):
	f = open(filename, 'r')
	#data = sorted(f.readlines())
	data = f.readlines()
	lines = len(data)

	sd = sorted(simplify_data(data, lines))

	b = babies(sd)
	y = years(sd)

	db = {}
	db_pop = {}

	for baby in b:
		db[baby] = None	
		#print ("data_baseABOVE = ", db)
		for jj in range(0, len(sd)):
			record = sd[jj]
			year = record[0]
			name = record[2]
			gender = record[1]
			popularity = (record[3], None, record[2])
			baby_name = (record[2], record[1])
			#popularities.append(popularity)
			#db_pop[year] = popularity
			#db_pop = {year: popularity}
			tmp_pop = {year: (popularity)}
			tmp = {(baby_name): tmp_pop}
			#db_pop = {year: (popularity)}
			db_pop.update(tmp_pop)
			print ("DB_POP = ", db_pop)

			db.update(tmp)

			x = db[baby_name][year][2]
			print ("db[baby_name][year][2] = ", x)
			#db = {(baby_name): db_pop}
			"""if year not in db_pop:
				db_pop = {year: popularity}
				print ("db_POP = ", db_pop)
				db.update(db_pop)

				db = {baby_name : db_pop}	

				#db = db_pop"""
					

	print ("data_base = ", db)
	print ("lEN of DB = ", len(db))
	return db

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

def create_db(sd, b, y):
	
	ranking = None # set all ranking to None - unranked db

	pop_record = []
	year_names = []

	for jj in range(0, len(sd)):
		record = sd[jj]
		year = record[0]
		name = record[2]
		gender = record[1]
		count = record[3]
		add_names_db = add_name(db, name, gender, year, count)
		print ("DB = ", add_names_db)
		print ("LEN = ", len(add_names_db))
	print ("LEN FINAL = ", len(add_names_db))
	return add_names_db

def babies(sd):
	babies = []
	for i in range(0, len(sd)):
		record = sd[i]
		name = record[2]
		gender = record[1]
		year = record[0]
		baby = (name, gender)
		if baby not in babies:
			babies.append(baby)

	return babies

def years(sd):
	years = []
	for i in range(0, len(sd)):
		record = sd[i]
		year = record[0]
		if year not in years:
			years.append(year)
	return years


def test(sd):
	pass


def add_name(db, name, gender, year, count):

	popularity = (count, None, name)
	baby_record = (name, gender)
	db_pop[year] = popularity
	db[baby_record] = db_pop 
	return db
	# return None

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
