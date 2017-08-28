import requests
from bs4 import BeautifulSoup
from lxml import etree

http://www.cnblogs.com/junrong624/p/5533655.html
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
url = 'https://www.amazon.cn/s/ref=amb_link_xZmRV23lO9eCAMd8396fbg_8?ie=UTF8&page=1&rh=n%3A813272051&pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=merchandised-search-left-2&pf_rd_r=YNBZF5FTBS9DGBFKD6K8&pf_rd_r=YNBZF5FTBS9DGBFKD6K8&pf_rd_t=101&pf_rd_p=66d50942-1cfd-4f72-b4a3-0e56f855eca2&pf_rd_p=66d50942-1cfd-4f72-b4a3-0e56f855eca2&pf_rd_i=813108051'
amazon_html = requests.get(url,headers = header )

amazon_html.encoding='utf-8'
amazon_html.text

读取保存下的网页
with open('D:/0.html', 'r',encoding='utf-8') as f:
    product  = f.read()
    
利用xpath
html = etree.parse(product)
循环输出

count = 0
for i in list(range(24)):
    herf = html.xpath('//*[@id="result_%d"]/div/div[3]/div[1]/a/@href'%count)
    count = count + 1
#     print(herf[0])
    with open('D:/test.txt', 'a+') as f1:
         f1.write(herf[0]+'\n')
            
        
