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


def get_recipe_information(api_key, recipe_id):
    url = "https://api.spoonacular.com/recipes/{id}/information".format(
        id=recipe_id)
    key = f"?apiKey={api_key}"

    complete_url = url + key
    response = requests.get(complete_url)
    json_response = response.json()
    json_formated = json.dumps(json_response, indent=4)
    # print(json_formated)

    #  returns a json response with the recipe information
    return json_response


def get_recipe_ingredients_measurment(api_key, recipe_id):
    url = "https://api.spoonacular.com/recipes/{id}/information".format(
        id=recipe_id)
    key = f"?apiKey={api_key}"

    complete_url = url + key
    response = requests.get(complete_url)
    json_response = response.json()
    json_formated = json.dumps(json_response, indent=4)

    recipe_measurment_information = []
    for item in json_response["extendedIngredients"]:

        item_name = item["nameClean"]
        measurement = item["measures"]["metric"]
        measurement_amount = measurement["amount"]
        measurement_unitShort = measurement["unitShort"]

        recipe_measurment_information.append(
            {
                "Item: " + item_name,
                "Measurement: " + str(measurement_amount) +
                " " + measurement_unitShort
            })
    # print(recipe_measurment_information)
    # returns a list of dictionaries containing the measurement of the 'recipe_id' ingredients
    return recipe_measurment_information

# returns the time it takes a recipe to be ready


def get_recipe_cooking_time(api_key, recipe_id):

    get_recipe_informations = get_recipe_information(api_key, recipe_id)
    ready_in = get_recipe_informations["readyInMinutes"]

    # print("Ready in: " + str(ready_in) + " minutes")
    # returns the time it takes a recipe to be ready
    return ready_in


# search_by_ingredient(api_key, "apple,sugar,cinnamon", 4)
# get_recipe_information(api_key, 660261)
# get_recipe_ingredients_measurment(api_key, 660261)
get_recipe_cooking_time(api_key, 660261)
