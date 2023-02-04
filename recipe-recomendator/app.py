from chalice import Chalice
from service import search_by_ingredient, get_recipe_information, get_recipe_ingredients_measurment, get_recipe_cooking_time, convert_amounts, search_recipe_by_cuisine, search_by_nutrients, recipe_under_max_time

app = Chalice(app_name='recipe-recomendator')


@app.route('/search/ingredient/{ingredient}/{num_recipes}')
def search_by_ingredient_controller(ingredient, num_recipes):
    api_key = app.current_request.headers.get("x-api-key")

    return search_by_ingredient(api_key, ingredient, num_recipes)


@app.route('/recipe/info/{recipe_id}')
def get_recipe_information_controller(recipe_id):
    api_key = app.current_request.headers.get("x-api-key")

    return get_recipe_information(api_key, recipe_id)


@app.route('/ingredient/measurment/{recipe_id}')
def get_recipe_ingredients_measurment_controller(recipe_id):
    api_key = app.current_request.headers.get("x-api-key")

    return get_recipe_ingredients_measurment(api_key, recipe_id)


@app.route('/ingredient/convert/{ingredient_name}/{amount}/{source_unit}/{target_unit}')
def convert_amounts_controller(ingredient_name, amount, source_unit, target_unit):
    api_key = app.current_request.headers.get("x-api-key")

    return convert_amounts(api_key, ingredient_name, amount, source_unit, target_unit)


@app.route('/search/cuisine/{cuisine}/{num_recipes}')
def search_recipe_by_cuisine_controller(cuisine, num_recipes):
    api_key = app.current_request.headers.get("x-api-key")

    return search_recipe_by_cuisine(api_key, cuisine, num_recipes)


@app.route('/search/nutrient/{nutrients_list}')
def search_by_nutrients_controller(nutrients_list):
    api_key = app.current_request.headers.get("x-api-key")

    return search_by_nutrients(api_key, nutrients_list)


@app.route('/maxtime/{max_time}')
def recipe_under_max_time_controller(max_time):
    api_key = app.current_request.headers.get("x-api-key")

    return recipe_under_max_time(api_key, max_time)
