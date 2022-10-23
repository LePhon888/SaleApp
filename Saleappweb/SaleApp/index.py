from flask import render_template, request
from SaleApp import app, dao

@app.route("/")
def index():
    categories = dao.load_categories()

    cate_id = request.args.get('category_id')
    products = dao.load_products(cate_id)
    return render_template('index.html', categories=categories, products=products)

if __name__ == "__main__":
    app.run(debug=True)