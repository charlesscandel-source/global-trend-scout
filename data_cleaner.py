import os
import pandas as pd


def safe_read_csv(path, default_columns=None):
    if not os.path.exists(path):
        print(f'Warning: missing file {path}')
        return pd.DataFrame(columns=default_columns or [])
    try:
        return pd.read_csv(path)
    except Exception as e:
        print(f'Warning: failed to read {path}: {e}')
        return pd.DataFrame(columns=default_columns or [])

shopify_df = safe_read_csv('shopify_new_arrivals.csv', default_columns=['name', 'link'])
tiktok_df = safe_read_csv('tiktok_mademebuyit.csv', default_columns=['id', 'desc', 'stats', 'author'])
amazon_df = safe_read_csv('amazon_movers_shakers.csv', default_columns=['name', 'link'])

sources = []
if {'name', 'link'}.issubset(shopify_df.columns):
    sources.append(shopify_df[['name', 'link']])
else:
    print('Warning: shopify_new_arrivals.csv is missing expected columns.')
if {'name', 'link'}.issubset(amazon_df.columns):
    sources.append(amazon_df[['name', 'link']])
else:
    print('Warning: amazon_movers_shakers.csv is missing expected columns.')

if sources:
    all_df = pd.concat(sources, ignore_index=True)
else:
    all_df = pd.DataFrame(columns=['name', 'link'])

problem_keywords = ['solve', 'fix', 'improve', 'help', 'tool']
all_df['is_problem_solving'] = all_df['name'].fillna('').str.contains('|'.join(problem_keywords), case=False)
filtered_df = all_df[all_df['is_problem_solving']].copy()
if filtered_df.empty:
    print('No problem-solving products were found in the scraped data.')
filtered_df['supplier_link'] = (
    'https://aliexpress.com/search?keyword=' +
    filtered_df['name'].fillna('').str.replace(' ', '+', regex=False)
)

master_df = filtered_df.head(50)
master_df.to_csv('master_data.csv', index=False)
print('Data cleaning complete.')
