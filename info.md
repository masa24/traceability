```html
{% extends "template.html" %}

{% block content %}

    <style>
        /* ここにpage1.htmlのスタイルを記述 */
        .container {
            display: flex; /* Use Flexbox */
            justify-content: space-between; /* Distribute the containers evenly along the main axis */
            max-width: 1200px; /* Set the maximum width for the container */
            margin: 0 auto; /* Center the container horizontally */
        }
        .product-details {
            background-color: #f9fff9;
            border: 1px solid #ccc;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            max-width: 800px;
            width: 500px;
            margin: 0 auto;
            transform: scale(110%);
            font-size: 150%;

        }
        .maker-details {
            background-color: #f9fff9;
            border: 1px solid #ccc;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            max-width: 400px;
            margin: 0 auto;
            transform: scale(110%);
            font-size: 150%;

        }
        .product-details p {
            margin: 10px 0;
        }

        .section-title{
            height: 30px;
        }

        .product-details strong {
            color: #69b869;
        }

        .sweet{
            font-size: 130px;
            position: absolute;
            bottom: 40px;
            left: 430px;
            margin-bottom: 20px; /* Add margin at the bottom to create spacing */
        }

    .pic {
        width: 100%; /* Allow the image to take up the full width of its parent container */
        max-width: 100%; /* Add this to ensure the image doesn't exceed its original size */
        display: block; /* Ensure the image behaves as a block-level element */
        height: auto; /* Let the height adjust automatically to maintain aspect ratio */
    }

    .maker-details p {
        max-width: 100%; /* Adjust the paragraph's max width to fit the container */
        margin: 10px 0; /* Optional: Add some vertical margin to the paragraph */
    }


    </style>

    <h2 class="section-title">お問い合わせ商品</h2>
    <div class = "container">
        <div class="product-details">

            <p><strong>ID:</strong> {{id}}</p>
            <p><strong>栽培者:</strong> {{maker}}</p>
            <p><strong>品種:</strong> {{type}}</p>
            <p><strong>重量:</strong> {{ weight }}g</p>
            <p><strong>産地:</strong> {{ location }}</p>
            <p><strong>検査日:</strong> {{ check_date }}</p>
        </div>
        <div class="maker-details">
            <img class = "pic" src="{{ image }}">
            <a href = "{{ quote }}">公式YouTubeへ</a>
        </div>
    </div>


    <p class="sweet"><strong>糖度:</strong> {{ sweet }}　度</p>
{% endblock %}

```
