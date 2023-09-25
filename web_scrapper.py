""" 
    Web Scrapper Project 
    @creator: Maks Kasyanchuk
"""

from bs4 import BeautifulSoup

#print("----------------------- All Document Data Section ----------------------------")

def parse_data() -> BeautifulSoup:
    """ Function to parse the data from html document """
    # Open an HTML file to parse its data
    with open("index.html", encoding="UTF-8") as html_doc:
        soup = BeautifulSoup(html_doc, 'html.parser')
    formatted = soup.prettify()
    # Output formatted html data
    print(formatted)

    return formatted

def find_specific_data() -> BeautifulSoup:
    """ Function to parse a specific data of html document """
    # Open an HTML file to parse the data
    with open("index.html", encoding="UTF-8") as html_doc:
        soup = BeautifulSoup(html_doc, 'html.parser')

    # Output all div fields
    print(soup.find_all('div'))

    return soup.find_all('div')


if __name__ == '__main__':
    parse_data()
    print("-------------------------------------------------------")
    find_specific_data()
