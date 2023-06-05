import os
from bs4 import BeautifulSoup
import re

# get list of all files in the CONTENTS directory
files = os.listdir('CONTENTS')

# for each file
for filename in files:
    # skip if the file does not have an html extension
    if not filename.endswith('.html'):
        continue

    # open the file with utf-8 encoding
    with open(f'CONTENTS/{filename}', 'r', encoding='utf-8') as file:
        # create BeautifulSoup object
        soup = BeautifulSoup(file, 'html.parser')

        # get the title from the title tag
        title = soup.title.string if soup.title else "No Title"

        # make a valid filename from the title by replacing any non-alphanumeric characters or spaces with an underscore
        valid_filename = re.sub('[^0-9a-zA-Z ]+', '_', title)

        # get the body text by finding the body tag and getting the text
        # use split and join to remove extra whitespace
        body = ' '.join(soup.body.get_text(separator='\n').split()) if soup.body else "No Body Text"

        # save title and body text in a new text file
        with open(f'TEXTS/{valid_filename}.txt', 'w', encoding='utf-8') as new_file:
            new_file.write(f'Title: {title}\n\nBody:\n{body}')
