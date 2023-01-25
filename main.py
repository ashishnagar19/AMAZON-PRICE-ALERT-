import requests
import lxml
import smtplib
from bs4 import BeautifulSoup
response = requests.get(url="https://www.amazon.in/Doglapan-Hard-Truth-about-Start-Ups"
                            "/dp/067009711X/?_encoding=UTF8&pd_rd_w=p4mIY&content-id=amzn1.sym.a591f53f-b25f-40ba"
                            "-9fb6-d144bc8febfb&pf_rd_p=a591f53f-b25f-40ba-9fb6-d144bc8febfb&pf_rd_"
                            "r=ZMDNPX575WGAKYTFV61Z&pd_rd_wg=8C4Xk&pd_rd_r=4fd29d2c-6715-48bc-a13e-940b9cf08457&ref_="
                            "pd_gw_ci_mcx_mr_hp_atf_m", headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                                                              "AppleWebKit/537.36"
                                                                              " (KHTML, like Gecko) Chrome/"
                                                                              "109.0.0.0 Safari/537.36",
                                                                 "Accept-Language":"en-US,en;q=0.9,hi;q=0.8"})



data = response.text
soup = BeautifulSoup(data, 'lxml')

price = soup.find(name="span", id="price").get_text()
price_without_currency = price.split("₹")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

if price_as_float < 300:
    with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="ash92199@gmail.com", password="password")
            connection.sendmail(from_addr="ash92199@gmail.com", to_addrs="ashishnagar9650@gmail.com",
                  msg=f"Subject:Doglapan price fall\n\nPrice of the product reduces to {price_as_float}. Now you can buy immediately from the link below\n\nhttps://www.amazon.in/Doglapan-Hard-Truth-about-Start-Ups/dp/067009711X/?_encoding=UTF8&pd_rd_w=p4mIY&content-id=amzn1.sym.a591f53f-b25f-40ba-9fb6-d144bc8febfb&pf_rd_p=a591f53f-b25f-40ba-9fb6-d144bc8febfb&pf_rd_r=ZMDNPX575WGAKYTFV61Z&pd_rd_wg=8C4Xk&pd_rd_r=4fd29d2c-6715-48bc-a13e-940b9cf08457&ref_=pd_gw_ci_mcx_mr_hp_atf_m")
