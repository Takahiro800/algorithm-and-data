# 書籍「アルゴリズムとデータ構造」の学習ノート

## 繰り返しの標準入力について

```python
from sys inport stdin
A = sys.stdin.readline()
```
上記のように `sys.stdin.readline()`を使うと、input()よりかなり高速に取得することができるようになる

## リストの中身を半角区切りで出力したい
```python
def print_hankaku:
  return ' '.join(list)
```
上記のようにすれば良い。
注意すべきは、
- リストの各要素はString型でないといけない。intではエラーが起きる。
- `" "`の中身で各要素を区切ることになる
