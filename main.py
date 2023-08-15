import requests
from send_email import send_email

api_key = "3dddb5eef9ac4286b9eeac762d7792d6"
topic = "tesla"

url =f"https://newsapi.org/v2/everything?q={topic}& \
       from=2023-07-15&sortBy=publishedAt&apiKey={api_key} \
       &language=en"


request = requests.get(url)
content = request.json()

body = """"""

for article in content['articles'][:20]:
    if article['title'] is not None:
        body = "Subject: News API" + "\n" + body + article['title'] + '\n' + article['description'] + "\n" + article['url'] + 2 * '\n'

body = body.encode('utf-8')    
    
send_email(body)