# -*- coding: utf-8 -*-

import re
import urllib
from bs4 import BeautifulSoup

url = "https://conferencealerts.com/country-listing.php?page=1&ipp=All&country=Indonesia"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.find(id ='searchResultTable')
bom = str(text)
paragraphs = re.sub("(<[^>]*?>)", "", bom)
rmv = re.sub('^\s+', '', paragraphs, flags=re.MULTILINE)
print rmv

htms = open("write.txt","w")
htms.write(rmv)
htms.close()