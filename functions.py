def ask_user():
    querystring = {'query': input('What dish are you looking for? (example: "burger")\n'),
                   'number': int(input('How many results do you want to receive? (between 0 and 100)\n')),
                   'offset': int(input('You want to skip a number of results? (between 0 and 900)\n'))}
    print('\nThe following questions do not require an answer, press Enter if you want to skip\n')
    querystring['diet'] = input(
        'Are you following a specific diet?\nChoose one or none from: pescetarian, lacto vegetarian, ovo vegetarian, '
        'vegan, vegetarian\n').replace(' ', '')
    querystring['excludeIngredients'] = input("Any ingredients you don't want to have in your recipe? \n"
                                              "Separate them with a comma\n").replace(' ', '')
    querystring['intolerances'] = input('Any intolerances?\nChoose none, one or more from: dairy, egg, gluten, peanut,'
                                        ' sesame, seafood, shellfish, soy, sulfite, tree nut, wheat\n').replace(' ', '')
    querystring['type'] = input('What type of recipe? \nChoose one or none from: main course, side dish, dessert, '
                                'appetizer, salad, bread, breakfast, soup, beverage, sauce, drink\n').replace(' ', '')
    querystring['cuisine'] = input('What cuisine shall the recipe belong to?\nChoose none, one or more from: african, '
                                   'chinese, japanese, korean, vietnamese, thai, indian, british, irish, french, '
                                   'italian, mexican,\n spanish, middle eastern, jewish, american, cajun, southern, '
                                   'greek, german, nordic, eastern european, caribbean, '
                                   'or latin american\n').replace(' ', '')
    return querystring


def choose_recipe(param):
    choice = int(input('Which recipe would you like to receive information about?\nType the number of the recipe'
                       ' (1 is first, 2 is second, etc.)\n'))
    return param['results'][choice - 1]['id']


def print_recipes_list(param):
    if param['results'] is None:
        return False
    for item in param['results']:
        print('Title of the recipe: ' + item['title'])
        print('Ready in ' + str(item['readyInMinutes']) + ' mins')
        print('Number of servings: ' + str(item['servings']))
        print('\n', end='')
    return True


def print_information(param):
    print('\n', end='')
    print('Preparation time ' + str(param['preparationMinutes']) + ' mins')
    print('Cooking time ' + str(param['cookingMinutes']) + ' mins')
    print('Ingredients are:')
    for item in param['extendedIngredients']:
        print('* ', end=' ')
        print(str(item['measures']['us']['amount']) + ' ' + str(
            item['measures']['us']['unitShort']), end=' ')
        print(item['name'], end=' ')
        if len(item['meta']) > 0:
            print('(', end='')
            for i in range(len(item['meta']) - 1):
                print(item['meta'][i], end=', ')
            print(item['meta'][len(item['meta']) - 1], end='')
            print(')')
        else:
            print('')
    print('\nStep to follow:')
    print(param['instructions'])


def ask_about_substitute():
    a = input("\nDo you want to find a substitute for a certain ingredient? \nAnswer with yes if it's the case"
              " or with no if not\n")
    a = a.replace(' ', '')
    a = a.lower()
    return a


def ask_substitute():
    product = input('What product would you like to substitute? (only one)\n')
    product = product.replace(' ', '').lower()
    return product


def print_substitute_options(param):
    if param['status'] == 'success':
        for item in param['substitutes']:
            print('* ', end='')
            print(item, end='\n')
    else:
        return False
