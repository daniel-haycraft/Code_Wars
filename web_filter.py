
# redflags = ['staffing', 'talent']
# def get_website_words(url):
#     # Send a GET request to the URL
#     response = requests.get(url)

#     # Parse the HTML content using BeautifulSoup
#     soup = BeautifulSoup(response.content, 'html.parser')

#     # Get all the text from the HTML content
#     text = soup.get_text()
#     text = text.lower()
#     # Split the text into individual words
#     words = text.split()
#     for word in words:
#         if word in redflags:
#             return True

#     # Return the list of words
#     return 'hello'
# import requests
# from bs4 import BeautifulSoup
# running = True

# while running:

#     url= input('please enter your url ')
#     if url == 'quit':
#         running = False
#     else:
#         print(get_website_words(url),url)


import requests
from bs4 import BeautifulSoup

import webbrowser
from plyer import notification

# my_notis = notification.notify(
#     title = title,
#     message = message,
#     app_name = app_name,
#     timeout = timeout,
#     ticker = ticker
# )

# ur= "https://www.google.com/search?q=" 
# response = requests.get(ur)
# webbrowser.open(ur)
# soup = BeautifulSoup(response.content, "html.parser")
# res = soup.find_all('span')
# for r in res:
#     if r.text == '$':
#         print(r)

# def noti_squad(title, message, app_name, timeout, ticker):
#     pass
#     # webbrowser.open(ur)






