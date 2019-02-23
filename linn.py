#!/usr/bin/env python

from bs4 import BeautifulSoup as soup
import sys
import urllib.request

# Check Linn County Jail Roster
url = "https://www.linnsheriff.org/jail/current-inmates/"

# Open connection and grab page
req = urllib.request.Request(url, data=None, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
f = urllib.request.urlopen(req)

# HTML parser
page_soup = soup(f.read().decode('utf-8'), "html.parser")

# Grab each person in the roster, and when the roster was last updated
name_containers = page_soup.findAll('a')
time_containers = page_soup.findAll('p')

# Keeping a variable holding the current amount of inmates. Variable i = 0 to start iterating at the first inmate.
roster = len(name_containers)
i = 0
f = open('linn_roster.txt', 'w')
f.write(time_containers[3].text)
while i < roster:
    f.write(name_containers[i].text)
    f.write("\n")
    i += 1

f.close()


