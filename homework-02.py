#Masashi_IJICHI
#2024/06/04
#Homework 2

age=input("How old are you?")
#assuming the heart rate for human is 80 beats per minute
human_heart_beat=age*60*24*365
print(human_heart_beat)
#assuming the heart rate for blue whale is 33 beats per minute
whale_heat_beat=33*60*24*365
print(whale_heat_beat)
#assuming the heart rate for rabbit is 160 beats per minute
rabbit_heart_beat=160*60*24*365
if rabbit_heart_beat>=1000000000:
    print(rabbit_heart_beat/1000000000+"billion")
else:
    print(rabbit_heart_beat)

rabbit_heart_beat_in_billion=rabbit_heart_beat/1000000000
if rabbit_heart_beat>=1000000000:
    print(f"Rabbit's heart beats {rabbit_heart_beat_in_billion} billion times per minute ")
else:
    print(rabbit_heart_beat)
#pros:f-strings integrate strings and numbers cleanly.  cons:takes more time to code

myage=32
age_difference=32-int(age)
age_difference=abs(age_difference)
print(age_difference)

current_year=2024
birth_year_1=current_year-myage
birth_year_2=current_year-int(age)

if (birth_year_1%2)==0:
    print(str(birth_year_1)+" is Even")
else:
    print(str(birth_year_1)+" is Odd")

if (birth_year_2%2)==0:
    print(str(birth_year_2)+" is Even")
else:
    print(str(birth_year_2)+" is Odd")

import pandas as pd
from datetime import datetime

#I'm sure there is better way than following.  But so far I did my best.  
df=pd.read_html("https://simple.wikipedia.org/wiki/Democratic_Party_(United_States)")[1]
df['Term start']=df['Term start'].str.replace("[c]","")
df['Term start']=df['Term start'].apply(lambda x: datetime.strptime(x, "%B %d, %Y"))
#How many times there has been a president from the Democratic Party in office since they were born (each president only counts once)
their_birthday=input('Type your birthday in this format "yyyy-mm-dd"')
print(len(df[df['Term start'] > their_birthday]["President"].unique().tolist()))

df2=pd.read_html("https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States")[0]
df2['Term[14]']=df2['Term[14]'].str.replace("Incumbent", datetime.now().strftime("%B %d, %Y"))

import re

date_pattern = r"([A-Za-z]+ \d{1,2}, \d{4})"
date_format = "%B %d, %Y"
df2['Term[14]']=df2['Term[14]'].apply(lambda x: re.findall(date_pattern, x))

#If someone says they were born in the future, ask them for their year of birth again. Assume they'll do it right the second time.
correct_birthday=input('Type your birthday in this format "yyyy-mm-dd"')
if correct_birthday>datetime.now().strftime("%Y-%m-%d"):

    correct_birthday=input('You typed future date.  Type your birthday in this format again "yyyy-mm-dd"')

    
correct_birthday=datetime.strptime(correct_birthday, "%Y-%m-%d").date()

#Which US President was in office when they were born 

for date_range in df2['Term[14]']:
    start_date_str, end_date_str = date_range
    
    start_date = datetime.strptime(start_date_str, date_format).date()
    end_date = datetime.strptime(end_date_str, date_format).date()
    
    
    if start_date <= correct_birthday <= end_date:
        
        target_row = df2[df2['Term[14]'].apply(lambda x: x == date_range)]
        
        
        name = target_row['Name (Birth–Death)'].iloc[0]
        
        clean_name = re.sub(r"\(.*", "", name)
        
        
        print(clean_name.strip())
    else:
        pass