# Dylan Hamid
# Programming Exercise 12
# In this assignment, you will utilize numpy to analyze student grades stored in a CSV file.
# You will perform various statistical calculations and operations to gain insights into the dataset.
# This assignment will help you practice data manipulation and analysis using numpy arrays.

import numpy as np


def main():
    # Loading data from CSV file into numpy array
    # Tuple to be used in reference and data type for numpy array
    array_columns = [('First Name', 'U30'), ('Last Name', 'U30'), ('Exam 1', 'i2'), ('Exam 2', 'i2'), ('Exam 3', 'i2')]

    # Creating numpy array of grades.csv
    grades_array = np.loadtxt('grades.csv', array_columns, delimiter=',', skiprows=1)

    # Isolating values corresponding to each exam to own array variable for operating on
    exam_one_grades = grades_array['Exam 1']
    exam_two_grades = grades_array['Exam 2']
    exam_three_grades = grades_array['Exam 3']

    # Combining values from all exams to single array for operating on
    all_exams_grades = np.concatenate((exam_one_grades, exam_two_grades, exam_three_grades), axis=None)

    # Printing first few rows of dataset
    print(f'{grades_array[0]}\n'
          f'{grades_array[1]}\n'
          f'{grades_array[2]}\n'
          f'{grades_array[3]}\n')

    # Calculating statistics for each exam
    # Passing in specific exam array and string denoting name of exam to be displayed
    print(statistics_calculator(exam_one_grades,'Exam One'))
    print(statistics_calculator(exam_two_grades, 'Exam Two'))
    print(statistics_calculator(exam_three_grades, 'Exam Three'))


    # Calculating overall statistics for entire dataset
    # Passing in all exam array and string denoting all exams to be displayed
    print(statistics_calculator(all_exams_grades,'All Exams'))

    # Determining the number of students who passed and failed each exam
    # Passing in arrays for each exam into calculator for pass and fail count, assigning to variable
    pass_and_fail_exam_one = pass_and_fail_calculator(exam_one_grades)
    pass_and_fail_exam_two = pass_and_fail_calculator(exam_two_grades)
    pass_and_fail_exam_three = pass_and_fail_calculator(exam_three_grades)

    # Displaying pass/fail count for each exam
    print(f'Students who passed Exam One: {pass_and_fail_exam_one[0]}\n'
           f'Students who failed Exam One: {pass_and_fail_exam_one[1]}\n')

    print(f'Students who passed Exam Two: {pass_and_fail_exam_two[0]}\n'
           f'Students who failed Exam Two: {pass_and_fail_exam_two[1]}\n')

    print(f'Students who passed Exam Three: {pass_and_fail_exam_three[0]}\n'
          f'Students who failed Exam Three: {pass_and_fail_exam_three[1]}\n')

    # Calculating the overall pass percentage across all exams
    # Passing in all exam array to calculate pass and fail count
    pass_and_fail_all_exams = pass_and_fail_calculator(all_exams_grades)

    # Calculating the fraction of total passing grades to be displayed as percent
    all_exams_passing_percent = pass_and_fail_all_exams[0]/(pass_and_fail_all_exams[0] + pass_and_fail_all_exams[1])

    # Displaying percent of all exam grades which are passing.
    print(f"Passing percent for all exams = {all_exams_passing_percent * 100:.2f}%")


# Calculates mean, median, standard deviation, minimum, and maximum of exam array passed in,
# And returns string displaying data.
def statistics_calculator(exam_data, exam):
    # Assigning passed in variables to usable variables
    exam_grades = exam_data
    exam = exam

    # Operating on passed in array
    mean = np.mean(exam_grades)
    median = np.median(exam_grades)
    standard_deviation = np.std(exam_grades)
    minimum = np.min(exam_grades)
    maximum = np.max(exam_grades)

    # Returning strings displaying calculated data
    return (f'Statistics for {exam}:\n'
            f'Mean: {mean}\n'
            f'Median: {median}\n'
            f'Standard Deviation: {standard_deviation}\n'
            f'Minimum: {minimum}\n'
            f'Maximum: {maximum}\n')


# Accumulates pass and fail count for a passed in array, returns counts
def pass_and_fail_calculator(exam_grades):
    # Initializing variables
    grades = exam_grades
    pass_count = 0
    fail_count = 0

    # Accumulates pass_count if grade is passing (>=60), accumulates fail_count otherwise
    for grade in grades:
        if grade >= 60:
            pass_count += 1
        else:
            fail_count += 1

    # Returns pass and fail count
    # Is operated on in main
    return [pass_count, fail_count]


main()
