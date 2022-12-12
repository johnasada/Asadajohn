# ################################################## #
# File: windchill.py                                 #
# Author: Asada, John Paul                  #
# Course: CSE 110                                    #
# Purpose: To fulfill the requirements for w13 prove #
# ################################################## #

"""    - - -     explainig the variables     - - -     """
# c = Celcius
# F = Fahrenheit
# v = the wind speed in miles per hour
# temp = the temperature in °F
# c_temp = the temperature in °C


def wind_chill(temp, v):
    return (35.74 + (0.6215 * temp)) - (35.75 * v ** 0.16) + (0.4275 * temp * (v ** 0.16))
# The above function calculates the wind chill using temperature in °F


def celsius_wind_chill(temp, v):
    return (35.74 + (0.6215 * c_temp)) - (35.75 * v ** 0.16) + (0.4275 * c_temp * (v ** 0.16))
# The above function calculates the wind chill using the converted temperature


temp = int(input("Enter the temperature: "))
scale = input("Farenheit or Celcius (F/C)? ").lower()
c_temp = (temp * 9/5) + 32  # This line converts the temperature from °C to °F

if scale == "f":
    for v in range(5, 61, 5):
        print(
            f"At temperature {temp:.1f}°F, and {v} mph, the windchill is:\
                {wind_chill(temp,v):.2f}°F"
        )
# To write the degrees symbol(°), I used Alt + 248 or Alt + 0176

elif scale == "c":
    for v in range(5, 61, 5):
        print(
            f"At temperature {temp:.1f}°F, and {v} mph, the windchill is:\
                {celsius_wind_chill(temp,v):.2f}°F"
        )
# Thanks for using my program

# Much Love coming from this end. 
# Hope to work with you someday