class Civil_engineering:
    specialisation = "Highway Engineering"
    category = "Water_Resources_Engineering"

    def practice(self):
        return "Civil Engineering is the practice of designing and executing " \
        "structural works that serve the general public."
    def consultancy(self):
        return "Consultancy is a professional service that provides expert advice " \
        "and guidance in a specific field."

my_civil_engineering = Civil_engineering()  # creating an instance of the class
my_civil_engineering.practice()  # calling the instance method
print(my_civil_engineering.practice())  # accessing class variable through instance
my_civil_engineering.consultancy()  # calling the instance method
print(my_civil_engineering.consultancy())  # accessing class variable through instance


class Civil_engineering:
    specialisation = "Highway Engineering"
    category = "Water_Resources_Engineering"

    def __init__(self, specialisation, category, careerpath):
        self.careerpath = careerpath
        self.specialisation = specialisation
        self.category = category
    
Civil_engineeringDetails = Civil_engineering("Highway Engineering", "Infrastructure", "Highway Engineer") #creating an instance of the class
print(Civil_engineeringDetails.specialisation) #accessing instance variable through instance
print(Civil_engineeringDetails.category) #accessing instance variable through instance
print(Civil_engineeringDetails.careerpath) #accessing instance variable through instance



class Civil_engineering:
    def __init__(self):
        self.__specialisation = "Highway Engineering"

    def get_specialisation(self):
        if self.__specialisation == "Highway Engineering":
            return "You need basic knowledge of civil engineering to pursue this field."
        else:
            return "Pursue structrural engineering."    


    
