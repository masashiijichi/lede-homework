#Masashi IJICHI
#2024June05
#Homework 3, Part 2

#PART TWO: Lists

#1
countries=["USA","China","Japan","Germany","France","Netherlands","Greece"]

#2
for country in countries:
    print(country)

#3
countries=sorted(countries)
print(countries)

#4
print((countries)[0])

#5
print((countries)[-2])

#6
del countries[1]
print(countries)

#7
for country in countries:
    print(country.upper())

#PART TWO: Dictionaries

#1 https://en.wikipedia.org/wiki/Sarv-e_Abarkuh
tree={"name":"Cypress of Abarkuh","species":"Cypress","age":"4500","location_name":"Iran","latitude":"31.12264","longitude":"53.27984"}

#2
print(f"{tree['name']} is a {tree['age']} year old tree that is in {tree['location_name']}")


#3
if float(tree["latitude"])<40.7128 :
    print(f"The tree {tree['name']} in {tree['location_name']} is south of NYC" )
else: 
    print(f"The tree {tree['name']} in {tree['location_name']} is north of NYC")


#4
your_age=input("How old are you?")
your_age=int(your_age)

if your_age> int(tree['age']):
    print(f"you are {your_age-tree['age']} years older than {tree['name']}.")
elif your_age<int(tree['age']):
    print(f"{tree['name']} was {int(tree['age'])-your_age} years old when you were born.")
