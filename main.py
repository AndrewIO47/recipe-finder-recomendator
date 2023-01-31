import json
import requests

api_key = ""

"https://api.spoonacular.com/recipes/findByIngredients?apiKey=6c0f13faf52043bab2dce46f705660ee&query=apple"

# returns a list of dictionaries with the recipe 'title' and 'id'


def search_by_ingredient(api_key, ingredient, num_recipes):
    url = "https://api.spoonacular.com/recipes/findByIngredients"
    key = f"?apiKey={api_key}"
    # coma separated. ex. apple,sugar,cinnamon
    ingredients = f"&ingredients={ingredient}"
    number = f"&number={num_recipes}"
    complete_url = url + key + ingredients + number

    response = requests.get(complete_url)
    json_response = response.json()
    json_formated = json.dumps(json_response, indent=4)

    recipe_list_by_ingredients = []  # id and title of recipe
    for item in json_response:

        recipe_list_by_ingredients.append(
            {
                "id: " + str(item["id"]),
                "title: " + item["title"]
            })
    # print(recipe_list_by_ingredients)
    return (recipe_list_by_ingredients)


