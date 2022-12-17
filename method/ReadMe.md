# Hello World
Rで使えるメソッドを乗せています。他にあれば伝えてください

## 使い方

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
