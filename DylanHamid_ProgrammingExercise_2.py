# Dylan Hamid
# Programming Exercise 2
# Spam (or junk email) costs U.S. organizations billions of dollars a year in spam-prevention software, equipment,
# network resources, bandwidth, and lost productivity.
# Research online some of the most common spam email messages and words.
# Create a list of 30 words and phrases commonly found in spam messages.
# Write an application in which the user enters an email message.
# Then your application will scan the message for each of the 30 keywords or phrases.
# For each occurrence of one of these within the message, add a point to the message's "spam score".
# Next, rate the likelihood that the message is spam, based on the number of points received.
# Display the user's spam score, the likelihood message that it is spam,
# and the words/phrases which caused it to be spam.

import re


def main():
    #Prompt user for message to be scanned.
    email_message = input("Enter your email message here. Please remove all linebreaks: ")

    #Sends user's message to spam_checker().
    #Returns spam score, phrases found in message and assigns to return_values
    return_values = spam_checker(email_message)

    #Assigns spam score and the phrases found to score and phrase_list, respectively
    score = return_values[0]
    phrase_list = return_values[1]

    #Prints spam score
    print(f'Spam score: {score}')

    #Labels message as likely to be spam if a spam score higher than 3.
    #Lables message as unlikely to be spam if not.
    if score > 3:
        print("This message is likely spam!")
    else:
        print("This message is unlikely to be spam.")

    #Prints the phrases found in message
    print('These common spam keywords/phrases were found in your email:', *phrase_list, sep=', ')

#Scans message for keywords and phrases common in spam emails
#Counts each occurance as spam score
#And notes the phrase found
def spam_checker(email):
    #Phrases in word bank are all lowercase, so .lower() is needed in case of capitalization
    #Assigns the user message to a variable.
    email = email.lower()

    #Initializes spam score, used to accumulate amount of times phrases are found in message.
    spam_score = 0

    #Initializes a list to hold the phrases which are found in message
    phrase_list = []

    #Word bank of common spam phrases.
    spam_phrases = ["urgent", "immediate", "guaranteed", "offer", "special promotion", "winner",
                    "you have been chosen", "eligible", "dear friend", "congratulations", "hello!", "good news",
                    "attention", "click here", "attachment", "click to view", "download now", "click below",
                    "activate link", "act now", "get out of debt", "last chance", "no catch", "password", "near you",
                    "additional income", "home-based", "work from home", "big bucks", "best price"]

    #Loops over each phrase in word bank to scan if its present in message.
    for phrase in spam_phrases:
        #Assigns all individual instance of a phrase to a list.
        #Will be looped over and accumulated, and used to determine if phrase needs to be added to phrase_list.
        occurance_list = re.findall(phrase, email)

        #For loop to loop over occurance_list, accumulates spam_score for each loop.
        for occurance_found in occurance_list:
            spam_score += 1

        #Adds a phrase from word bank to list if it has at least one occurance in the message.
        if len(occurance_list) > 0:
            phrase_list.append(phrase)
        else:
            continue

    #Assigns spam_score and phrase_list to a list, so both can be returned at once easily.
    return_values = [spam_score, phrase_list]

    #Returns spam_score and phrase_list to main().
    return return_values


main()