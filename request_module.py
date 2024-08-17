import requests

query = input("what type of news you want to read?: ")
# Fetch the news data
response = requests.get(
    f"https://newsapi.org/v2/everything?q={query}&from=2024-07-16&sortBy=publishedAt&apiKey=f05ae6f0e5264094b923fb13079ca407"
)

# Parse the JSON response
news_data = response.json()

for article in news_data['articles']:
    print(f"""
Name: 
        {article['source']['name']}
Author: 
        {article['author']}   
Title: 
        {article['title']}
Description: 
        {article['description']}
Read more about at: 
        {article['url']}
        \n\n
        """)
