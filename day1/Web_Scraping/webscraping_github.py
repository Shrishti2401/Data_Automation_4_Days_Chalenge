# %%
import requests # type: ignore

# %%
web =requests.get("https://www.flipkart.com/")
print(web.status_code)

# %%
# print(web.content)
# Print the first 500 characters of the content
print(web.content[:500])

# %%
with open("web_content.html", "wb") as file:
    file.write(web.content)

print("Content saved to web_content.html")

# %%
from bs4 import BeautifulSoup # type: ignore

# Parse and prettify the HTML content
soup = BeautifulSoup(web.content, "html.parser")
print(soup.prettify())  # Print the first 500 characters of the prettified content

# %%
soup.title.string  # Get the title of the page
print(soup.title.string)  # Print the title of the page
# Find all the links on the page
links = soup.find_all("a")
# Print the first 10 links
for link in links[:10]:
    print(link.get("href"))  # Print the href attribute of each link
# Find all the images on the page
images = soup.find_all("img")
# Print the first 10 images
for img in images[:10]:
    print(img.get("src"))  # Print the src attribute of each image
# Find all the headings on the page
headings = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
# Print the first 10 headings
for heading in headings[:10]:
    print(heading.text.strip())  # Print the text of each heading
# Find all the paragraphs on the page
paragraphs = soup.find_all("p")
# Print the first 10 paragraphs
for paragraph in paragraphs[:10]:
    print(paragraph.text.strip())  # Print the text of each paragraph
# Find all the divs on the page
divs = soup.find_all("div")
# Print the first 10 divs
for div in divs[:10]:
    print(div.text.strip())  # Print the text of each div
# Find all the spans on the page
spans = soup.find_all("span")
# Print the first 10 spans
for span in spans[:10]:
    print(span.text.strip())  # Print the text of each span
# Find all the lists on the page
lists = soup.find_all("ul")
# Print the first 10 lists
for lst in lists[:10]:
    print(lst.text.strip())  # Print the text of each list
# Find all the list items on the page
list_items = soup.find_all("li")
# Print the first 10 list items
for item in list_items[:10]:
    print(item.text.strip())  # Print the text of each list item
# Find all the forms on the page
forms = soup.find_all("form")
# Print the first 10 forms
for form in forms[:10]:
    print(form.text.strip())  # Print the text of each form
# Find all the tables on the page
tables = soup.find_all("table")
# Print the first 10 tables
for table in tables[:10]:
    print(table.text.strip())  # Print the text of each table
# Find all the table rows on the page
rows = soup.find_all("tr")
# Print the first 10 rows
for row in rows[:10]:
    print(row.text.strip())  # Print the text of each row
# Find all the table headers on the page
headers = soup.find_all("th")
# Print the first 10 headers
for header in headers[:10]:
    print(header.text.strip())  # Print the text of each header
# Find all the table data on the page
data = soup.find_all("td")
# Print the first 10 data cells
for cell in data[:10]:
    print(cell.text.strip())  # Print the text of each data cell
# Find all the scripts on the page
scripts = soup.find_all("script")
# Print the first 10 scripts
for script in scripts[:10]:
    print(script.text.strip())  # Print the text of each script
# Find all the styles on the page
styles = soup.find_all("style")
# Print the first 10 styles
for style in styles[:10]:
    print(style.text.strip())  # Print the text of each style
# Find all the meta tags on the page
meta_tags = soup.find_all("meta")
# Print the first 10 meta tags
for meta in meta_tags[:10]:
    print(meta)  # Print each meta tag
# Find all the links to CSS files on the page
css_links = soup.find_all("link", rel="stylesheet")
# Print the first 10 CSS links
for css in css_links[:10]:
    print(css.get("href"))  # Print the href attribute of each CSS link
# Find all the links to JavaScript files on the page
js_links = soup.find_all("script", src=True)
# Print the first 10 JavaScript links
for js in js_links[:10]:
    print(js.get("src"))  # Print the src attribute of each JavaScript link
