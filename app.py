from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__, static_url_path='/static')

recipes = [
    {
        "title": "Сырный суп",
        "description": "Вкусно, просто, сырно",
        "image": "soupe.jpg",
        "price": 200,
        "cooking_time": 10,
        "difficulty": 1,  # легко
        "route": "soupe.html"
    },
    {
        "title": "Макакроны по-флотски",
        "description": "Макарошки + фаршик = <3",
        "image": "pasta.jpg",
        "price": 150,
        "cooking_time": 5,
        "difficulty": 1,  # очень легко
        "route": "pasta.html"
    },
    {
        "title": "Картошечка",
        "description": "Ммммм... картошечка)))",
        "image": "potato.jpg",
        "price": 300,
        "cooking_time": 15,
        "difficulty": 1,  # легко
        "route": "potato.html"
    },
    {
        "title": "Перловая каша",
        "description": "Докатились...",
        "image": "perlovka.jpg",
        "price": 250,
        "cooking_time": 20,
        "difficulty": 3,  # средне
        "route": "perlovka.html"

    },
    {
        "title": "Омлет",
        "description": "Простой и вкусный завтрак, который можно приготовить всего за несколько минут.",
        "image": "omlet.jpg",
        "price": 180,
        "cooking_time": 30,
        "difficulty": 3,  # средне
        "route": "omlet.html"
    },
    {
        "title": "Гречка с овощами",
        "description": "Гречка, гркчка, гречка",
        "image": "buckwheat.jpg",
        "price": 170,
        "cooking_time": 10,
        "difficulty": 1,  # легко
        "route": "buckwheat.html"
    }
]



@app.route('/')
def index():
    return render_template('index.html', recipes=recipes)
    
    


if __name__ == "__main__":
    # Запуск приложения Flask
    app.run(host='0.0.0.0', port=5000,debug=True)