"""
@author: Hangil Kim
"""

from google_images_download import google_images_download #ライブラリ読み込み

response = google_images_download.googleimagesdownload() #クラス指定

searchkeywords = input("Search Keywords: ") #検索する単語を入力
crowlingnumber = int(input("Crawling number for each keywords(~50): ")) #保存する枚数を指定

arguments = {"keywords":searchkeywords,"limit":crowlingnumber,"print_urls":True} #ダウンロード命令
paths = response.download(arguments) #ダウンロードする場所設定
print(paths)   #ダウンロードしたファイルを表示