# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}


# test function by updating damages
def update_values(string_list, multiplier_dict):
    new_list = []
    for item in string_list:
        if item.endswith("M"):
            key = "M"
            base_value = float(item[:-1])  # Remove the 'M' and convert to float
            new_value = base_value * multiplier_dict.get(key, 1)
        elif item.endswith("B"):
            key = "B"
            base_value = float(item[:-1])  # Remove the 'B' and convert to float
            new_value = base_value * multiplier_dict.get(key, 1)
        else:
            new_value = item  # Keep the original value
        new_list.append(new_value)
    return new_list


updated_damages = update_values(damages, conversion)


# print(updated_damages)
# 2
# Create a Table
# Create and view the hurricanes dictionary
def hurricane_dict(
    hurricaneName,
    hurricaneMonths,
    hurricaneYears,
    hurricaneMaxWinds,
    hurricaneAreas,
    hurricaneDamage,
    hurricaneDeaths,
):
    hurricane_dictionary = {
        hurricaneName[i]: (
            hurricaneName[i],
            hurricaneMonths[i],
            hurricaneYears[i],
            hurricaneMaxWinds[i],
            hurricaneAreas[i],
            hurricaneDamage[i],
            hurricaneDeaths[i],
        )
        for i in range(len(hurricaneName))
    }
    return hurricane_dictionary


# Create dictionary of hurricanes
dictOfHurricane = hurricane_dict(
    names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths
)

# print(dictOfHurricane)

# 3
# Organizing by Year


# create a new dictionary of hurricanes with year and key
def hurricane_dict_year(dict_of_hurricane):
    hurricane_list_by_year = {}
    for details in dict_of_hurricane.values():
        name, month, year, max_wind, area, damage, death = details
        if year not in hurricane_list_by_year:
            hurricane_list_by_year[year] = {
                "hurricaneName": [],
                "hurricaneMonths": [],
                "hurricaneYears": [],
                "hurricaneMaxWinds": [],
                "hurricaneAreas": [],
                "hurricaneDamage": [],
                "hurricaneDeaths": [],
            }
        hurricane_list_by_year[year]["hurricaneName"].append(name)
        hurricane_list_by_year[year]["hurricaneMonths"].append(month)
        hurricane_list_by_year[year]["hurricaneYears"].append(year)
        hurricane_list_by_year[year]["hurricaneMaxWinds"].append(max_wind)
        hurricane_list_by_year[year]["hurricaneAreas"].append(area)
        hurricane_list_by_year[year]["hurricaneDamage"].append(damage)
        hurricane_list_by_year[year]["hurricaneDeaths"].append(death)
    return hurricane_list_by_year


# Create dictionary of hurricanes organized by year
hurricaneListByYears = hurricane_dict_year(dictOfHurricane)
# print(hurricaneListByYears)
# Print the result
# 4
# Counting Damaged Areas


# create dictionary of areas to store the number of hurricanes involved in
def count_affected_areas(dict_of_hurricane):
    area_count = {}

    for details in dict_of_hurricane.values():
        _, _, _, _, areas, _, _ = details
        for area in areas:
            if area in area_count:
                area_count[area] += 1
            else:
                area_count[area] = 1

    return area_count


affected_area_dict = count_affected_areas(dictOfHurricane)


# print(affected_area_dict)
# 5
# Calculating Maximum Hurricane Count
# find most frequently affected area and the number of hurricanes involved in
def maxhurricanecount(affected_area):
    most_affected_area = None
    max_count = 0

    for area, count in affected_area.items():
        if count > max_count:
            most_affected_area = area
            max_count = count

    return most_affected_area, max_count


maxhitarea = maxhurricanecount(affected_area_dict)

# print(maxhitarea)


# 6
# Calculating the Deadliest Hurricane
# find highest mortality hurricane and the number of deaths
def find_deadliest_hurricane(dict_of_hurricane):
    deadliest_hurricane = None
    max_deaths = 0

    for hurricane, details in dict_of_hurricane.items():
        _, _, _, _, _, _, deaths = details
        if deaths > max_deaths:
            deadliest_hurricane = hurricane
            max_deaths = deaths

    return deadliest_hurricane, max_deaths


deadliestHurricane = find_deadliest_hurricane(dictOfHurricane)

print(deadliestHurricane)
# 7
# Rating Hurricanes by Mortality
# categorize hurricanes in new dictionary with mortality severity as key
mortality_scale = {1: 99, 2: 499, 3: 999, 3: 9999, 5: 10000}


def rate_hurricanes_by_mortality(dict_of_hurricane, mortality_scale):
    rated_hurricanes = {rating: [] for rating in mortality_scale}

    for hurricane, details in dict_of_hurricane.items():
        name, month, year, max_wind, areas, damage, deaths = details
        for rating, upper_bound in mortality_scale.items():
            if deaths <= upper_bound:
                hurricane_info = name
                rated_hurricanes[rating].append(hurricane_info)
                break

    return rated_hurricanes


rated_hurricanes = rate_hurricanes_by_mortality(dictOfHurricane, mortality_scale)

# print(rated_hurricanes)


# 8 Calculating Hurricane Maximum Damage


# find highest damage inducing hurricane and its total cost
def find_highest_damage(dict_of_hurricane):
    higest_damage_hurricane = None
    max_damage = 0.0

    for hurricane, details in dict_of_hurricane.items():
        (
            _,
            _,
            _,
            _,
            _,
            updated_damages,
            _,
        ) = details
        try:
            updated_damages = float(updated_damages)
        except ValueError:
            continue
        if updated_damages > max_damage:
            highest_damage_hurricane = hurricane
            max_damage = updated_damages

    return highest_damage_hurricane, max_damage


highestdamageHurricane = find_highest_damage(dictOfHurricane)

print(highestdamageHurricane)

# 9
# Rating Hurricanes by Damage
# categorize hurricanes in new dictionary with damage severity as key
damage_scale = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000}


def rate_hurricanes_by_damage(dict_of_hurricane, damage_scale):
    rated_hurricane = {rating: [] for rating in damage_scale}

    for hurricane, details in dict_of_hurricane.items():
        name, month, year, max_wind, areas, damage, deaths = details
        for rating, upper_bound in damage_scale.items():
            try:
                damage = float(damage)
            except ValueError:
                continue
            if damage <= upper_bound:
                hurricane_info = name
                rated_hurricane[rating].append(hurricane_info)
                break

    return rated_hurricane


rated_hurricanes_by_damage = rate_hurricanes_by_damage(dictOfHurricane, damage_scale)

print(rated_hurricanes_by_damage)
