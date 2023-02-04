import json
from unicodedata import name
from charset_normalizer import api
import requests
import os


def search_by_ingredient(api_key, ingredient, num_recipes):
    url = "https://api.spoonacular.com/recipes/findByIngredients"
    key = f"?apiKey={api_key}"
    # coma separated. ex. apple,sugar,cinnamon
    ingredients = f"&ingredients={ingredient}"
    number = f"&number={num_recipes}"
    complete_url = url + key + ingredients + number

    response = requests.get(complete_url)
    json_response = response.json()

    recipe_list_by_ingredients = []  # id and title of recipe

    for item in json_response:
        recipe = {"id": item["id"], "title": item["title"]}

        recipe_list_by_ingredients.append(recipe)

    # returns a list of dictionaries with the recipe 'title' and 'id'
    return json.dumps(recipe_list_by_ingredients, indent=4)


def get_recipe_information(api_key, recipe_id):
    url = "https://api.spoonacular.com/recipes/{id}/information".format(
        id=recipe_id)
    key = f"?apiKey={api_key}"

    complete_url = url + key
    response = requests.get(complete_url)
    json_response = response.json()
    json_formated = json.dumps(json_response, indent=4)

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
                "Item": item_name,
                "Measurement": measurement_amount,
                "Measurement Unit": measurement_unitShort
            }
        )
    # returns a list of dictionaries containing the measurement of the 'recipe_id' ingredients
    return recipe_measurment_information


def get_recipe_cooking_time(recipe_id):
    get_recipe_informations = get_recipe_information(recipe_id)
    ready_in = get_recipe_informations["readyInMinutes"]

    # returns the time it takes a recipe to be ready
    return ready_in


def convert_amounts(api_key, ingredient_name, amount, source_unit, target_unit):
    url = "https://api.spoonacular.com/recipes/convert"
    key = f"?apiKey={api_key}"
    ingredient_name = f"&ingredientName={ingredient_name}"
    amount = f"&sourceAmount={amount}"
    source_unit = f"&sourceUnit={source_unit}"
    target_unit = f"&targetUnit={target_unit}"

    complete_url = url + key + ingredient_name + amount + source_unit + target_unit
    response = requests.get(complete_url)
    json_response = response.json()
    json_formated = json.dumps(json_response, indent=4)

    # converts amounts to the specified measuring metric
    answer = json_response["answer"]
    return answer


def search_recipe_by_cuisine(api_key, cuisine, num_recipes):
    url = "https://api.spoonacular.com/recipes/complexSearch"
    key = f"?apiKey={api_key}"
    cuisine = f"&cuisine={cuisine}"
    number_recipes = f"&number={num_recipes}"

    complete_url = url + key + cuisine + number_recipes
    response = requests.get(complete_url)
    json_response = response.json()
    json_formated = json.dumps(json_response, indent=4)

    recipe_cusine_list = []
    for recipe in json_response["results"]:
        title = recipe["title"]
        recipe_cusine_list.append(title)

    # returns a list of recipes by "cusine" and "number" of recipes wanted"
    return recipe_cusine_list


def search_by_nutrients(api_key, nutrients_list):
    url = "https://api.spoonacular.com/recipes/findByNutrients"
    key = f"?apiKey={api_key}"

    # Searches recipes by specific nutrients
    complete_url = url + key + "&" + nutrients_list
    response = requests.get(complete_url)
    json_response = response.json()
    json_formated = json.dumps(json_response, indent=4)

    id_title_kal_prot_fat_carb_list = []
    for recipe in json_response:
        id = recipe["id"]
        title = recipe["title"]
        calories = recipe["calories"]
        protein = recipe["protein"]
        fat = recipe["fat"]
        carbs = recipe["carbs"]

        id_title_kal_prot_fat_carb_list.append(
            {
                "id: " + str(id),
                "title: " + title,
                "calories: " + str(calories),
                "protein: " + str(protein),
                "fat: " + str(fat),
                "carbs: " + str(carbs),
            }
        )

    # returns a list of of dictionaries with the nutrients of the recipe
    return id_title_kal_prot_fat_carb_list


def recipe_under_max_time(api_key, max_time):

    print("")
    print("")
    print("hello")
    print(api_key)
    print("")

    url = "https://api.spoonacular.com/recipes/complexSearch"
    key = f"?apiKey={api_key}"
    max_time = f"&maxReadyTime={max_time}"
    complete_url = url + key + max_time

    response = requests.get(complete_url)
    json_response = response.json()
    json_formated = json.dumps(json_response, indent=4)

    id_list = []
    for recipe in json_response["results"]:
        recipe_id = recipe["id"]
        information = get_recipe_information(recipe_id)
        title = information["title"]
        id_list.append(

            recipe_id,

        )
    # returns a list of recipesids under specified argument
    return id_list
