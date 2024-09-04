from fastapi import FastAPI
import uvicorn
from service import extract, transform
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from pathlib import Path


app = FastAPI()

static_path = Path(__file__).parent / "docs"/ "static"
templates_path = Path(__file__).parent / "docs" / "templates"

app.mount("/static", StaticFiles(directory=static_path), name="static")

templates = Jinja2Templates(directory=templates_path)


@app.get("/",response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", context= {"request": request}) 


@app.get("/tokopedia/search/{search_parameter}/pages={page}")
def read_product_search(search_parameter, page):
    html = extract.tokopedia_html.search_product(product_param = search_parameter, pages = page)
    product_list = transform.transform_html.tokopedia(html)
    return {
        "type" : "tokopedia search",
        "total_items" : len(product_list),
        "parameter" : search_parameter,
        "page_number" : page,
        "data" : product_list
        }



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)