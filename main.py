import requests
from bs4 import BeautifulSoup
import smtplib
email = "******@gmail.com"
password = "**********"
target_price = 2000
url = "https://www.amazon.com/Fujfilm-X-T4-Mirrorless-XF16-80mm-Kit/dp/B084ZTMFCH/ref=sr_1_3?qid=1679104647&rnid=502394&s=electronics&sr=1-3"
headers = {
    "Accept-Language": "en-US,en;q=0.9,tr-TR;q=0.8,tr;q=0.7,hi;q=0.6",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"

}
response = requests.get(url=url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
product_name = soup.find("span", id="productTitle").get_text().strip()
product_price = int(soup.find("span", class_="a-price-whole").get_text().replace(",", "").replace(".", ""))

if target_price < product_price:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs=email,
                            msg=f"\nPrice of the {product_name} is less than your target price:\n${product_price}\n{url}")
