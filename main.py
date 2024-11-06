import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL = 'gsmws111@gmail.com'
PASSWORD = 'nlqgvcpzhdcjoomc'

def scrape_data():
    url = 'https://www.mercadolivre.com.br/samsung-galaxy-s23-256-gb-5g-preto-8-gb-ram/p/MLB21436188#reco_item_pos=1&reco_backend=item_decorator&reco_backend_type=function&reco_client=home_items-decorator-legacy&reco_id=803029a5-b5ee-40ea-9e35-7e2c1ed788b6&reco_model=&c_id=/home/navigation-trends-recommendations/element&c_uid=2cdbb5a4-a6e1-4a8c-b38d-733aacde0b9f&da_id=navigation_trend&da_position=1&id_origin=/home/dynamic_access&da_sort_algorithm=ranker'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.find('h1', class_='ui-pdp-title').text.strip()
    price = soup.find('span', class_='andes-money-amount__fraction').text.strip()
    color = soup.find('span', id='picker-label-COLOR').text.strip()

    return title, price, color

def send_email(title, price, color):
    msg = MIMEMultipart()
    msg['From'] = EMAIL
    msg['To'] = 'westvsantana@gmail.com'
    msg['Subject'] = 'Detalhes do Produto'

    body = f"""
    Detalhes do Produto:
    - Título: {title}
    - Preço: R$ {price}
    - Cor: {color}
    """
    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)

def main():
    title, price, color = scrape_data()

    send_email(title, price, color)

if __name__ == '__main__':
    main()
