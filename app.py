from flask import Flask, render_template, request, jsonify
import json
import os
from utils import resize_image

app = Flask(__name__, static_url_path='/static')


IMAGE_DIR = 'static/images/'

def process_images():
    for filename in os.listdir(IMAGE_DIR):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(IMAGE_DIR, filename)
            resize_image(image_path, image_path)


recipes = [
    {
        "title": "Сырный суп",
        "description": '''Сливочный и насыщенный кулинарный шедевр, который порадует ваши вкусовые рецепторы. 
Сваренный из отборных сыров, этот суп отличается богатым и сырным вкусом, который согреет 
вас изнутри. Наслаждайтесь им с хрустящим хлебом или крекерами, чтобы полностью оценить его 
идеальную консистенцию и непревзойденный вкус.
        
        ''',
        "image": "soupe.jpg",
        "price": 150,
        "cooking_time": 30,
        "difficulty": 3,  # легко
        "route": "soupe.html"
    },
    {
        "title": "Макакроны по-флотски",
        "description": '''Приготовьтесь к вкусному путешествию в прошлое с макаронами по-флотски! Это блюдо — 
настоящий морской волк, сытное и простое в приготовлении, как жизнь на корабле. Отборные 
макароны, обжаренные с сочным фаршем, создают дуэт, достойный шторма вкусов. Подавайте 
это блюдо с хрустящими огурчиками и ломтиком ржаного хлеба, и вы почувствуете себя 
настоящим моряком, покоряющим волны кулинарных наслаждений!''',
        "image": "pasta.jpg",
        "price": 100,
        "cooking_time": 20,
        "difficulty": 2,  # очень легко
        "route": "pasta.html"
    },
    {
        "title": "Картошечка",
        "description": '''Дамы и господа, приготовьтесь к картофельному параду! Жаренная картошка — это золотая 
середина кулинарного мира, блюдо, которое никогда не выходит из моды. Хрустящая корочка, 
нежный и воздушный центр — этот картофель покорит ваше сердце с первого укуса. Посыпьте его 
зеленью, добавьте соус по вкусу и наслаждайтесь каждой ложечкой этого картофельного 
блаженства!''',
        "image": "potato.jpg",
        "price": 70,
        "cooking_time": 25,
        "difficulty": 1,  # легко
        "route": "potato.html"
    },
    {
        "title": "Перловая каша",
        "description": '''Перловая каша — это не просто еда, это гимн сытости и пользе! Каждая жемчужинка перловки, 
сваренная до совершенства, тает во рту, наполняя вас энергией на весь день. Добавьте в кашу 
грибы, лук и морковь, и вы получите не просто завтрак, а настоящее произведение кулинарного 
искусства!''',
        "image": "perlovka.jpg",
        "price": 80,
        "cooking_time": 40,
        "difficulty": 3,  # средне
        "route": "perlovka.html"

    },
    {
        "title": "Омлет",
        "description": '''Омлет — это утренний маэстро кулинарии, который превращает обычные яйца в шедевр. 
Нежный, воздушный, с начинкой на любой вкус — омлет станет идеальным началом вашего дня. 
Добавьте сыр, ветчину, овощи или все, что подскажет вам ваша фантазия, и наслаждайтесь этим 
яичным облаком на тарелке!''',
        "image": "omlet.jpg",
        "price": 50,
        "cooking_time": 15,
        "difficulty": 2,  # средне
        "route": "omlet.html"
    },
    {
        "title": "Гречка с овощами",
        "description": '''Гречка с овощами — это симфония вкусов и пользы, которая перенесет вас в самое сердце 
русской кухни. Рассыпчатая гречка, обжаренная с сочными овощами, создает блюдо, которое 
согреет вас в холодный день и зарядит энергией на весь вечер. Подавайте гречку с квашеной 
капустой или солеными огурцами, и вы поймете, что счастье можно найти даже в простой тарелке 
каши''',
        "image": "buckwheat.jpg",
        "price": 90,
        "cooking_time": 30,
        "difficulty": 2,  # легко
        "route": "buckwheat.html"
    }
]


@app.route('/card_page/<title>')
def show_card_page(title):
    # Найдите рецепт по названию
    recipe = next((recipe for recipe in recipes if recipe['title'] == title), None)
    if recipe:
        return render_template(recipe['route'], recipe=recipe)
    else:
        return "Рецепт не найден"

        
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