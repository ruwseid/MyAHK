# MyAHK

My AutoHotKey script (AutoHotkey v2).

## 数字・記号レイヤー

無変換 (`vk1D`) が左レイヤー、変換 (`vk1C`) が右レイヤーです。
Karabinerの左右Commandレイヤーと同じ配置にしています。

| レイヤー | キー（左から順） | 出力（左から順） |
|---|---|---|
| 左 | qwert | 12345 |
| 左 | asdfg | 67890 |
| 右 | yuiop | !@#$% |
| 右 | hjkl; | ^&*() |
| 右 | qwer | _-+= |
| 右 | asdfg | ~、二重引用符、[、{、半角パイプ |
| 右 | zxcvb | バッククォート、単一引用符、]、}、バックスラッシュ |

通常の文字・記号キー、無変換との矢印移動・削除、IME切替は維持します。
数字・記号はUnicode指定で送信するため、NumLockやUS/JIS配列の記号位置に依存しません。

`config/num.csv` と `config/num_symbol.csv` を編集したら、リポジトリ直下で
`python genAHK.py` を実行して `include.ahk` を再生成し、`main.ahk` を再読み込みしてください。
CSV・生成スクリプト・生成済みファイルを一緒に管理します。

2026-10-28: 34対応の生成と既存操作との重複を静的確認。Windows上での実入力は未確認。
