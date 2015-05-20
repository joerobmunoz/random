__author__ = 'treefort'

# This file contains the classes for data transfer and business objects respectively.
# There were separated for ease of readability.

class CityData():
    """
    Represents the city data object
    """
    def __init__(self):
        self.population = 0
        self.city = ""
        self.state = ""
        self.interstates = []


    def fill(self, line):
        if line and len(line) == 4:
            try:
                self.population = int(line[0])
                self.city = str(line[1])
                self.state = str(line[2])
                self.interstates = line[3].split(';')
            except Exception, er:
                print er.message
        else:
            print 'Line: \n %(line)s \n may have been improperly formatted' % {'line': line}


class DegreeData():
    """
    Represents the Degree from Chicago object for Option 2
    """

    def __init__(self, degree=0, city="", state=""):
        self.degree = degree
        self.city = city
        self.state = state
