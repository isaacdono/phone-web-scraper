from bs4 import BeautifulSoup
import requests

# Setup for the link of the most selled phones at Magazine Luiza
def setup_for_page(page_number: int):
    url = f'https://www.magazineluiza.com.br/celulares-e-smartphones/l/te/entity---celular/\
    ?page={str(page_number)}&sortOrientation=desc&sortType=soldQuantity'
    print(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

# Fetched info will be if it's recommended, the product basic info, rating and price, like bellow

#<p color="" class="sc-dtInlm dPncPq">
# magalu indica
# </p>

# <h2 data-testid="product-title" font-size="1,1,1" font-weight="regular" class="sc-gQSkpc iWaBVz">
# Smartphone Samsung Galaxy A15 6,5" 128GB Azul Claro 4G 4GB RAM Câm. Tripla 50MP + Selfie 13MP 5000mAh Dual Chip
# </h2>

# <span format="score-count" font-size="0,1,1" font-weight="regular" color="text.scratched" class="sc-cezyBN iJpWGJ">
# 4.8 (8326)
# </span>

# <p data-testid="installment" font-size="0,1" font-weight="regular" class="sc-dcJsrY dpUJi sc-bdOgaJ gYMJkM" color="#404040">
# R$&nbsp;1.099,00 em 10x de R$&nbsp;109,90 sem juros
# </p>

# Get products raw data
def fetch_phone_li(n_page: int):
    soup = setup_for_page(n_page)
    raw_product_list = soup.find_all('li', class_='sc-fTyFcS iTkWie')
    return raw_product_list

n_page = 1
raw_phone_data = fetch_phone_li(n_page)
