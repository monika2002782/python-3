# import requests
# from bs4 import BeautifulSoup


# url="http://www.google.com"

# response=requests.get(url)


# soup=BeautifulSoup(response.content,"html.parser")

# write_title=soup.find_all("div")
 




# # for title in write_title:


# #     print(title.get_text())# URL of the webpage to scrape
# url = "https://www.google.com"

# # Send an HTTP GET request to the URL
# response = requests.get(url)

# # Parse the HTML content of the page using BeautifulSoup
# soup = BeautifulSoup(response.content, "html.parser")

# # Find all the article titles using the appropriate HTML tags and attributes
# article_titles = soup.find_all("div")

# # Print the titles of the articles
# for title in article_titles:
#   print(title.get_text())
