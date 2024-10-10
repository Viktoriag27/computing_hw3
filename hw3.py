# 1)
# Create a function called "car_at_light"
# It should take one parameter: "light"
# which gives the color of a traffic light.
# If the color is "red", the function should return
# "stop". If the color is "green", the function
# should return "go". If the color is "yellow"
# the function should return "wait". If the color
# is anything else, the function should raise
# an exception with the following message: 
# "Undefined instruction for color: <light>" 
# where <light> is the value of the parameter light.
#

# 2)
# Create a function named "safe_subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
# If the values cannot be subtracted due to its type, 
# it returns None.
# If there is any other reason why it fails show the problem 
# 

# 3)
# Imagine you have a dictionary with the attributes of a person
# {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
# {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}
# create two functions that returns the age of the person
# that handles both examples.
# Name the first function "retrieve_age_eafp" and follow EAFP
# Name the second function "retrieve_age_lbyl" and follow lbyl

from datetime import datetime

# EAFP 
def retrieve_age_eafp(person, name, last_name):
    current_year = datetime.now().year
    try:
        # Check if the provided name and last_name match the dictionary
        if person['name'] == name and person['last_name'] == last_name:
            # Try to retrieve and calculate the age
            birth_year = person['birth']
            age = current_year - birth_year
            return age
        else:
            return "Person not found."
    except KeyError:
        return "Birth year is missing."
    except TypeError:
        return "Invalid data format for birth year."

# LBYL
def retrieve_age_lbyl(person, name, last_name):
    current_year = datetime.now().year
    # Check if the provided name and last_name match the dictionary
    if person.get('name') == name and person.get('last_name') == last_name:
        # Check if 'birth' exists and is a valid integer
        if 'birth' in person and isinstance(person['birth'], int):
            birth_year = person['birth']
            age = current_year - birth_year
            return age
        else:
            return "Birth year is missing or invalid."
    else:
        return "Person not found."

# Example data
person_data = {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
person_data_no_birth = {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}
# Test
print(retrieve_age_eafp(person_data, 'John', 'Doe'))          # Should return the calculated age
print(retrieve_age_eafp(person_data_no_birth, 'Janet', 'Bird')) # Should return "Birth year is missing."
print(retrieve_age_eafp(person_data, 'Jane', 'Doe'))          # Should return "Person not found."

print(retrieve_age_lbyl(person_data, 'John', 'Doe'))          # Should return the calculated age
print(retrieve_age_lbyl(person_data_no_birth, 'Janet', 'Bird')) # Should return "Birth year is missing or invalid."
print(retrieve_age_lbyl(person_data, 'Jane', 'Doe'))          # Should return "Person not found."

# 4)
# Imagine you have a file named data.csv. 
# Create a function called "read_data" that reads the file
# making sure to use to handle the fact 
# that it might not exist. 
#
import csv

def read_data(file_name):
    try:
        # Try to open and read the CSV file
        with open(file_name, mode='r') as file:
            csv_reader = csv.reader(file)
            data = [row for row in csv_reader]  # Read all rows into a list
        return data
    
    except FileNotFoundError:
        # Handle the case where the file doesn't exist
        return f"Error: The file '{file_name}' does not exist."
    
    except Exception as e:
        # Handle any other exceptions
        return f"An error occurred: {e}"

# Example usage
file_name = 'data.csv'
result = read_data(file_name)
print(result)


# 5) Squash some bugs! 
# Find the possible logical errors (bugs) 
# in the code blocks below. Comment in each of them
# which logical errors did you find and correct them
### (a)
total_double_sum = 0
for elem in [10, 5, 2]:
    double = elem * 2
    total_double_sum += elem

### (b)
strings = ''
for string in ['I', 'am', 'Groot']:
    strings = string+"_"+string

### (c) Careful!
j=10
while j > 0:
   j += 1

### (d)
productory = 0
for elem in [1, 5, 25]:
    productory *= elem


