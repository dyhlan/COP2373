# Dylan Hamid
# Programming Exercise 13
# Write a program (function) to create a database called population_(your initials).
# For ex: population_SM would be my database.
# Create a table named population with the following fields; 1. city, 2. year, 3. population.
# Choose 10 cities in Florida and insert data into the population table for the year 2023.
# Create a function to the simulate population growth and decline for the next 20 years at various rates for each year.
# Insert this data into the population table.
# Using matplotlib, create a function to show the population growth for a city.
# Let the user know the 10 cities as options and ask them to choose one
# and display the population growth for the city visually.

import sqlite3
import random
import matplotlib.pyplot as plt


def main():
    # Connecting to database and creating cursor
    conn = sqlite3.connect('population_DH.db')
    cursor = conn.cursor()

    # Removes population table from any previous iterations/executions of file; starts fresh
    cursor.execute("DROP TABLE IF EXISTS population")

    # Creates table
    table_creation_query = """
        CREATE TABLE population (
        city VARCHAR(30),
        year INT,
        population INT
        );
        """

    cursor.execute(table_creation_query)

    # Inserts 10 Floridian cities into database
    cursor.execute("""
    INSERT INTO population (city, year, population) VALUES ('JACKSONVILLE', 2023, 985843),
        ('MIAMI', 2023, 455924),
        ('TAMPA', 2023, 403364),
        ('ORLANDO', 2023, 320742),
        ('GAINESVILLE', 2023, 145812),
        ('TALLAHASSEE', 2023, 202221),
        ('LAKELAND', 2023, 122264),
        ('BRANDON', 2023, 116365),
        ('MIRAMAR', 2023, 138319),
        ('CLEARWATER', 2023, 116850)
        """)

    conn.commit()
    # Simulates population growth for each city for 20 years and adds to database
    population_growth()


def population_growth():
    # Connect to database and create cursor
    connection = sqlite3.connect('population_DH.db')
    cursor = connection.cursor()

    # Iterates over each city, simulating growth
    cursor.execute("SELECT * FROM population")
    for row in cursor.fetchall():
        # Assigning values from database row to variables, for operations
        # Year acts as accumulator for while loop
        # City is for inserting data with the proper city
        # Population is operated on for each city
        year = row[1]
        city = row[0]
        population = float(row[2])

        # Calculates a new population each year for the currently selected city for 20 years
        while year != 2043:
            # New year gets inserted into database
            year += 1

            # Calculates growth rate for city
            rate = random.uniform(-.2,.3)

            # Adds new population to current population, then rounds down.
            new_population = int(population + (population * rate))

            # Assigns new population to population, so each year adds onto the population from the previous one
            population = new_population

            # Inserts the city, year, and population into database
            cursor.execute(f"INSERT INTO population VALUES ('{city}', {year}, {new_population})")

    connection.commit()
    connection.close()

    # Allows user to see population growth of a selected city graphed
    city_growth_mapping()


def city_growth_mapping():
    # Connecting to database and creating cursor.
    connection = sqlite3.connect('population_DH.db')
    cursor = connection.cursor()

    # Initializing arrays to hold population and year from database, to be plotted on graph
    x_axis_data = []
    y_axis_data = []

    # Repeats if user does not enter a city name found in database
    while True:
        try:
            # Prompting user to enter city name
            print("Please select a city's population growth you would like to view. The 10 cities available are:")
            print(f"JACKSONVILLE \nMIAMI \nTAMPA \nORLANDO \nGAINESVILLE \nTALLAHASSEE "
                  f"\nLAKELAND \nBRANDON \nMIRAMAR \nCLEARWATER")
            user_city = input("Enter your city here: ").upper()

            # Appending City's population growth to axis data arrays for plotting
            cursor.execute(f"SELECT year, population FROM population where city = '{user_city}'")
            for row in cursor.fetchall():
                x_axis_data.append(row[0])
                y_axis_data.append(row[1])

            # Assigning first, fifth, tenth, fifteenth, and last/twenty-first population counts as y-axis ticks
            y_axis_points = [y_axis_data[0], y_axis_data[4], y_axis_data[9], y_axis_data[14], y_axis_data[20]]

            # Plotting population growth
            plt.plot(x_axis_data, y_axis_data, marker = "o")

            # Dressing the graph with ticks and a label for the x-axis
            plt.xticks(x_axis_data)
            plt.xlabel("Year")
            plt.yticks(y_axis_points)

            # Showing graph
            plt.show()
            break
        except:
            print("ERROR: Please enter a valid city name. Please try again.")


main()
