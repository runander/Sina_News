header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
url = 'https://www.amazon.cn/%E5%8E%A8%E5%85%B7/b/ref=sd_allcat_kitche_l2_b813108051?ie=UTF8&node=813108051'
amazon_html = requests.get(url,headers = header ,verify=False)

for tage in soup.find_all("a"):
    print(tage.get("href"))
    
    //*[@id="result_0"]/div/div[3]/div[1]/a/@href
