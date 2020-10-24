from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client

# URL to web scrap from.
page_url = "https://www.overclockers.co.uk/offers/pc-components?p=1"
# opens the connection and downloads html page from url
uClient = uReq(page_url)
soup = soup(uClient.read(), "html.parser")
#print(soup.find_all(class_="artbox"))
containers = soup.find_all(class_="artbox")
#
output = "overclockers.csv"
headers = "product_name,image,price,link \n"
f = open(output, "w")
f.write(headers)


for container in containers:
    #print(container.div.div)
    #print()
    #print()
    #print()
    #print()
    #print()
    #print()
    #print()
    #print()
    #print()
    #print()
    product_name = (container.div.find("a", {"class": "producttitles"})['title']) #product name
    image = (container.div.find("a", {"class": "product_img"}).img['src'])#image
    #print(container.div.find("p", {"class": "pseudoprice"}).select_one("span[class*=price]").text)
   # print(container.div.select('p[class*="price"]').span['price'])
    #.select_one("span[class*=price]").text)
    if (container.div.select_one("span[class*=price]") is None):
        continue;
    else:
        price = (container.div.select_one("span[class*=price]").text)

    link = (container.div.find("a", {"class": "hover_bg"})['href'])
    
    print("product_name: " + product_name + "\n")
    print("image: " + image + "\n")
    print("price: " + price + "\n")
    print("link: " + link + "\n")

    f.write(product_name.replace(",", "|") + ", " + image + ", " + price + ", " + link + "\n")
f.close()



#make_rating_sp = containers[0].div.select("a")
#print(make_rating_sp[0].img["title"].title())