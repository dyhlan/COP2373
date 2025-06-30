# Dylan Hamid
# Programming Exercise 7
# Using the code in Section 7.4, write a program that will allow me to enter a paragraph,
# including sentences which begin with numbers.
# Display each individual sentence and the count of sentences in the paragraph.

import re

def main():
    # Prompting user to enter a paragraph to be counted
    paragraph = input("Please enter a paragraph: ")

    # Sending user's paragraph to function to be counted, then assigning to variable.
    sentences_in_paragraph = sentence_finder(paragraph)

    # Displaying the count of sentences in the paragraph.
    print(f'There are {len(sentences_in_paragraph)} sentences in your paragraph:')

    # Looping to display each sentence individually.
    for sentence in sentences_in_paragraph:
        print('->', sentence)


def sentence_finder(paragraph):
    # Assigning user's paragraph to a usable variable.
    paragraph = paragraph

    # Setting up the regular expression pattern to find a sentence
    sentence_expression = r'[A-Z0-9].*?[.!?](?= [A-Z0-9]|$)'

    # Finding each sentence in user's paragraph, assigning to a list
    sentences_in_paragraph = re.findall(sentence_expression, paragraph, flags=re.DOTALL | re.MULTILINE)

    # Returning the list of user's sentences to main()
    return sentences_in_paragraph


main()