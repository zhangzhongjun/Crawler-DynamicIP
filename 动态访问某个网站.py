# coding=utf-8
import requests
import os
import json
from fake_useragent import UserAgent
import random
import time

#ua = UserAgent(path="D://Chrome下载内容//手机//user-agents.json",use_cache_server=False)
ua = UserAgent()

url = "http://httpbin.org/get"
url2 = "http://mj70.cn/index.php?id=qweaa"
headers = {
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Accept-Encoding":"gzip, deflate",
"Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
"Cache-Control":"max-age=0",
"Connection":"keep-alive",
"Cookie":"safedog-flow-item=; Hm_lvt_cdce8cda34e84469b1c8015204129522=1532053769;Hm_lpvt_cdce8cda34e84469b1c8015204129522=1532143123",
"Host":"mj70.cn",
"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36"
}
parameter={}
count = 1
while True:

    os.system("rasdial zzj-校园网 /disconnect")
    os.system("RASDIAL zzj-校园网 17151213070 7895123")

    headers["User-Agent"] = ua.random
    try:
        res = requests.get(url,params = parameter,headers=headers,timeout=10)
    except Exception as e:
        continue
        
    
    #print(json.loads(res.text)["origin"])
    
    try:
        res = requests.get(url2,params = parameter,headers=headers,timeout=10)
    except Exception as e:
        print(e)
        continue
    print("第 ",count," 次访问")    
    count = count + 1
    wait = random.randint(10,20)
    print("程序等待 ",wait," s")
    time.sleep(wait)
    