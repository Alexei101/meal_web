
from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def get_recipe():
    response = requests.get("https://www.themealdb.com/api/json/v1/1/random.php")
    ans = response.json()
    recipe_instructions = ans['meals'][0]['strInstructions']
    label = ans['meals'][0]['strMeal']
    return f'<h1>{label}</h1><p>{recipe_instructions}</p>'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5080)  # Запуск приложения
