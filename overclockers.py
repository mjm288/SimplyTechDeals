from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client

# URL to web scrap from.
page_url = "https://www.overclockers.co.uk/offers/pc-components?p=1"
uClient = uReq(page_url)
soup = soup(uClient.read(), "html.parser")
uClient.close()
output = "overclockers.csv"
headers = "product_name,image,price,link \n"
f = open(output, "w")
f.write(headers)

categories = ["pc-systems","gaming-laptops","pc-components",
"cases-and-modding","air-cooling","water-cooling","monitors","peripherals","networking"]

for category in categories:
    runNext = True
    pageCount = 1
    while (runNext == True):
        new_url = "https://www.overclockers.co.uk/offers/" + category + "?p=" + str(pageCount)
        print(pageCount)
        if (pageCount > 20):
            runNext = False
            continue
        from bs4 import BeautifulSoup as soup  # HTML data structure
        uClient = uReq(new_url)
        soup = soup(uClient.read(), "html.parser")
        uClient.close()
        
        containers = soup.find_all(class_="artbox")

        for container in containers:
            if ((container.div.select_one("span[class*=price]") is None)):
                runNext = False
                continue;

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

            f.write(product_name.replace(",", "|") + ", " + image + ", " + price.replace(",", "|") + ", " + link + "\n")
        
        pageCount += 1
f.close()
