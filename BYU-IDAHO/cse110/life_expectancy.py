number = 0
lowest = 1000
largest = 0

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
        
            if largest < life_expectancy:
                largest = life_expectancy


print(f"The overall max life expectancy is: {largest}")
print(f"The overall min life expectancy is: {lowest}")
print()                  