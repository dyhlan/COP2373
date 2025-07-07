# Dylan Hamid
# An instructor teaches a class in which each student takes three exams.
# The instructor would like to store this information in a file named grades.csv for later use.
# Create a program that allows an instructor to input how many students they want to enter.
# Then enter each student’s first name and last name as strings and the student’s three exam grades as integers.
# Use the csv module to write each record into the grades.csv file and have a header of
# First Name, Last Name, Exam 1, Exam 2 and Exam3. Each student should be a record in the grades.csv file.
# Once the file is created, create a separate program to read the grades.csv file and
# display the data in tabular format. Implement the with keyword.
# You may need to refer back to Chapter 5 for formatting.

import csv


def main():
    # Looping until user inputs either 1 or 2
    while True:
        # Ask user which action they want to do. Used to enter function corresponding to action.
        which_function = input('Please type "1" to enter grades, and type "2" to view them. ')

        # Breaks loop if user enters 1 or 2, repeats otherwise
        if which_function == '1' or which_function == '2':
            break
        else:
            print("ERROR. Please enter either a 1 or a 2. Please try again.")
            continue

    # Matches user's input to enter function
    # User inputs 1, matches and goes to enter_grades
    # User inputs 2, matches and goes to view_grades
    match which_function:
        case "1":
            enter_grades()
        case "2":
            view_grades()


def enter_grades():
    # Initializing counter for loop and array to be written to file
    student_number = 0
    student_array = [['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3'], ['', '', 0, 0, 0]]

    # Loop to ensure user enters a number.
    while True:
        try:
            # Prompt user for number of students. Used to compare with student_number to allow data entry for correct
            # number of students.
            number_of_students = int(input('How many students would you like to enter grades for? '))
            break

        except:
            print('ERROR: Please enter a number.')
            continue

    # Looping over each student
    while student_number < number_of_students:

        # Prompting user for student's first name, last name, and grades for 3 exams
        try:
            student_array[student_number + 1][0] = input("Please enter the student's first name: ")
            student_array[student_number + 1][1] = input("Please enter the student's last name: ")
            student_array[student_number + 1][2] = int(input("Please enter the grade for the student's first exam: "))
            student_array[student_number + 1][3] = int(input("Please enter the grade for the student's second exam: "))
            student_array[student_number + 1][4] = int(input("Please enter the grade for the student's third exam: "))

        except:
            print('ERROR: Please enter an integer for exam grades.')
            continue

        # Creating list in array to enter next students information into
        student_array.append(['', '', 0, 0, 0])

        # Accumulating counter for loop and for array entry
        student_number += 1

    # Removing blank list created at the end of final loop
    student_array.remove(['', '', 0, 0, 0])

    # Writing array to file
    with open('grades.csv', 'w', newline='') as grades_csv:
        data_entry = csv.writer(grades_csv, dialect='excel', delimiter='|', )
        data_entry.writerows(student_array)


def view_grades():
    try:
        # Printing grades of students.
        with open('grades.csv', newline='') as grades_csv:
            data_reader = csv.reader(grades_csv, delimiter=' ')
            for row in data_reader:
                print(' '.join(row))
    # If user tries to read before entering grades, will display the below message.
    except:
        print("ERROR: File not found. Please enter grades first before viewing them.")


main()