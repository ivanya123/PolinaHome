# -coding:utf-8-
import requests
from bs4 import BeautifulSoup
from req_bs4_parcing.data_enter import user_name, password, payload

url = "https://scholar.google.com/scholar?hl=ru&as_sdt=0%2C5&q=A+novel+solid+oxide+electrochemical+oxygen+pump+for+oxygen+therapy&btnG=".replace(
    ' ', '+')

response = requests.get(url)
print(response)

citations = BeautifulSoup(response.text, "html.parser")
text = citations.find_all("div")
print(text)
for i in text:
    print(i.text)
