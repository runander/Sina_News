__author__ = 'Chendi'
#coding=utf-8
import requests
from bs4 import BeautifulSoup
import re
import pandas
import json
res=requests.get('http://news.sina.com.cn/china/')
res.encoding='utf-8'
soup=BeautifulSoup(res.text,'html.parser')
#获取评论数量
commentURL = 'http://comment5.news.sina.com.cn/page/info?version=1&\
format=js&channel=gn&newsid=comos-{}\
&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20'
def getCommentCounts(newsurl):
    m = re.search('doc-i(.+).shtml',newsurl)
    newsid = m.group(1)
    comments = requests.get(commentURL.format(newsid))
    jd = json.loads(comments.text.strip('var data='))
    return jd['result']['count']['total']

#获取文章的详细内容
def getNewsDetails(url):
    details = []
    res=requests.get(url)
    res.encoding='utf-8'
    soup=BeautifulSoup(res.text,'html.parser')
    details = ''.join(soup.select('#artibody')[0].text.strip())
    return details

#获取责任编辑
def getEditors(url):
    res=requests.get(url)
    res.encoding='utf-8'
    soup=BeautifulSoup(res.text,'html.parser')
    editors = soup.select('.article-editor')[0].text.strip('责任编辑：')
    return editors

#获取新闻来源
def getNewsUrl(url):
    res=requests.get(url)
    res.encoding='utf-8'
    soup=BeautifulSoup(res.text,'html.parser')
    newsurl = soup.select('.time-source span a')[0].text
    return newsurl

#获取新闻的时间、标题、链接等内容，作为执行的入口。
for news in soup.select('.news-item'):
    if len(news.select('h2'))>0:
        h2= news.select('h2')[0].text
        time=news.select('.time')[0].text
        href=news.select('a')[0]['href']
        commetns = getCommentCounts(href)
        editors = getEditors(href)
        # newsurl = getNewsUrl(href)
        print(time,h2+'\n',href+'评论数量:',commetns,'责任编辑:'+editors)

