import json
from SaleApp import app

def load_categories():
    with open('%s/data/categories.json' % app.root_path, encoding='utf-8') as f:
        return json.load(f)


def load_products(cate_id=None):
    with open('%s/data/products.json' % app.root_path, encoding='utf-8') as f:
        products = json.load(f)

    if cate_id:
        products = [p for p in products if p['category_id'] == int(cate_id)]

    return products