import urllib.request as request
import urllib.parse as parse
import re
import time
import os
import random

# from xpinyin import Pinyin


# 添加header
header = \
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        "referer": "https://image.baidu.com"
    }
url = "https://www.baidu.com"
keyword = input("请输入关键字：")
keyword = parse.quote(keyword, 'utf-8')
path = "D://test"
n = 0
order = 0
count = 0
while (n < 1000):
    print("count={}".format(count))
    if count >= 10:
        break
    error_times = 0
    n += 30
    # 关键字(可以可以控制台输入)
    # 获取请求
    url1 = url.format(word=keyword, pageNum=str(n)) + "&t={}".format(time.time())
    req = request.Request(url=url1, headers=header)
    # 打开网页
    try:
        req = request.urlopen(req)
        html = req.read().decode("utf-8")
    except:
        error_times = 1
    if error_times == 1:
        continue
    # 解析结果
    p = re.compile(r"thumbURL.*?\.jpg")
    # p = re.compile(r"https://.*?\.jpg")
    results = p.findall(html)
    # print(results)
    # 创建文件目录存放文件
    if os.path.isdir(path) == False:
        os.makedirs(path)
    for i in results:
        i = i.replace('thumbURL":"', '')
        print(i)
        request.urlretrieve(i, path + "/pic_{num}_{ram}.jpg".format(num=order,
                                                                    ram=random.randint(1, 1000)))
        order += 1
        count += 1
    # 记录总数
