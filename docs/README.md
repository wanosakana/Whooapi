# Whoo API Documentation

ReadTheDocs形式のWhoo APIリファレンスドキュメントです。

## ビルド方法

### 必要なツール

```bash
pip install -r requirements.txt
```

### ドキュメントのビルド

```bash
# HTML形式でビルド
sphinx-build -b html . _build/html

# または make を使用
make html
```

### ローカルで確認

```bash
cd _build/html
python -m http.server 8000
```

ブラウザで `http://localhost:8000` を開いてください。

## ディレクトリ構造

```
whoo-api-docs/
├── index.rst                 # メインインデックス
├── authentication.rst        # 認証
├── user_management.rst       # ユーザー管理
├── location.rst             # 位置情報
├── friends.rst              # フレンド機能
├── messaging.rst            # メッセージング
├── rooms.rst                # ルーム・チャット
├── premium.rst              # プレミアム機能
├── challenges.rst           # チャレンジ
├── other.rst                # その他
├── conf.py                  # Sphinx設定
└── requirements.txt         # Python依存関係
```

## ReadTheDocs.orgにデプロイ

1. GitHubリポジトリを作成
2. このドキュメントをプッシュ
3. ReadTheDocs.orgでリポジトリをインポート
4. 自動ビルドが開始されます

## ライセンス

このドキュメントはネットワークトラフィック解析から生成されています。
