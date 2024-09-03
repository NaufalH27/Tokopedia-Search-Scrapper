from .import process_raw_data
from . import raw_data_pool
from bs4 import BeautifulSoup


def tokopedia(html):
    data_bucket_list = []
    soup = BeautifulSoup(html, features="html.parser")
    product_container = soup.find('div', {'data-testid': 'cntrFindProductsResult'})
    if product_container:
        all_product_div = product_container.find_all('div', {'data-ssr':"findProductSSR"})
    else:
        return
    
    for product_div in all_product_div:
        data_bucket = raw_data_pool.collect_data(product_div)
        processed_data_bucket = process_raw_data.get_processed_data(data_bucket)
        data_bucket_list.append(processed_data_bucket)

    return data_bucket_list