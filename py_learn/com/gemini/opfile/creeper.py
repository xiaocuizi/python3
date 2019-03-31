from urllib.request import urlopen
from bs4 import BeautifulSoup

url = r"http://www.jueshitangmen.info/tian-meng-bing-can-11.html"
try:
    print("开始open....")
    html = urlopen(url).read().decode("utf-8")
    print(html)
except:
    print("出错啦。")
    raise
finally:
    print("完成啦。")
    pass