# Find all the comments on the page
comments = soup.find_all(string=lambda text: isinstance(text, Comment))
# Print the first 10 comments
for comment in comments[:10]:
    print(comment)  # Print each comment
# Find all the iframes on the page
iframes = soup.find_all("iframe")
# Print the first 10 iframes    
for iframe in iframes[:10]:
    print(iframe.get("src"))  # Print the src attribute of each iframe
# Find all the audio tags on the page
audio_tags = soup.find_all("audio")
# Print the first 10 audio tags
for audio in audio_tags[:10]:
    print(audio.get("src"))  # Print the src attribute of each audio tag
# Find all the video tags on the page
video_tags = soup.find_all("video")
# Print the first 10 video tags
for video in video_tags[:10]:
    print(video.get("src"))  # Print the src attribute of each video tag
# Find all the object tags on the page
object_tags = soup.find_all("object")
# Print the first 10 object tags
for obj in object_tags[:10]:
    print(obj.get("data"))  # Print the data attribute of each object tag
# Find all the embed tags on the page
embed_tags = soup.find_all("embed")
# Print the first 10 embed tags
for embed in embed_tags[:10]:
    print(embed.get("src"))  # Print the src attribute of each embed tag
# Find all the canvas tags on the page
canvas_tags = soup.find_all("canvas")
# Print the first 10 canvas tags
for canvas in canvas_tags[:10]:
    print(canvas)  # Print each canvas tag
# Find all the SVG tags on the page
svg_tags = soup.find_all("svg")
# Print the first 10 SVG tags

for svg in svg_tags[:10]:
    print(svg)  # Print each SVG tag
    

# %%
# Install Selenium if not already installed
%pip install selenium

from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.common.keys import Keys # type: ignore
import time

# Set up the WebDriver (e.g., ChromeDriver)
driver = webdriver.Chrome()  # Ensure you have the ChromeDriver installed and in PATH
driver.get("https://www.flipkart.com/")

# Close the login popup if it appears
try:
	close_button = driver.find_element(By.XPATH, "//button[contains(text(), '✕')]")
	close_button.click()
except:
	pass

# Find the search bar and enter the query
search_box = driver.find_element(By.NAME, "q")  # 'q' is the name attribute of the Flipkart search box
search_box.send_keys("laptop")
search_box.send_keys(Keys.RETURN)

# Wait for the search results to load
time.sleep(2)

html = driver.page_source
lap_soup = BeautifulSoup(html, "html.parser")



# Close the browser after scraping
driver.quit()

# %%
print(lap_soup.prettify()[:1000])  # Print the first 1000 characters of the prettified content

# %%
# Save the prettified HTML content to a file
with open("lap_soup_content.html", "w", encoding="utf-8") as file:
    file.write(lap_soup.prettify())

print("HTML content saved to lap_soup_content.html")

# %%
# Find all the product prices
product_price_data ={
    "listed_Price": [],
    "Discount_Price": [],
    "Discount_Percentage": []

}


# Find all the product properties
product_Properties = {
    "Processor_type": [],
    "RAM": [],
    "Operating_System": [],
    "Storage": [],
    "display_size": [],
    "Warranty": [],
}

# %%
from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.common.keys import Keys # type: ignore
from selenium.webdriver.chrome.options import Options # type: ignore
from bs4 import BeautifulSoup # type: ignore
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (optional)
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.flipkart.com/")

# Close the login popup if it appears
try:
    close_button = driver.find_element(By.XPATH, "//button[contains(text(), '✕')]")
    close_button.click()
except:
    pass

# Find the search bar and enter the query
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("laptop")
search_box.send_keys(Keys.RETURN)

# Wait for the search results to load
time.sleep(3)

# Scroll down to load more results
for _ in range(5):
    driver.execute_script("window.scrollBy(0, 1000);")
    time.sleep(2)

# Get the page source and parse it with BeautifulSoup
html = driver.page_source
lap_soup = BeautifulSoup(html, "html.parser")

# Close the browser
driver.quit()

