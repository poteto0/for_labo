# Hello World
Pythonでよく使うものをオブジェクト化orスクリプトとしてまとめたものです。
`images`は無視してください。基本的にファイル単位でのダウンロードがおすすめです

## AnimePlot
tiffのスタック画像としてグラフを保存します。保存結果はフォルダで出力されます。
プロットにアニメーションをつけたい場合に利用してください。
最後にImageJなどでgifに変換してください。現状は散布図などには対応していません。時系列データなどで使って貰うといいと思います。
<br>
使用例
```python
import AnimePlot as AP
ap = AP.AnimePlot(パス("a/folda"),横比, 縦比, (0,100)などの形でxlim, ylim)
ap.set_color(["blue", "green"]) # 色のリスト(トラックしたいデータの数だけ色を追加してください)
ap.set_data(x_data, [data1, data2]) # yのデータをリストで渡してください(※色リストとサイズを合わせてください)
ap.set_marker() # マーカーを追加してください
ap.plot_timelapse(10) # インターバルを設定して実際にプロットを保存します
```
実行結果例

![実行例](images/1.gif)

`ap.unset_marker()`でmarkerを消すことができます。

## timeout
機械学習などで待ち時間が長いときにセッションのタイムアウトを防ぐために用いるスクリプトです。
ただし、`pyautogui`のインストールが必要になります。
```
pip install pyautogui
```
別ターミナルで
```
python 使いたいスクリプト.py
```
で使えます。

* `timeout/mouse.py`

マウス移動+クリックによってタイムアウトを阻止できるものに使う。

ex) Google Colaboratory, Kaggle

* `timeout/keybord.py`

キーボードでの入力が必要な場面でお使いください。

ex) ssh接続が必要な時
