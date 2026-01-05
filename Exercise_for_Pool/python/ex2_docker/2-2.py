#2-2.py
#いろいろインポート
import requests
import pandas as pd
from bs4 import BeautifulSoup
import re
import time

from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import Session #データを追加・取得・更新・削除
# from models import ex2_2

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String #追加

print('実行中')





#カラム(店舗名、電話番号、メールアドレス、都道府県、市区町村、番地、建物名、URL、SSL)
#テーブルのベースを作る
class Base(DeclarativeBase):
    pass

class ex2_2(Base):
    __tablename__ = 'ex2_2'
    shop:Mapped[str] = mapped_column(
        String(255), 
        primary_key=True
    )
    phone:Mapped[str] = mapped_column(
        String(255), 
        nullable=True
    )
    meal:Mapped[str] = mapped_column(
        String(255), 
        nullable=True
    )
    prefecture:Mapped[str] = mapped_column(
        String(255), 
        nullable=True
    )
    Municipality:Mapped[str] = mapped_column(
        String(255), 
        nullable=True
    )
    house_number:Mapped[str] = mapped_column(
        String(255), 
        nullable=True
    )
    build:Mapped[str] = mapped_column(
        String(255), 
        nullable=True
    )
    url:Mapped[str] = mapped_column(
        String(255), 
        nullable=True
    )
    ssl:Mapped[str] = mapped_column(
        String(255), 
        nullable=True
    )
#テーブルのベースを作る ここまで


# #データフレームの作成
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
    x = x.values.tolist()
    print(x)
    # x.to_csv('1-1.csv',encoding='utf-8-sig',index=False)
    

    #テーブルの内容を作成
    def main():
        engine = create_engine(
            "mysql+pymysql://root:ryoma120208@localhost:3307/gurunabi",
            echo=True
        )
        Base.metadata.create_all(engine)  #テーブル作成
        with Session(engine) as session:
            for i in x:
              # print(len(x))
              user = ex2_2(shop=i[0],phone=i[1],meal=i[2],prefecture=i[3],Municipality=i[4],house_number=i[5],build=i[6],url=i[7],ssl=i[8])
              session.add(user) #データを追加
            session.commit() #データをコミット


    if __name__ == "__main__":
        main()

## URL 50の店舗
URL = ['https://r.gnavi.co.jp/y258000/','https://r.gnavi.co.jp/d0pmr73v0000/','https://r.gnavi.co.jp/1u6anpu20000/','https://r.gnavi.co.jp/jbaxrhfn0000/','https://r.gnavi.co.jp/8j0t801g0000/','https://r.gnavi.co.jp/6xv1g2330000/','https://r.gnavi.co.jp/jpe57fj30000/','https://r.gnavi.co.jp/fevdnvkz0000/','https://r.gnavi.co.jp/hc223jn60000/','https://r.gnavi.co.jp/hbftgz890000/','https://r.gnavi.co.jp/809a67k70000/','https://r.gnavi.co.jp/sn1x2m6g0000/','https://r.gnavi.co.jp/md2p8kvb0000/','https://r.gnavi.co.jp/gt8esxua0000/','https://r.gnavi.co.jp/1uxy658t0000/','https://r.gnavi.co.jp/ny2wrxp80000/','https://r.gnavi.co.jp/jrhvnruw0000/','https://r.gnavi.co.jp/7zzkx4ch0000/','https://r.gnavi.co.jp/cfxgm3490000/','https://r.gnavi.co.jp/s1w26gwr0000/','https://r.gnavi.co.jp/htnzr2re0000/','https://r.gnavi.co.jp/8wjx1apk0000/','https://r.gnavi.co.jp/gwpz4j9t0000/','https://r.gnavi.co.jp/fy55jxf10000/','https://r.gnavi.co.jp/1b6byye60000/','https://r.gnavi.co.jp/fxyrmhzh0000/','https://r.gnavi.co.jp/rcanjvpw0000/','https://r.gnavi.co.jp/y186900/','https://r.gnavi.co.jp/kapxbzst0000/','https://r.gnavi.co.jp/rac7ra0x0000/','https://r.gnavi.co.jp/djt7tuu50000/','https://r.gnavi.co.jp/hueaukdr0000/','https://r.gnavi.co.jp/ae57r8yz0000/','https://r.gnavi.co.jp/y089208/','https://r.gnavi.co.jp/r9bwwkz10000/','https://r.gnavi.co.jp/y690900/','https://r.gnavi.co.jp/frjhraad0000/','https://r.gnavi.co.jp/y016707/','https://r.gnavi.co.jp/8uatghj80000/','https://r.gnavi.co.jp/cf4kr8m60000/','https://r.gnavi.co.jp/ept0xufg0000/','https://r.gnavi.co.jp/5yujradd0000/','https://r.gnavi.co.jp/4zprtk9s0000/','https://r.gnavi.co.jp/d89h808z0000/','https://r.gnavi.co.jp/2nvfjvfj0000/','https://r.gnavi.co.jp/9fc5tw2p0000/','https://r.gnavi.co.jp/3d5zt6df0000/','https://r.gnavi.co.jp/4segx05f0000/','https://r.gnavi.co.jp/y266603/','https://r.gnavi.co.jp/jcwghnea0000/']

#ユーザーエージェントを設定
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

