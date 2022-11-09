import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

URL = "https://www.amazon.com/Instant-Pot-Pressure-Steamer-Sterilizer/dp/B08PQ2KWHS/ref=dp_prsubs_1?pd_rd_w=p67O7&content-id=amzn1.sym.ec3cee7c-6bd8-496a-8166-4fdb6d51cad1&pf_rd_p=ec3cee7c-6bd8-496a-8166-4fdb6d51cad1&pf_rd_r=AHS3HN1XCK3SQEA6VD47&pd_rd_wg=w3Fk2&pd_rd_r=f3ede7b0-2c8a-497f-9951-6f5ca073b838&pd_rd_i=B08PQ2KWHS&psc=1"
headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}
SMTP_ADDRESS = "smtp.gmail.com"
EMAIL = "andeanusha222@gmail.com"
PASSWORD = os.getenv("password")
response = requests.get(url=URL, headers=headers)
response.raise_for_status()
website = response.text

soup = BeautifulSoup(website, "html.parser")
title = soup.find(id="productTitle").get_text().strip()
print(title)
price = soup.find(name="span", class_="a-offscreen")

if float(price.text.split('$')[1]) < 150:
    message = f"{title} is now {price}"

    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="andeanusha24@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}"
        )
