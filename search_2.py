
### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    
    ### ここに検索ロジックを書く
    if word in source:
        print (f"{word}が見つかりました")
    else:
        print(f"{word}が見つからなかったので")
        source.append(word)
        print(f"{word}をリストに追加しました")
        print(source)

if __name__ == "__main__":
    search()
