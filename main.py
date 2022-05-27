def make_cookbook():
    with open('recipes.txt', encoding='utf-8') as file:
        cook_book = {}
        for block in file.read().split('\n\n'):
            name, _, *ingredient = block.split('\n')
            structure = []
            for ing in ingredient:
                ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, ing.split(' | '))
                structure.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            cook_book[name] = structure
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    ingredient_dict = {}
    for dish in dishes:
        for ingredient in make_cookbook()[dish]:
            ingredient['quantity'] *= person_count
            if ingredient['ingredient_name'] not in ingredient_dict:
                ingredient_dict[ingredient['ingredient_name']] = ingredient
                del ingredient['ingredient_name']
            else:
                ingredient_dict[ingredient['ingredient_name']]['quantity'] += ingredient['quantity']
    return ingredient_dict



