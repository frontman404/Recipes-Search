import requests
import functions

url1 = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search"

querystring = functions.ask_user()

headers = {
    "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    "X-RapidAPI-Key": "YOUR KEY HERE"
}

recipe_list = requests.request("GET", url1, headers=headers, params=querystring)
recipe_list_usable = recipe_list.json()
check = functions.print_recipes_list(recipe_list_usable)

if not check:
    print('No recipes found')
else:

    id_of_choice = functions.choose_recipe(recipe_list_usable)

    url2 = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/"+str(id_of_choice)+"/information"

    recipe_information = requests.request("GET", url2, headers=headers)
    recipe_information_usable = recipe_information.json()
    functions.print_information(recipe_information_usable)

    answer = functions.ask_about_substitute()
    while answer == 'yes':
        url3 = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/ingredients/substitutes"
        ingredient = functions.ask_substitute()
        substitute_query = {"ingredientName": ingredient}
        substitute = requests.request("GET", url3, headers=headers, params=substitute_query)
        substitute_usable = substitute.json()
        check = functions.print_substitute_options(substitute_usable)
        if check is False:
            print("There's no substitute for that ingredient")
        answer = functions.ask_about_substitute()

