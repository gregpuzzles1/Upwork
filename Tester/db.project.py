# python version = 3.3.5
# platform = win32

# Functions dealing with unranked databases
# These functions will either work on, or create, unranked databases


def read_file(filename):
	db1 = {}
	db2 = {}
	persons = []
	popularities = []
	names_list = []
	year_list = []

	f = open(filename, 'r')
	#data = sorted(f.readlines())
	data = f.readlines()
	lines = len(data)

	sd = simplify_data(data, lines)
	print ("simplify_data(data, lines) = ", sd)
	print ("year_names = ", sd[0][1])


"""def yrnames(data, lines):

	year_names = []

	simplify_data(data, lines)

	year_name = (line[2], line[0])
	year_names.append(year_name)

	#return year_names"""

def simplify_data(data, lines):

	simpledata = []
	year_names = []

	for line in range(0, lines):
		line = data[line].replace('"', '').split(',')
		line[3] = line[3].replace('\n', '')
		#print ("line = ", line, '\n')

		year = line[0]
		gender = line[1]
		name = line[2]
		count = line[3]

		s = year, gender, name, count
		simpledata.append(s)

		year_name = (line[2], line[0])
		year_names.append(year_name)

	return (simpledata, year_names)

		#print ("xx = ", year, gender, name, count)

	"""if line[0] != 'YEAR':


	# Create the lists that will be used in the databases.
	# Lists were initialized at the beginning of the funcion

			# set all ranking to None
			ranking = None 

			# create name/gender key list
	

			person = (name, gender)
			persons.append(person)
			print ("persons = ", persons, '\n')

			#if year == 2010 and 

			# create count/rank value list
			# pop = popluarity
			count = line[3]
			popularity = (count, ranking, name)
			popularities.append(popularity)
			print ("popularities = ", popularities, '\n')
			print ("popularities[0][2] = ", popularities[0][2])


			db1[year] = popularity
			print ("db1 = ", person, db1)

			db2 = {person: db1}
			print ("db2 = ", db2, '\n')

	return db2"""	

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
	print ("database = ", x)


if __name__ == '__main__':
	main()
