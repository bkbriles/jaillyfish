#!/usr/bin/env python

from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup
import sys
import smtplib

# Check Marion County Inmate Roster
url = "http://apps.co.marion.or.us/JailRosters/mccf_roster.html"

# Open connection and grab page
uClient = uReq(url)
page_html = uClient.read()
uClient.close()

# HTML parser
page_soup = soup(page_html, "html.parser")

# Grab each person in the roster, and when the roster was last updated
name_containers = page_soup.findAll("a", {"href":"#"})
time_containers = page_soup.findAll("div", {"align":"center"})

# Keeping a variable holding the current amount of inmates. Variable i = 0 to start iterating at the first inmate.
roster = len(name_containers)
i = 0
f = open('marion_roster.txt', 'w')
f.write(time_containers[0].text)
while i < roster:
    f.write(name_containers[i].text)
    i += 1

f.close()

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