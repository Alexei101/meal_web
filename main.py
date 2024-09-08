

import requests


if __name__ == '__main__':
    response = requests.get("https://www.themealdb.com/api/json/v1/1/random.php")
    ans = response.json()
    recipe_instructions = ans['meals'][0]['strInstructions']
    label = ans['meals'][0]['strMeal']
    print(label)
    print(recipe_instructions)
