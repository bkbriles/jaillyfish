#!/usr/bin/env python

import sys
import smtplib
import linn
import marion

# Initialize some variables. Replace keywords with real contacts.
keywords = ['LASTNAME, FIRSTNAME', 'LASTNAME2', 'ETC']

# Generate new roster files and test for any matches
linn.linn_roster()
marion.marion_roster()

# Create a list to hold any contact should they be in jail. Needed to send an email later.
# Then open up roster files and check against keywords
number_in_jail = 0
name = []
f = open("marion_roster.txt")
for line in f:
    if any(keyword in line for keyword in keywords):
        print(line)
        name.append(line)
        number_in_jail += 1

# Close the roster file
f.close()

f = open("linn_roster.txt")
for line in f:
    if any(keyword in line for keyword in keywords):
        print(line)
        name.append(line)
        number_in_jail += 1

# Close the roster file
f.close()

# If there are no contacts in jail, print. Else: send an email listing my friends who are in jail
if number_in_jail == 0:
    print("No one you know is in Jail.")
else:
    smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login('myemail@outlook.com', 'myPassword')
    smtpObj.sendmail('myemail@outlook.com', 'recepient@gmail.com', 'Subject: A Contact is in Jail!\nThe following are in jail: ' + str(name))
    smtpObj.quit()