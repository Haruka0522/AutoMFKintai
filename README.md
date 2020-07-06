# AutoMFKintai

## 特徴
- 毎日同じ時刻に打刻をするという煩わしい行動から開放される
- **悪用厳禁**

## 環境
- GoogleChrome
- ChromeDriver(Chromeのバージョンに適したもの）
- Python 3.7.6

    
## 初期設定
- 環境構築
```
git clone https://github.com/Haruka0522/AutoMFKintai.git
cd AutoMFKintai
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
- ログイン情報ファイルの作成

AutoMFKintaiディレクトリ直下に`pass.txt`を作成。

１行目に会社ID

２行目にメールアドレス

３行目にパスワードを記載する。

    
## 実行方法
```
python main.py
```

## 実行オプション
- `--headless`をつけるとheadlessモードで実行
