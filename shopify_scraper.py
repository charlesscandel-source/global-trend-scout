import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# List of top Shopify stores (example URLs)
shopify_stores = [
    'https://www.supremenewyork.com/shop/new',
    'https://www.palaceskateboards.com/collections/new',
    # Add more top Shopify stores here
]

fallback_products = [
    {'name': 'Wireless Phone Mount', 'price': '$19.99', 'link': 'https://example.com/product/phone-mount', 'source': 'fallback'},
    {'name': 'Portable Mini Blender', 'price': '$29.99', 'link': 'https://example.com/product/mini-blender', 'source': 'fallback'},
    {'name': 'Travel Jewelry Organizer', 'price': '$15.99', 'link': 'https://example.com/product/jewelry-organizer', 'source': 'fallback'},
]

def scrape_new_arrivals(url):
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        products = []
        selectors = [
            'div.product',
            'div.product-card',
            'li.product',
            'article.product',
            'div.grid__item',
            'div.product-grid-item',
        ]
        for selector in selectors:
            for product in soup.select(selector):
                name = product.select_one('h3, h2, .product-title, .title')
                price = product.select_one('.price, .product-price')
                link = product.select_one('a[href]')
                if name and link:
                    products.append({
                        'name': name.get_text(strip=True),
                        'price': price.get_text(strip=True) if price else 'N/A',
                        'link': link['href'],
                        'source': url,
                    })
        if not products:
            print(f'No products found for {url}')
        return products
    except Exception as e:
        print(f'Error scraping {url}: {e}')
        return []

all_products = []
for url in shopify_stores:
    products = scrape_new_arrivals(url)
    all_products.extend(products)
    time.sleep(1)  # Be polite

if not all_products:
    print('No Shopify products scraped; using fallback sample data.')
    all_products = fallback_products

pd.DataFrame(all_products).to_csv('shopify_new_arrivals.csv', index=False)
print('Shopify scraping complete.')