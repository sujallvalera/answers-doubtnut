# Answer Scraper For doubtnut.com
You can now get answer of any prompted question with video explaination. 

# Requirements
- You will need an API Key and Engine ID of Google Custom Search JSON API.

- Create your new Custom Search Engine here to get your Engine ID: https://cse.google.com/cse/create/new

- Add the following website in your Custom Search Engine:
  - https://www.doubtnut.com/

  - You are free to customise your Custom Search Engine by prioritising any of your preferred keywords, excluding any web pages or turning on the 'Safe Search' feature.

  - NOTE: Please don't turn on the 'Search the entire Web' feature as it is currently not possible to scrape from any random sites appearing in the search results.

- Visit here to get your API key: https://developers.google.com/custom-search/v1/overview

- Python 3 installed on your machine.

- BeautifulSoup, Requests and dotenv libary.

**NOTE: You don't need to install these libraries seperately when you install Lyrics Extractor using `pip` but if are cloning this repository then you may use `pip install -r requirements.txt` to install all the project dependencies.**

# How To Use
1. Just run the main.py file on your machine;
```python
   python main.py
```   
2. Enter your question on the given input;
3. Viola! You have recieved your question's answer.

# Usage
This script is intended for educational and experimental purposes only. It should not be used to violate the terms of use of monkeytype.com or any other website. Use this script at your own risk.
