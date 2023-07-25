```.html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #e0f2e0;
            overflow: hidden;
        }

        header {
            background-color: #69b869;
            color: #fff;
            padding: 11px;
            text-align: center;
        }

        header h1 {
            margin: 0;
        }

        aside {
            width: 14%;
            background-color: #8ec98e;
            color: #fff;
            padding: 12px;
            position: fixed; /* 画面に固定表示 */
            top: 70px; /* ヘッダーの高さ+10px分だけ下にずらす */
            bottom: 0; /* 画面下端までの高さ */
            left: 0; /* 画面左端からの位置 */
        }

        aside ul {
            list-style: none;
            padding: 0;
            margin: 0;
        }

        aside li {
            margin-bottom: 10px;
        }

        aside a {
            color: #fff;
            text-decoration: none;
            display: block;
            padding: 5px;
            border-radius: 5px;
            background-color: #5d905d;
        }

        aside a:hover {
            background-color: #77b577;
        }

        .content {
            padding: 20px;
            margin-left: 220px;
            margin-top: 0px; /* サイドバーの高さに合わせて上にマージンを設定 */
            min-height: calc(100vh - 60px); /* 画面の高さ - ヘッダーの高さ */
            background-color: #f9fff9;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            translateY(-60 px);
            overflow: hidden;
        }

    </style>
</head>
<body>
    <!-- 共通のヘッダー -->
    <header>
        <h1>グレープベース トレサビリティ</h1>
    </header>
    <!-- 共通のサイドバー -->
    <aside>
        <ul>
            <li><a href="/home/{{ id }}">お問い合わせ商品</a></li>
            <li><a href="/history/{{ id }}">栽培歴</a></li>
            <!--<li><a href="/pesticides/{{ id }}">防除歴</a></li>-->
        </ul>
    </aside>
    <!-- 個別のページコンテンツ -->
    <div class="content">
        {% block content %}{% endblock %}
    </div>
</body>
</html>
