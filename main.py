from lxml import html
from bs4 import BeautifulSoup
import lxml.html
import urllib.request


def extraire_content(url, xpath):
    ## Ouvrir l'URL
    site = urllib.request.urlopen(url).read()
    ## Parser le contenu HTML
    lxml_site = lxml.html.fromstring(site)
    ## Extraire le contenu avec XPath
    description = lxml_site.xpath(xpath)[0]
    ## Convertir le contenu en texte brut
    text = description.text_content()
    
    print(text)

if __name__ == '__main__':
    url = 'https://sulphers.github.io'
    xpath = "//div[@class='hero-content']"
    res = extraire_content(url, xpath)
