import csv
import ast

class Recipe:
    def __init__(self, name, ingredients, liters, notes):
        self.name = name
        self.ingredients = ingredients
        self.liters = liters
        self.notes = notes
    def __str__(self):
        return self.name

    def print_recipe(self):
        print(f"Recipe: {self.name}")
        print(f"Notes: {self.notes}")
        print(f"Liters: {self.liters}")
        print("Ingredients:")
        for produce_item, quantity in self.ingredients.items():
            print(f"  {produce_item}: {quantity} units")


def line():
    print('\n ---- ---- ----\n')


def read_recipes_from_csv(file_path):
    recipes = []
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            name = row['name']
            ingredients = ast.literal_eval(row['ingredients'])
            liters = float(row['liters'])
            notes = row['notes']
            recipes.append(Recipe(name, ingredients, liters, notes))
    return recipes

def generate_shopping_list(user_recipes):
    shopping_list = {}
    recipe_list = []

    while True:
        print("\nSelect a recipe by entering its corresponding number:\n")

        for idx, recipe in enumerate(user_recipes, start=1):
            print(f"{idx}. {recipe.name}, - {recipe.notes}")
        line()
        if recipe_list:
            print("Current Selected Recipes: ", end = '')
            for i in recipe_list: print(i, end = ', ')
            print('\n')

        entry = input("Enter help to see all recipe detials. \nEnter number or press return to enter quantites: ")
        if entry == '':
            break
        elif entry.upper() =='HELP':
            list_recipes(user_recipes)
            input('\nPress return')
            continue

        selected_recipe_idx = int(entry) - 1
        selected_recipe = user_recipes[selected_recipe_idx]
        recipe_list.append(selected_recipe)


    for selected_recipe in recipe_list:
        selected_liters = float(input(f"How many liters of {selected_recipe.name} do you want to make? "))
        for produce_item, quantity in selected_recipe.ingredients.items():
            if produce_item in shopping_list:
                selected_recipe.ingredients[produce_item] += quantity * selected_liters
                shopping_list[produce_item] += selected_recipe.ingredients[produce_item]
                
            else:
                shopping_list[produce_item] = quantity * selected_liters
                selected_recipe.ingredients[produce_item] = quantity * selected_liters

        selected_recipe.liters = selected_liters

    return recipe_list,  shopping_list


def display_shopping_list(shopping_list):
    print("\nShopping List:")
    for item, quantity in shopping_list.items():
        print(f"  {item}: {quantity:.2f}")


def list_recipes(recipe_list):
    for i in recipe_list:
        line()
        i.print_recipe()

# Read recipes from CSV file
csv_file_path = 'recipes.csv'
user_recipes = read_recipes_from_csv(csv_file_path)


'''
# Choose recipes to make
selected_recipes = []
print("\nSelect the recipes you want to make (Enter recipe numbers, separate by commas):")
for idx, recipe in enumerate(user_recipes, start=1):
    print(f"{idx}. {recipe.name}")
selected_recipe_indices = [int(i) - 1 for i in input().split(", ")]
for idx in selected_recipe_indices:
    selected_recipes.append(user_recipes[idx])
'''

# Generate and display shopping list
recipe_list, shopping_list = generate_shopping_list(user_recipes)
list_recipes(recipe_list)
display_shopping_list(shopping_list)
print()





