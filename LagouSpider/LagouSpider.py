import requests
from bs4 import BeautifulSoup
import math
import pandas as pd

keyword='数据分析'

#发送请求，获取html源码
def get_html(url):
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Content-Encoding':'gzip',
        'Content-Language':'zh-CN',
        'Content-Type':'text/html;charset=UTF-8'
    }
    html = requests.get(url=url,headers=headers).text
    return html

#发送post请求，获取json数据
def post_html(url,parms,data):
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'WEBTJ-ID=20180826175611-16575a99192102-0eba8cee640072-9393265-960000-16575a9919390b; _ga=GA1.2.1659201636.1535277372; _gid=GA1.2.1125272691.1535277372; user_trace_token=20180826175612-43672253-a916-11e8-b36d-525400f775ce; LGSID=20180826175612-436722dc-a916-11e8-b36d-525400f775ce; PRE_UTM=m_cf_cpt_baidu_pc; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fs%3Fie%3DUTF-8%26wd%3D%25E6%258B%2589%25E5%258B%25BE; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpt_baidu_pc; LGUID=20180826175612-43672549-a916-11e8-b36d-525400f775ce; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1535277372; JSESSIONID=ABAAABAAAFCAAEG50D7FF860519438BC6C6EF28E41C246F; TG-TRACK-CODE=index_search; X_HTTP_TOKEN=475c0c9f101a3e41b5dea91ba55a19c3; LG_LOGIN_USER_ID=419661966043c022a5684105373c92d757f72ecb34488734; _putrc=CD839C2A99BB2E8F; login=true; unick=%E5%BC%A0%E5%8F%88%E4%BA%AE; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=289; gate_login_token=e1e193d7f1e818a4e9781a918dfd7950090e97915273a2fa; index_location_city=%E6%B7%B1%E5%9C%B3; _gat=1; LGRID=20180826180245-2e115aae-a917-11e8-b115-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1535277766; SEARCH_ID=94023cb9f331402fb44456082ff787c6',
        'Host': 'www.lagou.com',
        'Origin': 'https://www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
    html = requests.post(url=url, headers=headers,data=data,params = parms).json()
    return html

#得到主要城市
def get_city(html):
    cityname=[]
    soup = BeautifulSoup(html,'html.parser')
    cities = soup.select('.more-city-name')
    for city in cities:
        cityname.append(city.string)
    cityname = list(set(cityname))#进行去重
    return cityname

#每个城市有数据分析岗位需求的页码，将城市和页码信息进行保存到csv文件里面
def get_page(url,cities,pn=1):
    pages=[]
    for city in cities:
        params = {
            'city': city,
            'needAddtionalResult': 'false'
        }
        data = {
            'first': 'first',
            'pn': str(pn),
            'kd': keyword
        }
        jresult = post_html(url,parms=params,data=data)
        pagesize = jresult['content']['pageSize']
        total = jresult['content']['positionResult']['totalCount']
        page = math.ceil(total / float(pagesize))
        print(city, total)
        pages.append(page)
    cities_pages = {
        'city':cities,
        'page':pages
    }
    df = pd.DataFrame(cities_pages)
    df.to_csv('LagouCityPage.csv',encoding='gb18030',index=False)
    return cities_pages

#主体程序，
def main():
    city_url='https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?px=default&city=%E5%85%A8%E5%9B%BD'
    html = get_html(city_url)
    cities=get_city(html)#得到主要的城市
    page_url = 'https://www.lagou.com/jobs/positionAjax.json'
    get_page(url=page_url,cities=cities)#根据主要的城市，获取每个城市的页码数，并进行保存到csv文件

if __name__=='__main__':
    main()