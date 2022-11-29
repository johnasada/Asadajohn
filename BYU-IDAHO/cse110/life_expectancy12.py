import time

from datetime import datetime
current = datetime.now()
real_time = (current.strftime("%I:%M:%S %p"))
date = (current.strftime("%a, %b, %d, %Y"))
name = input("Please Enter your name: ").capitalize()
option = ""
while option != "no":
    life_max = -1
    life_min = 1000
    country_max = ""
    country_min = ""
    toss = 0
    number = 0
    lowest = 1000
    largest = 0
    lowest_country = ""
    lowest_year = ""
    largest_country = ""
    largest_year = ""
    average = 0


    choice_year = int(input("Enter the year of choice: "))

    print()

    with open("life-expectancy.csv") as expectancy_data:
        for line in expectancy_data:
            number = number + 1
            clean_line = line.strip()
            parts = line.split(",")

            if number > 1:  #skip the title line of the data file
                country = parts[0]
                code = parts[1]
                year = int(parts[2])
                life_expectancy = float(parts[3])

                if lowest > life_expectancy:
                    lowest = life_expectancy
                    lowest_country = country
                    lowest_year = year
            
                if largest < life_expectancy:
                    largest = life_expectancy
                    largest_country = country
                    largest_year = year
                

                if choice_year == year:
                    average += life_expectancy
                    toss = toss + 1
                    
                    if life_expectancy > life_max:
                        life_max = life_expectancy
                        country_max = country
                    
                    if life_expectancy < life_min:
                        life_min = life_expectancy
                        country_min = country


    average = average / toss

    print(f"The overall max life expectancy is: {largest} from {largest_country} in {largest_year}")
    print(f"The overall min life expectancy is: {lowest} from {lowest_country} in {lowest_year}")
    print()                  

    print()
    a = (f"For the year {choice_year}\nThe average life expectancy accross all countries was {average:.2f}")
    b = (f"The max life expectancy across all countries was {life_max} in {country_max}\nThe min life expectancy waas {life_min} in {country_min}")


    print(f"For the year {choice_year}\nThe average life expectancy accross all countries was {average:.2f}")
    print(f"The max life expectancy across all countries was {life_max} in {country_max}\nThe min life expectancy waas {life_min} in {country_min}")

    with open ("database.txt", "at") as doc:
        print(f"-------------------------------------", file=doc)
        print(name, file=doc)
        print(real_time, file=doc)
        print(date, file=doc)
        print(a, file=doc)
        print(b, file=doc)
        print(f"-------------------------------------", file=doc)

    print()
    option = input("do you want to text another year? ").lower()
print(f"Thank you {name}, please check database.txt for a copy of your analysed data.")