# Print the parsed HTML (or save it to a file for inspection)
with open("flipkart_laptops.html", "w", encoding="utf-8") as file:
    file.write(lap_soup.prettify())

print("HTML content saved to flipkart_laptops.html")

# %%
product_name=[]

class_data = lap_soup.find_all("div", class_="KzDlHZ")
print(f"Number of items found: {len(class_data)}")  # Print the number of items found
# Print the first 10 items
for item in class_data[:10]:
    product_name.append(item.text.strip())  # Sore Each product in list
# Find all the product names
print(product_name)  # Print the product names

# %%


class_data1 = lap_soup.find_all("div", class_="KzDlHZ")
print(f"Number of items found: {len(class_data1)}")  # Print the number of items found
# Print the first 10 items
for item in class_data1[10:25]:
    product_name.append(item.text.strip())  # Sore Each product in list
# Find all the product names
print(product_name)  # Print the product names

# %%
product_name[10:]

# %%
listed_price = []
discount_price = []
discount_percentage = []
# Find all the product prices
price_divs = lap_soup.find_all("div", class_="hl05eU")
print(f"Number of price divs found: {len(price_divs)}")  # Print the number of price divs found



# %%
# Print the first 10 price divs
for div in price_divs[:10]:
    # Extract data from sub-divs
    listed_price.append(div.find("div", class_="Nx9bqj _4b5DiR").text.strip() if div.find("div", class_="Nx9bqj _4b5DiR") else None)
    discount_price.append(div.find("div", class_="yRaY8j ZYYwLA").text.strip() if div.find("div", class_="yRaY8j ZYYwLA") else None)
    discount_percentage.append(div.find("div", class_="UkUFwK").text.strip() if div.find("div", class_="UkUFwK") else None)


# %%
# Print the first 10 price divs
for div in price_divs[10:]:
    # Extract data from sub-divs
    listed_price.append(div.find("div", class_="Nx9bqj _4b5DiR").text.strip() if div.find("div", class_="Nx9bqj _4b5DiR") else None)
    discount_price.append(div.find("div", class_="yRaY8j ZYYwLA").text.strip() if div.find("div", class_="yRaY8j ZYYwLA") else None)
    discount_percentage.append(div.find("div", class_="UkUFwK").text.strip() if div.find("div", class_="UkUFwK") else None)
len(listed_price), len(discount_price), len(discount_percentage)  # Print the lengths of the lists


# %%
Processor_type = []
RAM = []
Operating_System = []
Storage = []
display_size = []
Warranty = []

# %%
len(product_name), len(listed_price), len(discount_price), len(discount_percentage)


# %%
import csv
# Combine the lists into rows for the CSV
rows = []
for i in range(len(product_name)):
    rows.append({
        "Product Name": product_name[i],
        "Listed Price": listed_price[i],
        "Discount Price": discount_price[i],
        "Discount Percentage": discount_percentage[i]
    })

# Write to CSV
csv_file = "products.csv"
with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Product Name", "Listed Price", "Discount Price", "Discount Percentage"])
    writer.writeheader()
    writer.writerows(rows)

print(f"Data has been written to {csv_file}")

# %%
Ratings=[]
# Find all the ratings
ratings_divs = lap_soup.find_all("div", class_="XQDdHH")
print(f"Number of ratings divs found: {len(ratings_divs)}")  # Print the number of ratings divs found

# %%
ratings_divs

# %%
print(ratings_divs[1].contents[0])

# %%
for div in ratings_divs[:10]:
    # Extract data from sub-divs
    rating = div.contents[0] if div.contents[0] else None
    Ratings.append(rating)  # Store each rating in the list
print(len(Ratings))  # Print the number of ratings found

# %%
for div in ratings_divs[10:]:
    # Extract data from sub-divs
    rating = div.contents[0] if div.contents[0] else None
    Ratings.append(rating)  # Store each rating in the list
print(len(Ratings))  # Print the number of ratings found

# %%
Ratings=Ratings[10:]
len(Ratings)  # Print the number of ratings found after slicing
print(Ratings)  # Print the ratings list after slicing

