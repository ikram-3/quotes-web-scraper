# Quotes Web Scraper

This Python script scrapes quotes, authors, and tags from the [Quotes to Scrape](http://quotes.toscrape.com/) website using the `requests` and `BeautifulSoup` libraries. The scraped data is stored in a dictionary, converted into a Pandas DataFrame, and saved as a CSV file.

---

## Prerequisites

Before running the script, ensure you have the following Python libraries installed:

- `requests`
- `beautifulsoup4`
- `pandas`

You can install them using pip:

```bash
pip install requests beautifulsoup4 pandas
```

---


---

## How to Run

1. Clone this repository or download the script.
2. Install the required libraries using `pip` (see **Prerequisites**).
3. Run the script:

```bash
python scrape_quotes.py
```

4. The scraped data will be saved in a file named `quotes.csv`.

---

## Notes

- Ensure you comply with the website's `robots.txt` file and terms of service before scraping.
- Avoid sending too many requests in a short period to prevent overloading the server.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## LICENSE

```text
MIT License

Copyright (c) 2025 Muhammad Ikram

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
