from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq # Web client
from more_itertools import unique_everseen
import os

# URl to web scrap from.
# in this script we web scrape products from the clearance section of currys
page_url = "https://www.box.co.uk/weekly-deals/sort/Category/refine/o~all"

# soup = soup.encode('utf-8')

# opens the connection and downloads html page from url
uClient = uReq(page_url)

# parses html into a soup data structure to traverse html
# as if it were a json data type.
page_soup = soup(uClient.read(), "html.parser")
uClient.close()

# name the output file to write to local disk
out_filename = "BOX.csv"

# header of csv file to be written
headers = "product_name,price,desc,link,image\n"

# opens file, and writes headers
f = open(out_filename, "w")
f.write(headers)



test = page_soup.find("div", {"class","product-list weekly-deals-products"})
containers = test.findAll("div",{"class","product-list-item"})

for container in containers:

    product_name = container.img['data-title']
    link = container.a['href']
    image = "box.co.uk" + container.img['data-src']
    
    price = container.find('span',{'class','pq-price'})['data-inc']
    price = price.replace(",","")
    
    desc = str(container.find("ul"))
    desc = desc.replace("</li>\n<li>","|")
    desc = desc.replace("<ul>\n<li>","")
    desc = desc.replace("</li>\n</ul>","|")
    
    # prints the dataset to console
    print("product_name: " + product_name + "\n")
    print("price: " + price + "\n")
    print("desc: " + desc + "\n")
    print("link: " + link + "\n")
    print("image: " + image + "\n")

    desc = str(desc.encode('utf-8')).replace("b'","")
    desc = desc.replace("'","")
    product_name = str(product_name.encode('utf-8')).replace("b'","")
    product_name = product_name.replace("'","")
    image = str(image.encode('utf-8')).replace("b'","")
    image = image.replace("'","")
    link = str(link.encode('utf-8')).replace("b'","")
    link = link.replace("'","")
    
    # writes the dataset to file
    f.write(product_name + ", " + price + ", " + desc + ", " + link + ", "+ image + "\n")


#end of complete for loop

f.close() # closes file

x = open("BOX.csv","r")
lines = x.readlines()
x.close()

y = 2
print(len(lines))
try: 
    for y in range(323):
        del lines[y]
except IndexError:
    print(y)
    
real = open("Box_Deals.csv","w+")
real.write(headers)

for line in lines:
    real.write(line)

real.close()
os.remove("BOX.csv")



    
