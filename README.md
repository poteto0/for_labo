# for_labo
研究室の授業

## 使い方
ターミナルで作業ディレクトリに移動して
```
git clone https://github.com/poteto0/for_labo.git
```
とコマンドを入力

使いたいスクリプトファイルに
```
source("./for_labo/method/使いたい関数.R")
```
を追加して実行

または使いたい関数をコピペする

## 関数一覧
* calc_velocity:
速度を計算する。
```
data <- calc_velocity(速度を計算したいデータ, 1スライス毎の時間間隔)
```
* moving_average:
移動平均を求める
```
data <- moving_average(移動平均を求めたいデータ, 移動平均間隔)
```
