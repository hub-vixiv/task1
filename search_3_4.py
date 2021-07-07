
### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
source=[]
print("キャラクターリストchara.csvを読み込みます")
with open("chara.csv",encoding="utf-8") as f:
    source = f.readline().strip().split(',') 

### 検索ツール
def search():

    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    
    ### ここに検索ロジックを書く
    if word in source:
        print (f"{word}が見つかりました")
    else:
        print(f"{word}は見つかりません")
        ask_add = input(f"{word}をリストに追加しますか？\nはい→ｙ、いいえ→ｎ：")
        if ask_add == "y" :
            source.append(word)
            print(f"{word}をリストに追加しました")
            print(source)
        # else:
        #     pass

    ask_exp = input("現在のリストを書き出しますか？\nはい→ファイル名(拡張子なしで)、いいえ→ｎ：")
    if ask_exp != "n" :
        print(f"現在のリストを{ask_exp}.csvに書き出します")
        file_neme = ask_exp + ".csv"
        with open(file_neme, mode='w',encoding="utf-8") as f:
            f.write(','.join(source))


if __name__ == "__main__":
    search()
