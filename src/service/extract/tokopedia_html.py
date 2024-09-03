from . import fetch_html
from bs4 import BeautifulSoup


def search_product(product_param, pages = 1):
    pages_string = f"?page={pages}"
    html = fetch_html.get_html("https://tokopedia.com/find/" + product_param + pages_string)
    
    return html

