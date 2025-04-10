# Baby Name Popularity Database (Unranked + Ranked Functions)

# -------------------------------
# Unranked Database Functions
# -------------------------------

def read_file(filename):
    """
    Reads a CSV file and returns an unranked database.
    Sets all rankings to None.
    """
    db = {}
    with open(filename, 'r') as f:
        data = f.readlines()

    simpledata = simplify_data(data)

    for record in simpledata:
        year = int(record[0])
        gender = record[1]
        name = record[2]
        count = int(record[3])
        add_name(db, name, gender, year, count)

    return db


def simplify_data(data):
    """
    Loops through lines in the .csv file and creates a list of 4-tuples:
    (year, gender, name, count) for each baby
    """
    simpledata = []

    for line in data:
        line = line.replace('"', '').strip()
        if line.startswith("YEAR"):
            continue  # skip header
        parts = line.split(',')
        year = parts[0]
        gender = parts[1]
        name = parts[2]
        count = parts[3]
        s = (year, gender, name, count)
        simpledata.append(s)

    return simpledata


def add_name(db, name, gender, year, count):
    """
    Adds name, gender, year, and count to dictionary database.
    The rank is set to None (i.e., unranked).
    """
    key = (name, gender)
    if key not in db:
        db[key] = {}
    db[key][year] = (int(count), None)
    return None


def new_names(db, gender, old_year, new_year):
    """
    Returns a list of names of a given gender that appear in new_year
    but not in old_year. The result is alphabetically sorted.
    """
    new_names = []

    for (name, g), year_data in db.items():
        if g != gender:
            continue
        if new_year in year_data and old_year not in year_data:
            new_names.append(name)

    return sorted(new_names)

# -------------------------------
# Ranked Database Functions
# -------------------------------

def rank_names_for_one_year(db, year):
    """
    Calculates and assigns rank for all names in a given year.
    Male and female names are ranked separately.
    """
    gender_groups = {'MALE': [], 'FEMALE': []}

    for (name, gender), year_data in db.items():
        if year in year_data:
            count, _ = year_data[year]
            gender_groups[gender].append((name, count))

    for gender in gender_groups:
        ranked = sorted(gender_groups[gender], key=lambda x: -x[1])
        rank = 1
        prev_count = None
        skip = 0

        for i, (name, count) in enumerate(ranked):
            key = (name, gender)

            if count == prev_count:
                skip += 1
            else:
                rank += skip
                skip = 0

            db[key][year] = (count, rank)
            prev_count = count


def rank_names(db):
    """
    Ranks all names for all years, updating the database in place.
    Male and female names are ranked separately.
    """
    years = set()
    for name_data in db.values():
        years.update(name_data.keys())

    for year in years:
        rank_names_for_one_year(db, year)


def popularity_by_name(rdb, name, gender):
    """
    Returns a list of (year, rank) tuples for the given name and gender.
    Sorted by year. Returns [] if the name isn't found.
    """
    key = (name, gender)
    if key not in rdb:
        return []

    result = []
    for year in sorted(rdb[key].keys()):
        _, rank = rdb[key][year]
        result.append((year, rank))

    return result


def popularity_by_year(rdb, gender, year, top=10):
    """
    Returns a list of (rank, name) tuples for the top names of the given gender and year.
    Sorted by rank. If top exceeds actual names, return all.
    """
    results = []

    for (name, g), year_data in rdb.items():
        if g == gender and year in year_data:
            _, rank = year_data[year]
            if rank is not None:
                results.append((rank, name))

    results.sort()
    return results[:top]


def always_popular_names(rdb, gender, years=None, top=10):
    """
    Returns a list of names that are always in the top N in each year.
    If years is None, checks all years in the database.
    Sorted alphabetically.
    """
    if years is None:
        years = set()
        for data in rdb.values():
            years.update(data.keys())
        years = sorted(years)

    result = []

    for (name, g), year_data in rdb.items():
        if g != gender:
            continue

        always_top = True
        for y in years:
            if y not in year_data or year_data[y][1] is None or year_data[y][1] > top:
                always_top = False
                break

        if always_top:
            result.append(name)

    return sorted(result)


def increasing_rank_names(rdb, gender, old_year, new_year):
    """
    Returns a list of names (sorted alphabetically) whose ranks have improved
    (lower rank number) from old_year to new_year.
    """
    improved = []

    for (name, g), year_data in rdb.items():
        if g != gender:
            continue

        if old_year in year_data and new_year in year_data:
            old_rank = year_data[old_year][1]
            new_rank = year_data[new_year][1]

            if old_rank is not None and new_rank is not None and new_rank < old_rank:
                improved.append(name)

    return sorted(improved)

# -------------------------------
# Main Program (Example Usage)
# -------------------------------

def main():
    filename = "small.csv"  # Replace with your filename
    db = read_file(filename)

    print("\nUnranked database:")
    for key, value in db.items():
        print(f"{key}: {value}")

    rank_names(db)  # Rank everything in the database

    print("\nRanked database:")
    for key, value in db.items():
        print(f"{key}: {value}")

    print("\nPopularity of DANIEL (MALE):")
    print(popularity_by_name(db, "DANIEL", "MALE"))

    print("\nTop 3 names in 2010 (MALE):")
    print(popularity_by_year(db, "MALE", 2010, top=3))

    print("\nAlways popular names in top 3 (MALE):")
    print(always_popular_names(db, "MALE", top=3))

    print("\nNames that improved rank from 2009 to 2010 (MALE):")
    print(increasing_rank_names(db, "MALE", 2009, 2010))

    print("\nNew names in 2010 but not in 2009 (MALE):")
    print(new_names(db, "MALE", 2009, 2010))


if __name__ == '__main__':
    main()
