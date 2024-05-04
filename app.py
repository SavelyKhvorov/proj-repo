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
    recipes_to_display = request.args.get('recipes')
    if recipes_to_display:
        recipes_to_display = json.loads(recipes_to_display)
    else:
        recipes_to_display = recipes
    return render_template('index.html', recipes=recipes_to_display)


@app.route('/filters')
def show_filters():
    return render_template('filter.html',recipes=recipes)


@app.route('/apply_filters', methods=['POST'])
def apply_filters():
    price = int(request.json.get('price', 0))
    cooking_time = int(request.json.get('cooking_time', 0))
    difficulty = int(request.json.get('difficulty', 0))
    
    filtered_recipes = [recipe for recipe in recipes if
                   recipe['price'] <= price and
                   recipe['cooking_time'] <= cooking_time and
                   recipe['difficulty'] <= difficulty]
    
    return jsonify({'recipes': filtered_recipes})

if __name__ == "__main__":
    # Запуск приложения Flask
    app.run(host='0.0.0.0', port=5000,debug=True)