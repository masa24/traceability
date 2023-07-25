```html
{% extends "template.html" %}

{% block content %}
    <style>
        /* ここにpage1.htmlのスタイルを記述 */
        .product-details {
            background-color: #f9fff9;
            border: 1px solid #ccc;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            max-width: 600px;
            margin: 0 auto;
            transform: scale(110%);
            font-size: 150%;
            word-wrap: break-word;

        }

        .product-details p {
            margin: 10px 0;
        }

        .product-details strong {
            color: #69b869;
        }

    </style>

    <h2 class="section-title">栽培歴</h2>
    <div class="product-details">
        <p><strong>ID:</strong> {{id}}</p>
        <p><strong>栽培者:</strong> {{maker}}</p>
        <p><strong>定植月:</strong> {{planting}}</p>
        <p><strong>区画:</strong> {{area}}</p>
        <p><strong>ポット番号:</strong> {{pot_num}}</p>
    </div>
{% endblock %}

```
