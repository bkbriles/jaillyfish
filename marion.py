#!/usr/bin/env python

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import sys

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