# %%
csv_file = "products.csv"
rows = []
with open(csv_file, mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for i, row in enumerate(reader):
        # Add the new column data to each row
        row["Ratings"] = Ratings[i] if i < len(product_name) else None
        rows.append(row)

# Write the updated data back to the CSV file
with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    fieldnames = list(rows[0].keys())  # Get all column names, including the new one
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Ratings column has been added to {csv_file}")

# %%
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (optional)
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.flipkart.com/")

# Close the login popup if it appears
try:
    close_button = driver.find_element(By.XPATH, "//button[contains(text(), '✕')]")
    close_button.click()
except:
    pass

# Find the search bar and enter the query
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("laptop")
search_box.send_keys(Keys.RETURN)

# Wait for the search results to load
time.sleep(3)


html1 = driver.page_source
listed_soup = BeautifulSoup(html1, "html.parser")




# %%
product_prop=[]

# %%
import re
div_element = listed_soup.find_all("div", class_=re.compile("6NESgJ"))
print(f"Number of div elements found: {len(div_element)}")  # Print the number of div elements found
# Print the first 10 div elements
for div in div_element[10:]:
    if div:
      ul_element = div.find("ul", class_="G4BRas") 
      specs = [li.text.strip() for li in ul_element.find_all("li")]
      product_prop.append(specs)  # Store each product property in the list








      # Processor=ul_element.find_all("li")[0].text.strip() if ul_element.find_all("li")[0].text.strip() else None
      # RAM_type=ul_element.find_all("li")[1].text.strip() if ul_element.find_all("li")[1].text.strip() else None
      # Operating_Sys=ul_element.find_all("li")[2].text.strip() if ul_element.find_all("li")[2].text.strip() else None
      # Stor=ul_element.find_all("li")[3].text.strip() if ul_element.find_all("li")[3].text.strip() else None
      # display_s=ul_element.find_all("li")[4].text.strip() if ul_element.find_all("li")[4].text.strip() else None
      # Warrant=ul_element.find_all("li")[5].text.strip() if ul_element.find_all("li")[5].text.strip() else None

      # Processor_type.append(Processor)
      # RAM.append(RAM_type)
      # Operating_System.append(Operating_Sys)
      # Storage.append(Stor)
      # display_size.append(display_s)
      # Warranty.append(Warrant)

         
      # specs = [li.text.strip() for li in ul_element.find_all("li")]
      # print(specs)
    else: 
      print("Element not found!")
    
print(len(product_prop))  # Print the number of product properties found


# Extract list items




# Close Selenium WebDriver
driver.quit()

# # Print the extracted data
# print("Processor Type:", len(Processor_type))
# print("RAM:", len(RAM))
# print("Operating System:", len(Operating_System))
# print("Storage:", len(Storage))
# print("Display Size:", len(display_size))
# print("Warranty:", len(Warranty))


# %%
import csv

# Example: product_prop is a list of lists
# product_prop = [["Processor", "RAM", "Storage"], ["Intel i5", "8GB", "512GB SSD"], ...]

# Write to CSV
csv_file = "product_properties.csv"
with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(product_prop)  # Write each sublist as a row

print(f"Data has been written to {csv_file}")

# %%
len(class_data),len(price_divs),len(ratings_divs),len(div_element)

# %%
csv_file = "products.csv"
rows = []
with open(csv_file, mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for i, row in enumerate(reader):
        # Add the new column data to each row
        row["Index"] = i+1 if i < len(product_name) else None
        rows.append(row)

# Write the updated data back to the CSV file
with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    fieldnames = list(rows[0].keys())  # Get all column names, including the new one
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Index column has been added to {csv_file}")

# %%
indexed_properties = []
for i, row in enumerate(product_prop, start=1):  # Start index from 1
    indexed_properties.append([i] + row)  # Prepend the index to each row

# Write to CSV
csv_file = "product_properties.csv"
with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Index", "Processor", "RAM", "Storage"])  # Add header row
    writer.writerows(indexed_properties)

print(f"Index column has been added to {csv_file}")


