# AutoMFKintai

## 特徴
- 毎日同じ時刻に打刻をするという煩わしい行動から開放される
- **悪用厳禁**

## 環境
- GoogleChrome
- ChromeDriver(Chromeのバージョンに適したもの）
- Python 3.7.6


## 初期設定
- ラズパイで動かす場合
```
git clone https://github.com/Haruka0522/AutoMFKintai.git
cd AutoMFKintai
chmod +x raspi_setup.sh
./raspi_setup.sh
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

- その他の場合
```
git clone https://github.com/Haruka0522/AutoMFKintai.git
cd AutoMFKintai
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

- configファイルの作成
yaml形式で記載する。
`config/sample.yml`を参考にログインに必要な情報や、出勤/退勤時刻を記載する。

### 注意
myconfig.ymlという名前で作成するとgitの管理から除外される。その他の名前でconfigファイルを作成するときには`.gitignore`にファイル名を追加して、パスワードなどがgithubに公開されないように注意する。


## 実行方法
```
python main.py
```

### 実行オプション
- `--headless`
  - このオプションをつけるとchromeの起動がバックグラウンドで行われる
  - 短縮形`-H`でも可
- `--config_file`
  - configファイルのパスを指定する
  - defaultは`config/myconfig.yml`
