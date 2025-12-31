#1-2.py
#いろいろインポート
import pandas as pd
import re

from selenium import webdriver #Webブラウザを自動操作するためのオープンソースのフレームワーク
from selenium.webdriver.common.by import By #Byという要素の探し方を表すクラスの読み込み
from selenium.webdriver.support.ui import WebDriverWait #表示したい項目が表示されるまで待つため
from selenium.webdriver.support import expected_conditions as EC #表示したい項目が表示されるまで待つため
from selenium.webdriver.support.ui import Select #selectクラスをインポート
from selenium.webdriver.chrome.options import Options #ユーザーエージェント
from selenium.common.exceptions import NoSuchElementException
import time

print('実行中')

#ユーザーエージェント
options = Options()
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)

#データフレームの作成
def data(shop,phone,meal,prefecture,Municipality,house_number,build,url,ssl):
    x = pd.DataFrame({'店舗名':shop,
                '電話番号':phone,
                'メールアドレス':meal,
                '都道府県':prefecture,
                '市区町村':Municipality,
                '番地':house_number,
                '建物名':build,
                'URL':url,
                'SSL':ssl
                })
    print(x)
    x.to_csv('1-2.csv',encoding='utf-8-sig',index=False)

#からのリスト
shop_list = []
phone_list = []
meal_list = []
prefecture_list = []
Municipality_list = []
house_number_list = []
build_list = []
url_list = []
ssl_list = []

#URLを取得(50個分の店が表示してある)
options.add_argument('--headless=new') #ブラウザを表示しない
driver = webdriver.Chrome(options=options) #ブラウザを扱えるように接続してくれるもの(今回はChromeを使う)
driver.get('https://r.gnavi.co.jp/eki/0007180/izakaya/rs/?r=1000&sort=LOW') #ぐるなびのURLを取得
# wait = WebDriverWait(driver,10) #オブジェクトを作成し変数waitに代入、第二引数はタイムアウトの秒数
driver.implicitly_wait(3) #すべてのfind_elementが見つかるまで最大N秒待機、これを使うとwebdriverwaitやECを使う必要はない



time.sleep(3)

#50個のお店に移動

URL = ['https://r.gnavi.co.jp/y258000/','https://r.gnavi.co.jp/d0pmr73v0000/','https://r.gnavi.co.jp/1u6anpu20000/','https://r.gnavi.co.jp/jbaxrhfn0000/','https://r.gnavi.co.jp/8j0t801g0000/','https://r.gnavi.co.jp/6xv1g2330000/','https://r.gnavi.co.jp/jpe57fj30000/','https://r.gnavi.co.jp/fevdnvkz0000/','https://r.gnavi.co.jp/hc223jn60000/','https://r.gnavi.co.jp/hbftgz890000/','https://r.gnavi.co.jp/809a67k70000/','https://r.gnavi.co.jp/sn1x2m6g0000/','https://r.gnavi.co.jp/md2p8kvb0000/','https://r.gnavi.co.jp/gt8esxua0000/','https://r.gnavi.co.jp/1uxy658t0000/','https://r.gnavi.co.jp/ny2wrxp80000/','https://r.gnavi.co.jp/jrhvnruw0000/','https://r.gnavi.co.jp/7zzkx4ch0000/','https://r.gnavi.co.jp/cfxgm3490000/','https://r.gnavi.co.jp/s1w26gwr0000/','https://r.gnavi.co.jp/htnzr2re0000/','https://r.gnavi.co.jp/8wjx1apk0000/','https://r.gnavi.co.jp/gwpz4j9t0000/','https://r.gnavi.co.jp/fy55jxf10000/','https://r.gnavi.co.jp/1b6byye60000/','https://r.gnavi.co.jp/fxyrmhzh0000/','https://r.gnavi.co.jp/rcanjvpw0000/','https://r.gnavi.co.jp/y186900/','https://r.gnavi.co.jp/kapxbzst0000/','https://r.gnavi.co.jp/rac7ra0x0000/','https://r.gnavi.co.jp/djt7tuu50000/','https://r.gnavi.co.jp/hueaukdr0000/','https://r.gnavi.co.jp/ae57r8yz0000/','https://r.gnavi.co.jp/y089208/','https://r.gnavi.co.jp/r9bwwkz10000/','https://r.gnavi.co.jp/y690900/','https://r.gnavi.co.jp/frjhraad0000/','https://r.gnavi.co.jp/y016707/','https://r.gnavi.co.jp/8uatghj80000/','https://r.gnavi.co.jp/cf4kr8m60000/','https://r.gnavi.co.jp/ept0xufg0000/','https://r.gnavi.co.jp/5yujradd0000/','https://r.gnavi.co.jp/4zprtk9s0000/','https://r.gnavi.co.jp/d89h808z0000/','https://r.gnavi.co.jp/2nvfjvfj0000/','https://r.gnavi.co.jp/9fc5tw2p0000/','https://r.gnavi.co.jp/3d5zt6df0000/','https://r.gnavi.co.jp/4segx05f0000/','https://r.gnavi.co.jp/y266603/','https://r.gnavi.co.jp/jcwghnea0000/']

