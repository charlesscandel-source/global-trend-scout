# Global Trend Scout Data Hub

**Unlock the Future of E-commerce: Weekly Drops of 50 High-Growth, Low-Competition Products**

Are you tired of guessing which products will explode on the market? Global Trend Scout delivers curated, data-driven insights straight to your inbox every Monday. Our AI-powered system scrapes the latest trends from Shopify, TikTok, and Amazon, filters for problem-solving innovations, and provides direct supplier links to AliExpress and CJDropshipping.

**Perfect for:**
- E-commerce entrepreneurs
- Dropshippers
- Product researchers
- Trend analysts
- Resellers looking for the next big thing

## Features

- **Automated Weekly Data Drops**: 50+ products with growth potential
- **Multi-Source Intelligence**: Shopify new arrivals, TikTok viral trends, Amazon movers
- **Problem-Solving Focus**: Only products that solve real customer needs
- **Supplier Integration**: Direct links to reliable suppliers
- **Google Sheets Export**: Ready-to-use data format
- **Discord Community**: Join our Alpha Room for exclusive insights

## Pricing

**$39/month** - Unlimited access to weekly data drops and community support.

Subscribe now on [Whop.com](https://whop.com/global-trend-scout)!

## Installation

### Requirements
- Python 3.8+
- pip

### Install from Source
```bash
git clone https://github.com/yourusername/global-trend-scout.git
cd global-trend-scout
pip install -e .
```

### Or Install via pip (once published)
```bash
pip install global-trend-scout
```

## Usage

### Run the Complete Pipeline
```bash
trend-scout --run-all
```

### Run Individual Components
```bash
trend-scout --shopify    # Scrape Shopify new arrivals
trend-scout --tiktok     # Get TikTok trends
trend-scout --amazon     # Export Amazon movers
trend-scout --clean      # Process and filter data
```

### Output
- `shopify_new_arrivals.csv`: Raw Shopify data
- `tiktok_mademebuyit.csv`: TikTok trend data
- `amazon_movers_shakers.csv`: Amazon top products
- `master_data.csv`: Final curated list with supplier links

## Configuration

Create a `config.json` file for API keys and settings:
```json
{
  "google_sheets": {
    "service_account_file": "path/to/service_account.json",
    "spreadsheet_id": "your_spreadsheet_id"
  },
  "tiktok": {
    "session_id": "your_tiktok_session"
  }
}
```

## Subscription & Support

- **Subscribe**: [Whop.com/global-trend-scout](https://whop.com/global-trend-scout)
- **Community**: Join our Discord Alpha Room (included with subscription)
- **Support**: Email support@globaltrendscout.com

## License

MIT License - See LICENSE file for details.

## Disclaimer

This tool scrapes public data. Use responsibly and in accordance with website terms of service. We are not responsible for any misuse.