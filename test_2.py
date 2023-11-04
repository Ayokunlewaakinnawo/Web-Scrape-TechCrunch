import requests
from bs4 import BeautifulSoup
from datetime import datetime, timezone 

scraped_dict={}
url = "https://techcrunch.com/"
res = requests.get(url)

soup=BeautifulSoup(res.content, "html.parser")

latest=soup.find(class_='river--homepage')
articles = latest.find_all('h2', class_='post-block__title')

#number of articles
no_of_articles=0
articles=latest.find_all('div',class_='post-block')
for article in articles:
    no_of_articles+=1

#From the main landing page
#===========================

#article timestamp
article_time_stamp=latest.find_all('time', class_="river-byline__time")

#article title
article_title=latest.find_all('h2', class_='post-block__title')

#article small image url
article_image_url_small=latest.find_all('footer',class_="post-block__footer")


#article authors
article_authors=latest.find_all('span', class_="river-byline__authors")

#article category
article_category=latest.find_all('div', class_="article__primary-category")

for article in range(no_of_articles):
        #list of content for each article
        each_article=[]

        #inserting article title
        each_article.append(article_title[article].find('a').get_text().strip())
        scraped_dict[article]=each_article

        #inserting article timestamp
        raw_datetime=article_time_stamp[article]['datetime']
        raw_datetime=datetime.strptime(raw_datetime, '%Y-%m-%dT%H:%M:%S%z').astimezone()
        final_datetime=raw_datetime.strftime('%I:%M %p %Z %B %d, %Y')
        scraped_dict[article].append(final_datetime)
        
        #inserting article small image url
        scraped_dict[article].append(article_image_url_small[article].findChildren('img')[0]['src'])

        #inserting article authors
        authors_list=[]
        for author in article_authors[article].find_all('a'):
            authors_list.append(author.get_text().strip())
        scraped_dict[article].append(", ".join(authors_list))

        

        #inserting article category
        print(scraped_dict)
        

        #print(scraped_dict)




""""
for article in articles:
    a_tag = article.find('a')
    if a_tag:
        article_url = a_tag.get('href')
"""




