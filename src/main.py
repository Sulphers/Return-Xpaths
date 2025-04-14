from lxml import html
from bs4 import BeautifulSoup as soup
import lxml.html
import urllib.request
import sys

#Local file
# with open('index.html', 'r') as f:
#     page = f.read()


### je dois gérer le cas ou il y a plusieurs occurences de la string dans le html
### je dois gerer le cas avec une page Local


def find_string(url):
    if(len(sys.argv) != 2):
        print ("String to search is needed")
        return
    
    stringToFind = sys.argv[1]
    
    response = urllib.request.urlopen(url)
    if response.getcode() != 200:
        print("Error: Unable to fetch the page")
        return
    
    html_content = response.read()
    parsed_soup = soup(html_content, 'html.parser')
    
    
    a_string = parsed_soup.find(string=stringToFind)
    
    if not a_string:
        print("String not found")
        return
    else:
        res = a_string.find_parent()
        print(res)
        print(res.name)

    xpath='xpath=//' + res.name + '[@text()="' + stringToFind + '"]'
    print("Xpath: " + xpath)
    

if __name__ == '__main__':
    url = 'https://sulphers.github.io'
    find_string(url)
