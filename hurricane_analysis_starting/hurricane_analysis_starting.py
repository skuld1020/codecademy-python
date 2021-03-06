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

def update_damages(lst):
  conversion = {"M": 1000000, "B": 1000000000}
  updated_list = []
  for i in lst:
    if i[-1] == "M":
      i = float(i.strip("M")) * conversion["M"]
      updated_list.append(i)
    elif i[-1] == "B":
      i = float(i.strip("B")) * conversion["B"]
      updated_list.append(i)
    else:
      updated_list.append(i)
  return updated_list
# test function by updating damages

damages = update_damages(damages)
print(damages)

# 2 
# Create a Table
def hurricanes_dict(names, months, years, max_sustained_winds, area_affected, damages, deaths):
  hurr_dict = {}
  for i in range(len(names)):
    hurr_dict[names[i]] = {"Name": names[i], "Month": months[i], "Year": years[i], "Max Sustained Wind": max_sustained_winds[i], "Areas Affected": area_affected[i], "Damage": damages[i], "Deaths": deaths[i]}
  return hurr_dict

# Create and view the hurricanes dictionary
hurricanes = hurricanes_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths)
print(hurricanes)

# 3
# Organizing by Year
def hurr_year(hurr):
  hurricanes_year = {}
  for item in hurr:
    key_year = hurr[item]["Year"]
    value_year = hurr[item]
    if key_year not in hurricanes_year:
      hurricanes_year[key_year] = [value_year]
    else:
      hurricanes_year[key_year].append(value_year)
  return hurricanes_year  

  

# create a new dictionary of hurricanes with year and key
hurricanes_year = hurr_year(hurricanes)
print(hurricanes_year)


# 4
# Counting Damaged Areas
def damage_area(areas):
  count_area = {}
  for area in areas:
    for place in area:
      count_area[place] = count_area.get(place, 0)+1
  return count_area

# create dictionary of areas to store the number of hurricanes involved in
count_damage_areas = damage_area(areas_affected)
print(count_damage_areas)


# 5 
# Calculating Maximum Hurricane Count
def calculate_max_damage(areas):
  num = 0
  area = ""
  for place,number in areas.items():
    if number > num:
      num = number
      area = place
  return num,area

# find most frequently affected area and the number of hurricanes involved in

max_num, max_place = calculate_max_damage(count_damage_areas)
print(max_num,max_place) 


# 6
# Calculating the Deadliest Hurricane
def calculate_max_death(hurr):
  total = 0
  name = ""
  for item in hurr.values():
    cur_name = item["Name"]
    death_num = item["Deaths"]
    if death_num > total:
      total = death_num
      name = cur_name
  return name, total

# find highest mortality hurricane and the number of deaths

name, death_number = calculate_max_death(hurricanes)
print(name, death_number)

# 7
# Rating Hurricanes by Mortality
#mortality_scale = {0: 0,
#                   1: 100,
#                   2: 500,
#                   3: 1000,
#                   4: 10000
#                   5: more than 10000}

def rating_hurr(hurr):
  rating_hurr = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
  for item in hurr.values():
    name = item["Name"]
    death = item["Deaths"]
    if death == 0:
      rating_hurr[0].append(name)
    elif death <= 100:
      rating_hurr[1].append(name)
    elif death <=500:
      rating_hurr[2].append(name)
    elif death <=1000:
      rating_hurr[3].append(name)
    elif death <= 10000:
      rating_hurr[4].append(name)
    else:
      rating_hurr[5].append(name)
  return rating_hurr

# categorize hurricanes in new dictionary with mortality severity as key

rating_hurricanes = rating_hurr(hurricanes)
print(rating_hurricanes)

# 8 Calculating Hurricane Maximum Damage

def max_damage(hurr):
  max_damage = 0
  hurr_name = ""
  for item in hurr.values():
    damage = item["Damage"]
    name = item["Name"]
    if damage == "Damages not recorded":
      continue
    elif damage > max_damage:
      max_damage = damage
      hurr_name = name
  return max_damage, hurr_name

# find highest damage inducing hurricane and its total cost


max_damage, hurricane = max_damage(hurricanes)
print(max_damage, hurricane)



# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

def dam_hurr(hurr):
  dam_hur = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
  for item in hurr.values():
    damage = item["Damage"]
    name = item["Name"]
    if damage == "Damages not recorded":
      continue
    elif damage == 0:
      dam_hur[0].append(name)
    elif damage <= 100000000:
      dam_hur[1].append(name)
    elif damage <= 1000000000:
      dam_hur[2].append(name)
    elif damage <= 10000000000:
      dam_hur[3].append(name)
    elif damage <= 50000000000:
      dam_hur[4].append(name)
    else:
      dam_hur[5].append(name)
  return dam_hur
  
# categorize hurricanes in new dictionary with damage severity as key

damage_hurr = dam_hurr(hurricanes)
print(damage_hurr)



