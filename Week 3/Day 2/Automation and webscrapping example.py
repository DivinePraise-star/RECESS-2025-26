# Automation and Web Scraping Example
#Realworld Example: Automating the process of scraping product information from an e-commerce website and saving it to a CSV file.   
def scrape_product_info(url):   
    import requests
    from bs4 import BeautifulSoup
    import csv

    # Step 1: Make an HTTP request to the website
    url = "https://www.jumia.ug/?e=500&utm_source=PMAX&utm_medium=Paid&utm_campaign=UG_P-max-RC_Excluding_Brands_JGKids&gad_source=1&gad_campaignid=23887330756&gbraid=0AAAAACeJlnOVYBkMXJmuwY5bGzdn0BaTn&gclid=Cj0KCQjwxvjRBhC2ARIsAI7KJa33qxXKqqlJYQul7MgK6LSjEGC1Kxw5x16nfUDbS7mMivneLW6UYVUaAnKEEALw_wcB"
    response = requests.get(url)
    
    # Step 2: Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Step 3: Extract product information (example: product names and prices)
    products = []
    for product in soup.find_all('div', class_='sku -gallery'):
        name = product.find('span', class_='name').text.strip()
        price = product.find('span', class_='price').text.strip()
        products.append([name, price])
    
    # Step 4: Save the extracted data to a CSV file
    with open('products.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Product Name', 'Price'])
        writer.writerows(products)