##店舗名
p_string = []
for i in URL:
  time.sleep(3)  
  res = requests.get(i,headers=headers)
  res.encoding = 'utf-8'
  soup = BeautifulSoup(res.text,'html.parser')
  p_tag = soup.find('p',id = 'info-name') #'p'というタグをすべて見つける
  #p_string.append(p_tag)
  for s in p_tag:
    p_string.append(s.get_text(strip=True)) #前後の 空白・改行・タブを自動で除去
    text = s.get_text(strip=True).replace('\xa0', ' ')
#print(p_string)

# #電話番号
span_string = [] #空のリスト
for i in URL: #50のURLを回す
  time.sleep(3)    
  res = requests.get(i,headers=headers) #URLの取得
  soup = BeautifulSoup(res.text,'html.parser')
  span_tag = soup.find('span',class_="number") #電話番号
  for s in span_tag:
    span_string.append(s.get_text(strip=True)) #前後の 空白・改行・タブを自動で除去
#  span_string.append(span_tag.get_text(strip=True)) #リストに追加
#print(span_string)

##メールアドレス
#(仮)
z_string = [] #空のリスト
for i in URL: #50のURLを回す
  z_string.append(' ')
  # time.sleep(3) 
  # res = requests.get(i,headers=headers) #URLの取得
  # soup = BeautifulSoup(res.text,'html.parser')
  # z_tag = soup.find('span',class_="number") #電話番号
  # for s in z_tag:
  #   z_string.append(s.get_text(strip=True)) #前後の 空白・改行・タブを自動で除去
#  span_string.append(span_tag.get_text(strip=True)) #リストに追加
#print(z_string)

##都道府県
a_string = []
for i in URL:
  time.sleep(3) 
  res = requests.get(i,headers=headers)
  res.encoding = 'utf-8'
  soup = BeautifulSoup(res.text,'html.parser')
  a_tag = soup.find('span',class_="region") #住所
  a_tags = a_tag.get_text(strip=True)
  a_re = re.search(r'.+[都道府県]',a_tags)
  a_string.append(a_re.group())
  # for s in a_re.group():
  #   a_string.append(s.get_text(strip=True)) #前後の 空白・改行・タブを自動で除去
#print(a_string)

##市区町村
y_string = [] #空のリスト
for i in URL: #50のURLを回す
  time.sleep(3) 
  res = requests.get(i,headers=headers) #URLの取得
  res.encoding = 'utf-8'
  soup = BeautifulSoup(res.text,'html.parser')
  y_tag = soup.find('span',class_="region") #住所
  y_tags = y_tag.get_text(strip=True)
  y_re = re.search(r'[都道府県](.*?)[0-9]',y_tags) #都道府県から0-9の数字まで取得
  y_string.append(y_re.group(1)) #グループ1(.*?)を取得
  # for s in y_tag:
  #   y_string.append(s.get_text(strip=True)) #前後の 空白・改行・タブを自動で除去
#  span_string.append(span_tag.get_text(strip=True)) #リストに追加
#print(y_string)

##番地
w_string = [] #空のリスト
for i in URL: #50のURLを回す
  time.sleep(3) 
  res = requests.get(i,headers=headers) #URLの取得
  soup = BeautifulSoup(res.text,'html.parser')
  w_tag = soup.find('span',class_="region") #住所
  w_tags = w_tag.get_text(strip=True)
  w_re = re.search(r'[0-9].+',w_tags) #番地 数字で始まり最後まで
  w_string.append(w_re.group()) 
  # for s in w_tag:
  #   w_string.append(s.get_text(strip=True)) #前後の 空白・改行・タブを自動で除去
#  span_string.append(span_tag.get_text(strip=True)) #リストに追加
#print(w_string)

##建物名
v_string = [] #空のリスト
for i in URL: #50のURLを回す
  time.sleep(3) 
  res = requests.get(i,headers=headers) #URLの取得
  res.encoding = 'utf-8'
  soup = BeautifulSoup(res.text,'html.parser')
  v_tag = soup.find('span',class_="locality") #建物名
  if not v_tag: #建物名はない場合がある→もしない場合
    v_string.append('')  #リストに追加して数合わせ
    continue #そのまま実行する → これがないと型が混在してエラーがでる
  v_string.append(v_tag.get_text(strip=True)) #前後の 空白・改行・タブを自動で除去
#  span_string.append(span_tag.get_text(strip=True)) #リストに追加
#print(v_string)

##URL
u_string = [] #空のリスト
for i in URL: #50のURLを回す
  time.sleep(3) 
  res = requests.get(i,headers=headers) #URLの取得
  soup = BeautifulSoup(res.text,'html.parser')
  u_tag = soup.select_one('a[href*="gorp.jp"]') 
  if not u_tag: #URLはない場合がある→もしない場合
    u_string.append('')  #リストに追加して数合わせ
    continue #そのまま実行する → これがないと型が混在してエラーがでる
  u_string.append(u_tag.get("href")) #前後の 空白・改行・タブを自動で除去
#  span_string.append(span_tag.get_text(strip=True)) #リストに追加
#print(u_string)

##SSL
t_string = []
for j in u_string:
  time.sleep(3) 
  if not j: #jがないなら
    t_string.append('') #t_stringは何もない
  else: #それ以外
    try: #エラーの可能性がある処理
        requests.get(j, timeout=5) #URLを呼び出す
        t_string.append(True)
    except requests.exceptions.SSLError:
        t_string.append(False)

# #関数の呼び出し
data(p_string,span_string,z_string,a_string,y_string,w_string,v_string,u_string,t_string)

# import os
# print(os.getcwd()) #保存したCSVファイルがどこにあるのか確認できる
