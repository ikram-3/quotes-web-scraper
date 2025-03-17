import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the website to scrape
base_url = "http://quotes.toscrape.com"
url = base_url

# Dictionary to store the scraped data
data = {"text": [], "author": [], "tags": []}

# Loop through all pages
while True:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract quotes from the current page
    for quote in soup.find_all("div", class_="quote"):
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text
        tags = ", ".join(tag.text for tag in quote.find_all("a", class_="tag"))

        # Append data to the dictionary
        data["text"].append(text)
        data["author"].append(author)
        data["tags"].append(tags)

    # Check for the "Next" button
    next_button = soup.find("li", class_="next")
    if not next_button:
        break  # Exit the loop if there's no "Next" button

    # Update the URL to the next page
    next_page = next_button.find("a")["href"]
    url = base_url + next_page

# Convert the dictionary to a Pandas DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv("quotes.csv", index=False)

# Print the DataFrame
print(df)
