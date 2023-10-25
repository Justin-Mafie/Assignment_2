import requests
from bs4 import BeautifulSoup

# Define the URL of the Wikipedia page
url = 'https://en.wikipedia.org/wiki/Data_science'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the paragraph elements on the page
    paragraphs = soup.find_all('p')

    # Initialize a counter for paragraphs containing the word 'learning'
    learning_paragraphs = 0

    # Iterate through the paragraphs and count those containing 'learning'
    for paragraph in paragraphs:
        if 'learning' in paragraph.text:
            learning_paragraphs += 1

    # Print the total number of paragraphs and the number containing 'learning'
    total_paragraphs = len(paragraphs)
    print(f"Total paragraphs: {total_paragraphs}")
    print(f"Paragraphs containing 'learning': {learning_paragraphs}")
else:
    print("Failed to retrieve the page. Status code:", response.status_code)
