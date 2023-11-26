import requests
from bs4 import BeautifulSoup

# URL of the author's KDnuggets page
url = 'https://www.kdnuggets.com/author/kanwal-mehreen/page/3'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all blog entries
blog_entries = soup.find_all(class_='li-has-thumb__content')

# Iterate over each blog entry and extract information
for entry in blog_entries:
    # Extract the title
    title_element = entry.find('a')
    title = title_element.text.strip()

    # Extract the link
    link = title_element['href']

    # Extract the summary
    summary_element = entry.find(class_='author-post-excerpt')
    summary = summary_element.text.strip()
    
    # Print the extracted information
    print(f'Title: {title}')
    print(f'Link: {link}')
    print(f'Summary: {summary}')
    print()