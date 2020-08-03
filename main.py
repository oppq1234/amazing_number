import urllib.request as ur
import os
from bs4 import BeautifulSoup as bs

while True:
    name = input("今晚我想來點?(至多輸入快樂六位數)")
    if len(name) <= 6:
        break
    else:
        print("我覺得輸入六位數應該沒有很難")
    

origin = "https://nhentai.net/g/" + name + "/"      #轉換成網址
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
}                                                   #偽裝瀏覽器資訊
for i in range(1,10000):
    url = origin + str(i)
    nowpath = os.path.abspath('.\本' + name)        #獲取當前路徑
    
    try:
        req = ur.Request(url=url,headers=headers)
        result = ur.urlopen(req).read().decode('utf-8')
    except:
        print("無法使用")
        break
    else:
        if not os.path.isdir(nowpath):
            print("新增資料夾。")
            os.mkdir(nowpath)
        html = bs(result)
        img = html.select('section#image-container img')[0]
        imgurl = img.get('src')
        ur.urlretrieve(imgurl, os.path.join(nowpath, str(i) + '.jpg'), reporthook=None, data=None)
        print("已增加第" + str(i) + "頁。")
        time.sleep(1)