for b in URL:
    driver.get(b)        


#__next > div > div.layout_body__aISp9 > main > div.style_resultRestaurant__Oa8cF > div:nth-child(2) > div:nth-child(1) > article > div.style_title__d8_WF > a


# ##「お好み焼き・鉄板焼き てっぱん食堂」をクリック
# #btn_1 = driver.find_element(By.CSS_SELECTOR,'#__next > div > div.layout_body__aISp9 > main > div.style_resultRestaurant__Oa8cF > div:nth-child(2) > div:nth-child(1) > article > div.style_title__d8_WF > a')
# #btn_1.click()
    
    # #確認用
    # shop_list.append('a')
    # phone_list.append('b')
    # meal_list.append('c')
    # prefecture_list.append('d')
    # Municipality_list.append('e')
    # house_number_list.append('f')
    # build_list.append('g')
    # url_list.append('h')
    # ssl_list.append('i')

    #店舗名
    #header-wrapper > div > div.column-upper.column-upper--left > div > div:nth-child(1) > h1 > a
    shop = driver.find_element(By.CSS_SELECTOR,'#header-wrapper a')
    shop_name = shop.text.replace('\n', ' ')
    shop_list.append(shop_name)
    # print(shop.text)

    #電話番号
    #info-phone > td > ul:nth-child(1) > li:nth-child(1) > span.number
    phone = driver.find_element(By.CSS_SELECTOR, "#info-phone .number")
    if phone:
      phone_list.append(phone.text)
    else:
       phone_list.append('')
    # print(phone.text)

    #メールアドレス(保留)
    # meal = driver.find_element(By.)
    # meal_list.append(meal)
    meal_list.append('')

    # 住所
    region = driver.find_element(By.CLASS_NAME,'region')
    #都道府県
    prefecture_re = re.search(r'.+[都道府県]',region.text)
    prefecture_list.append(prefecture_re.group())
    # print(f"都道府県：{prefecture_re.group()}")

    # 市区町村
    Municipality_re = re.search(r'[都道府県](.*?)[0-9]',region.text)
    Municipality_list.append(Municipality_re.group(1))
    # print(f"市区町村：{Municipality_re.group(1)}")

    #番地
    house_number_re = re.search(r'[0-9].+',region.text)
    house_number_list.append(house_number_re.group())
    # print(f"番地：{house_numbe_re.group()}")

    #建物名
    try:
        build = driver.find_element(By.CLASS_NAME, 'locality')
        build_list.append(build.text)
        # print(f"建物名：{build.text}")
    except NoSuchElementException:
        build_list.append('')

    #URL
    try:
        url = driver.find_element(By.CSS_SELECTOR,'#sv-site > li > a')
        URL1 = url.get_attribute('href') #href属性の値が帰ってくる
        url_list.append(URL1)
        # print(f"URL：{URL}")
        ## SSL
        try: #エラーの可能性がある処理 
            driver.get(URL1)
            ssl_list.append('True')
        except Exception:
            ssl_list.append('False')
    except NoSuchElementException:
        url_list.append('')
        ssl_list.append('')
    # url = driver.find_element(By.CSS_SELECTOR,'#sv-site > li > a')
    # URL = url.get_attribute('href') #href属性の値が帰ってくる
    # print(f"URL:{URL}")

    # #SSL
    # if not URL: #URLがないなら
    #     ssl_list.append('')
    #     # print('')
    # else: #それ以外
    #     try: #エラーの可能性がある処理
    #         driver.get(URL)
    #         ssl_list.append('True')
    #     except Exception:
    #         ssl_list.append('False')
    
    driver.back()  #元のページに戻る

data(shop_list,phone_list,meal_list,prefecture_list,Municipality_list,house_number_list,build_list,url_list,ssl_list)

time.sleep(3)
driver.quit()


import os
print(os.getcwd()) #保存したCSVファイルがどこにあるのか確認できる




