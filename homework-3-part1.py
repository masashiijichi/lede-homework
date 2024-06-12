#Masashi IJICHI
#2024June05
#Homework 3, Part 1

#PART ONE: Lists
#1
numbers=[22, 90, 0, -10, 3, 22,48]

#2
print(len(numbers))

#3
numbers[3]

#4
print(int((numbers)[1])+int((numbers)[3]))

#5
print(sorted(numbers)[-2])

#6
print(numbers[-1])

#7
for a in numbers:
    print(a/2)

#8
import statistics
mean_num=statistics.mean(numbers)
median_num=statistics.median(numbers)

if mean_num==median_num:
    print("The mean and the median are equal")
elif mean_num>median_num:
    print("The mean is higher")
elif median>mean_num:
    print("The median is higher")

#PART ONE: Dictionaries
#1
movie={"title":"Interstellar","year":"2014","director":"Christopher Nolan"}
print("My favorite movie is", movie['title'], "which was released in", movie['year'], "and was directed by", movie['director'])

#2
movie["budget"]=165000000
movie["revenue"]=733202212
print(movie["budget"])
print(movie["revenue"])

#3
if movie["budget"]>movie["revenue"]:
    print( "That was a bad investment")
elif movie["revenue"]>= 5 * movie["budget"]:
    print("That was a great investment")
else:
    print("That was an okay investment")

#4
area_stats=[{"area":"Manhattan","population":int(1600000)},{"area":"Brooklyn","population":int(2600000)},
            {"area":"Bronx","population":int(1400000)},{"area":"Queens",
            "population":int(2300000)},{"area":"Staten Island","population":int(470000)
            }]

#5
for area in area_stats:
    if area["area"] == "Brooklyn":
        print(area["population"])

#6
populations=0
for area in area_stats:
    populations+=area['population']
print(populations)

#7
for area in area_stats:
    if area["area"] == "Manhattan":
        Manhattan_NYC_ratio=round(area["population"]/populations*100,2)
        print(f'{Manhattan_NYC_ratio}'"% pf NYC's population lives in Manhattan")


