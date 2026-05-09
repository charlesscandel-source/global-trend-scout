import subprocess
import sys

scripts = [
    'shopify_scraper.py',
    'tiktok_scraper.py',
    'amazon_scraper.py',
    'data_cleaner.py'
]

for script in scripts:
    print(f'Running {script}...')
    result = subprocess.run([sys.executable, script])
    if result.returncode != 0:
        print(f'Script failed: {script} (exit code {result.returncode})')
        break
else:
    print('All phases complete.')
