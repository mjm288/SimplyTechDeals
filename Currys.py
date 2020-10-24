from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client


# URl to web scrap from.
# in this script we web scrape products from the clearance section of currys
page_url = "https://www.currys.co.uk/gbuk/search-keywords/xx_xx_xx_xx_xx/-autumn_clearance-/1_50/relevance-desc/xx-criteria.html"


# opens the connection and downloads html page from url
uClient = uReq(page_url)

# parses html into a soup data structure to traverse html
# as if it were a json data type.
page_soup = soup(uClient.read(), "html.parser")
uClient.close()

# finds number of products
products = page_soup.find("strong").text.strip()
products = int(products[products.find('results')-4:-8])

# finds number of pages to go through
if int(products%50) > 0:
    pages = int(products/50 + 1)
else:
        pages = products/50
i = 0
# name the output file to write to local disk
out_filename = "Currys_Deals.csv"
# header of csv file to be written
headers = "product_name,price,desc,link,image\n"

# opens file, and writes headers
f = open(out_filename, "w")
f.write(headers)
for i in range(pages+1):
    
    page_url = "https://www.currys.co.uk/gbuk/search-keywords/xx_xx_xx_xx_xx/-autumn_clearance-/"+str(i+1)+"_50/relevance-desc/xx-criteria.html"    
    uClient = uReq(page_url)
    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()
    
    # finds each product from the store page
    containers = page_soup.findAll("article", {"class": "product result-prd stamped clearfix"})



    # loops over each product and grabs attributes about
    # each product
    for container in containers:
        # Finds all link tags "div"
        make_rating_sp = container.select("div")

        # grabs the price
        # Then cuts out white spaces using .strip()
        price = container.find('strong',{"class": "price"}).text.strip()
        price = price.replace(",","")
        
        # Grabs the text within the first "(a)" tag from within
        # the list of queries.
        product_name = container.a.select("span")[1].text
        product_name = product_name.replace(",","and")

        # grabs the description and makes all bullet points into one string, if empty then leaves desc empty
        try:
            desc = container.findAll("ul", {"class": "productDescription"})[0].text.strip().replace("\n","|")
        except IndexError:
            desc = ""
            
        # grabs link to product
        link = container.find('header',{"class":"productTitle"}).a['href']

        # grabs image of the product
        image = container.find('div',{"class":"product-images"})
        x = image.find('img')
     
        # accounts for different image sources 
        if x is None:
          image = image.source['srcset']
        else:
          image = image.img['src']
    
        
        # prints the dataset to console
        print("product_name: " + product_name + "\n")
        print("price: " + price + "\n")
        print("desc: " + desc + "\n")
        print("link: " + link + "\n")
        print("image: " + image + "\n")

        # writes the dataset to file
        f.write(product_name + ", " + price + ", " + desc + ", " + link + ", "+ image + "\n")
        
 
#end of complete for loop
f.close() # closes file
