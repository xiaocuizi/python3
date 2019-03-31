from bs4 import BeautifulSoup
url = r"http://www.weather.com.cn/weather/1012270101.html"
html = urlopen(url).read().decode("utf-8")
print(html)