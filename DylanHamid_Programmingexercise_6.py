# Dylan Hamid
# Programming Exercise 6
# Create functions to validate phone numbers, social security numbers and zip codes using regular expressions.
# Create a main function to get input from a user and then displaying if the phone number,
# social security number and zip code they entered is valid.
# Be sure to test the functions with various inputs, including valid and invalid examples,
# to ensure the correctness of the regular expressions.

import re

def main():
    # Displaying regular expression format to user.
    print('This program will validate a phone number, social security number, or a zip code. Please use the'
          ' following format.\nPHONE NUMBER: ***-***-****\nSOCIAL SECURITY NUMBER: ***-**-**** \nZIP CODE: *****')

    # Prompting user for phone number, ssn, or zip code to validate.
    sequence_to_validate = input("Please enter either a phone number, social security number, or"
                                 " a zip code: ")

    # Sending user's numbers to number_validator, assigning to variable whether its valid or not.
    is_sequence_valid = number_validator(sequence_to_validate)

    # Displaying whether number is valid.
    print(is_sequence_valid)


def number_validator(sequence):
    # Creating regular expression strings to validate user's numbers to
    phone_number_expression = r'\d\d\d[ -]\d\d\d[ -]\d\d\d\d$'
    ssn_expression = r'\d\d\d[ -]\d\d[ -]\d\d\d\d$'
    zip_code_expression =r'\d\d\d\d\d$'

    # Assigning user's numbers to a usable variable.
    sequence = sequence

    # Validating user's numbers by matching to the regular expressions, and returning depending on what it matches.
    if re.match(phone_number_expression, sequence):
        return "This is a valid phone number."
    elif re.match(ssn_expression, sequence):
        return "This is a valid social security number."
    elif re.match(zip_code_expression, sequence):
        return "This is a valid zip code."
    else:
        return "This is an invalid sequence."


main()
