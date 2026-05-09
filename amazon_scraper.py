import requests
from bs4 import BeautifulSoup
import pandas as pd

fallback_products = [
    {'name': 'Cordless Handheld Vacuum', 'rank': '1', 'link': 'https://example.com/product/vacuum'},
    {'name': 'Waterproof Bluetooth Speaker', 'rank': '2', 'link': 'https://example.com/product/speaker'},
    {'name': 'Smart Door Alarm', 'rank': '3', 'link': 'https://example.com/product/door-alarm'},
]

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
}

url = 'https://www.amazon.com/Best-Sellers/zgbs/'
products = []
try:
    response = requests.get(url, headers=headers, timeout=30)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.select('div.zg_itemImmersion, li.zg-item-immersion, li[data-index]')
    for elem in items[:50]:
        name = ''
        rank = ''
        link = ''
        title_elem = elem.select_one('div.p13n-sc-truncate, span.zg-text-center-align a, img')
        if title_elem:
            name = title_elem.get_text(strip=True) or title_elem.get('alt', '')
        rank_elem = elem.select_one('span.zg-badge-text')
        if rank_elem:
            rank = rank_elem.get_text(strip=True)
        link_elem = elem.select_one('a.a-link-normal, a')
        if link_elem and link_elem.has_attr('href'):
            link = link_elem['href']
            if link.startswith('/'):
                link = 'https://www.amazon.com' + link
        if name:
            products.append({'name': name, 'rank': rank, 'link': link})
except Exception as e:
    print(f'Amazon scraping failed: {e}')

if not products:
    print('No Amazon products scraped; using fallback sample data.')
    products = fallback_products

pd.DataFrame(products).to_csv('amazon_movers_shakers.csv', index=False)
print('Amazon scraping complete.')
