#!/usr/bin/env python

import sys
import smtplib

# Test marion_roster.txt to see if a contact is in jail
friends_in_jail = 0
keywords = ['LASTNAME, FIRSTNAME', 'LASTNAME2', 'ETC']

# Create a list to hold any contact should they be in jail. Needed to send an email later.
# Then open up the roster file and check against keywords
name = []
f = open('marion_roster.txt')
for line in f:
    if any(keyword in line for keyword in keywords):
        print line
        name.append(line)
        friends_in_jail += 1

# Close the roster file
f.close()

# If there are no contacts in jail, print. Else: send an email listing my friends who are in jail
if friends_in_jail == 0:
    print("None of your friends are in Marion County Jail.")
else:
    smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login('myemail@outlook.com', 'myPassword')
    smtpObj.sendmail('myemail@outlook.com', 'recepient@gmail.com', 'Subject: Friend in Jail!\nThe following are in jail: ' + str(name))
    smtpObj.quit()