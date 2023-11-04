import requests
from bs4 import BeautifulSoup
from datetime import datetime, timezone 




scraped_dict={}
url = "https://techcrunch.com/"
res = requests.get(url)

soup=BeautifulSoup(res.content, "html.parser")

latest=soup.find(class_='river--homepage')
#article = latest.find_all('div', class_='post-block')

#number of articles
no_of_articles=0
articles=latest.find_all('div',class_='post-block')
for article in articles:
    no_of_articles+=1


#article timestamp
#article_time_stamp=latest.find_all('time', class_="river-byline__time")

#article title
article_title=latest.find_all('h2', class_='post-block__title')

#article small image url
article_image_url_small=latest.find_all('footer',class_="post-block__footer")


#article authors
article_authors=latest.find_all('span', class_="river-byline__authors")

#=======================================================================


for article in range(no_of_articles):
    #list of content for each article
    each_article=[]

    #inserting article title
    each_article.append(article_title[article].find('a').get_text().strip())
    scraped_dict[article]=each_article

    '''
    #inserting article timestamp
    raw_datetime=article_time_stamp[article]['datetime']
    raw_datetime=datetime.strptime(raw_datetime, '%Y-%m-%dT%H:%M:%S%z').astimezone()
    final_datetime=raw_datetime.strftime('%I:%M %p %Z %B %d, %Y')
    scraped_dict[article].append(final_datetime)
    #raw_datetime=parser.parse(raw_datetime).replace(tzinfo=timezone.utc).astimezone(tz=None)
    #raw_datetime=parser.parse(raw_datetime).replace(tzinfo=timezone.utc).astimezone(tz=None)
    '''


    #inserting article image url
    scraped_dict[article].append(article_image_url_small[article].findChildren('img')[0]['src'])

    #inserting article authors
    authors_list=[]
    for author in article_authors[article].find_all('a'):
        authors_list.append(author.get_text().strip())
    scraped_dict[article].append(", ".join(authors_list))

    #article url content
    url_link= article_title[article].find('a')['href']
    scraped_dict[article].append(url_link)


    #Next Page - Full Article setup
    res_content = requests.get(url_link)
    soup_cont = BeautifulSoup(res_content.content, "html.parser")
    lar_image = soup_cont.find(class_='article--post')
    lat_cont = soup_cont.find('div', class_='article-content')
    cont = lat_cont.find_all('p', 'h')


    #article large image url
    article_image_url=lar_image.find_all('div', class_="article__featured-image-wrapper breakout")

    #img_src =article_image_url
    #article_image_url=lat_image.find_all('div', class_="article__content-wrap")
    im_url=""
    for img_element in article_image_url:
        im_url = img_element.find('img')['src']
    scraped_dict[article].append(im_url) 
 
    all_text = ""
    for all_cont in cont:
         all_text += all_cont.get_text()
    scraped_dict[article].append(all_text)
    
    all_txt = ""
    for all_conx in lat_cont:
        #all_txt += all_conx.get_text
        print(all_conx)
        

#for article_post in scraped_dict.values():  
#    print(article_post[4])

    #inserting article image url
    #scraped_dict[article].append(article_image_url[article].findChildren('img')[0]['src'])
    
    #inserting article image url
    #cont_img = article_image_url['src']

    

#print(lat_cont)


    

print('==============================================UPDTD222=========================================')
#print(article)
for article in lat_cont.values():
    print(article)
        

