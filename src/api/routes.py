from fastapi import APIRouter
from . import schema
from service import extract, transform
import sys



app = APIRouter()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/tokopedia/search/{search_parameter}/pages={page}")
def read_product_search(search_parameter, page):
    html = extract.tokopedia_html.search_product(product_param = search_parameter, pages = page)
    product_list = transform.transform_html.tokopedia(html)
    return {
        "type" : "tokopedia search",
        "total_items" : len(product_list),
        "parameter" : search_parameter,
        "page_number" : page,
        "data" : schema.get_product_list(product_list)
        }
