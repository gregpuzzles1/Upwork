# python version = 3.3.5
# platform = win32

# Functions dealing with unranked databases
# These functions will either work on, or create, unranked databases



def read_file(filename):
	d1 = {}
	d2 = {}
	dbkeys_persons = []
	dbvalues_pop = []

	f = open(filename, 'r')
	#data = sorted(f.readlines())
	data = sorted(f.readlines())
	lines = len(data)
	print ("lines = ", lines)
	print ("data = ", data)
	for line in range(0, lines):
		line = data[line].replace('"', '')
		line = line.split(',')
		print ("line = ", line)
		for dbitem in range(0, len(line)):
			if dbitem == 0:
				year = line[dbitem]
			elif dbitem == 1:
				gender = line[dbitem]
			elif dbitem == 2:
				name = line[dbitem]
			elif dbitem == 3:
				count = line[dbitem]
			else:
				print ("ERROR MESSAGE")

	# Create the lists that will be used in the databases.
	# Lists were initialized at the beginning of the funcion

		# create name/gender key
		dbkey_person = (name, gender)
		if dbkey_person != ('NAME', 'GENDER'):
			dbkeys_persons.append(dbkey_person)
			print ("dbkeys_persons = ", dbkeys_persons)

		# create count/rank value
		count = line[dbitem].replace('\n', '')
		dbvalue_pop = (count, None)
		if dbvalue_pop != ('COUNT', None):
			dbvalue_pop = (count, None)
			dbvalues_pop.append(dbvalue_pop)
			print ("dbvalue_popularitys = ", dbvalues_pop)

		# create pop_record
		print ("dbvalue_pop =", dbvalue_pop)
		d1[year] = dbvalue_pop
		print ("d1 {} =", dbkey_person, d1)

		d2[d1] = dbkey_person
		print ("d2 {} = ", d2)


	# return the resulting database

def add_name(db, name, gender, year, count):
	print ("Do you get here?")
	pass
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
	pass
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
	read_file(filename)


if __name__ == '__main__':
	main()
