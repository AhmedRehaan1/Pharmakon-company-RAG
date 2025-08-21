from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import json
import time

# Setup headless Chrome browser
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # comment this line if you want to see browser
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 10)

# Start at the shop page
driver.get("https://pharmakonegypt.org/shop/")
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul.products li.product")))

# Grab product cards
product_cards = driver.find_elements(By.CSS_SELECTOR, "ul.products li.product")

print(f"Found {len(product_cards)} products...")

data = []

for card in product_cards:
    try:
        name = card.find_element(By.CSS_SELECTOR, ".woocommerce-loop-product__title").text.strip()
        link = card.find_element(By.TAG_NAME, "a").get_attribute("href")

        # Visit product page
        driver.get(link)
        time.sleep(1)

        # Extract price
        try:
            price = driver.find_element(By.CSS_SELECTOR, "p.price").text.strip()
        except:
            price = "N/A"

        # Extract description
        try:
            desc = driver.find_element(By.CSS_SELECTOR, "#tab-description").text.strip()
        except:
            desc = "No description available."

        data.append({
            "product_name": name,
            "product_price": price,
            "product_description": desc,
            "product_link": link  # Added product link to the JSON
        })

        # Return to main shop page
        driver.back()
        time.sleep(1)
    except Exception as e:
        print(f"Skipping product due to error: {e}")
        continue

driver.quit()

# Save to JSON
with open("pharmakon_products.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n✅ Done! Scraped {len(data)} products and saved to pharmakon_products.json")