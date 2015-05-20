__author__ = 'Joe Munoz'
#Date: February 20, 2014

# kCura coding challenge:

    # Function calls are at the bottom of this file.

    # All file names are hard-coded

    # No directory paths are given, so it's assumed that both CityData.py
    # and the sample text file will be in this file's directory

# CityData.py contains the data transfer and business objects for this program
import CityData
from collections import OrderedDict


class FileWriter:
    def __init__(self, templatefunc=None, contextfilename=None):
        if templatefunc:
            self.get_template = templatefunc
        if contextfilename:
            self.filename = contextfilename

    def write_template(self):
        try:
            with open(self.filename, 'w') as file_handle:
                file_handle.write(self.get_template())
        except IOError, er:
            print 'Error reading file: %(file)s \n' + er.message % {'file': self.filename}
        finally:
            file_handle.close()


def read_in_cities():
    try:
        with open('Cities.txt', 'r') as file_handle:
            for line in file_handle.readlines():
                fields = line.rstrip().split('|')

                city = CityData.CityData()
                city.fill(fields)
                cities.append(city)
    except IOError, er:
        print 'File reading error' + er.message
    finally:
        file_handle.close()


# OPTION 1 (a)
def cities_by_population():
    # Sort cities by population
    sortedCities = sorted(cities, key=lambda city: city.population, reverse=True)

    # Build list of strings to use in writer
    city_data_string = []
    last_pop = 0
    for city in sortedCities:
        if city.population != last_pop:
            city_data_string.append(str(city.population) + '\n\n')
            last_pop = city.population
        city_data_string.append(city.city + ', ' + city.state + '\n')
        city_data_string.append('Interstates: ')
        for interstate in city.interstates:
            city_data_string.append(str(interstate) + ', ')
        city_data_string.append('\n\n')

    #return flattened string
    return ''.join(city_data_string)


#OPTION 1 (b)
def interstates_by_city():
    # Arrange interstates into dictionary (key: interstate, value: city)
    interstate_dictionary = dict()
    for city in cities:
        for istate in city.interstates:
            key = int(istate[2:])
            if not key in interstate_dictionary:
                interstate_dictionary[key] = []
            interstate_dictionary[key].append(city.city)

    # Sort dictionary by I-value
    sorted_interstates = OrderedDict(sorted(interstate_dictionary.items(), key=lambda d: d[0]))

    # Build list of strings to use in writer
    interstate_data_string = []
    for key in sorted_interstates:
        interstate_data_string.append(str(key) + ' ' + str(len(sorted_interstates[key])) + '\n')

    #return flattened string
    return ''.join(interstate_data_string)


# OPTION 2
def degrees_from_chicago():
    # Find Chicago City object
    chicago = next(x for x in cities if x.city == "Chicago")

    mutable_cities = list(cities)
    mutable_cities.remove(chicago)

    degree_list = [CityData.DegreeData(degree=0, city=chicago.city, state=chicago.state)]

    # Fill new list when degrees are found
    interstate_cache = chicago.interstates

    search_for_interstates = True
    while search_for_interstates:
        new_interstate_cache = list()
        for counter, interstate in enumerate(interstate_cache):
            # get a list of matching interstates
            for city in mutable_cities:
                match = filter(lambda c: c == interstate, city.interstates)

                if match:
                    # Add to degree list
                    degree_list.append(CityData.DegreeData(degree=counter+1, city=city.city, state=city.state))
                    # Remove from mutable list to help with recursion speed
                    mutable_cities.remove(city)
                    # Add new interstates to recent cache
                    for interstate in city.interstates:
                        new_interstate_cache.append(interstate)
        # If there are more interstates in the tree, keep searching
        # It's possible that some cities may have no link to Chicago, therefore we measure
        #   duration by the filling of the cache
        if len(new_interstate_cache) != 0:
            interstate_cache = new_interstate_cache
        else:
            search_for_interstates = False

    return build_degrees_string(degree_list)


def build_degrees_string(degree_city_objects):
    sortedCities = sorted(degree_city_objects, key=lambda city: city.degree, reverse=True)

    # Build list of strings to use in writer
    degree_data_string = []
    for city in sortedCities:
        degree_data_string.append(str(city.degree) + ' ' + city.city + ', ' + city.state + '\n')

    # Return flattened string
    return ''.join(degree_data_string)


cities = list()
read_in_cities()


#   Ideally, the FileWriter class should accept a list of these write objects and
#   iterate through them to write in a single execution. This was left out due
#   to allow easier single-file testing.

writer = FileWriter(templatefunc=degrees_from_chicago, contextfilename='Degrees_From_Chicago.txt')
writer.write_template()
writer = FileWriter(templatefunc=interstates_by_city, contextfilename='Interstates_By_City.txt')
writer.write_template()
writer = FileWriter(templatefunc=cities_by_population, contextfilename='Cities_By_Population.txt')
writer.write_template()