"""Functions for compiling dishes and ingredients for a catering company."""

from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)

def clean_ingredients(dish_name, dish_ingredients):
    """Remove duplicates from `dish_ingredients`.

    :param dish_name: str - containing the dish name.
    :param dish_ingredients: list - dish ingredients.
    :return: tuple - containing (dish_name, ingredient set).

    This function should return a `tuple` with the name of the dish as the first item,
    followed by the de-duped `set` of ingredients as the second item.
    """
    unique_ingredients = set(dish_ingredients)

    return dish_name, unique_ingredients

def check_drinks(drink_name, drink_ingredients):
    """Append "Cocktail" (alcohol)  or "Mocktail" (no alcohol) to `drink_name`, based on `drink_ingredients`.

    :param drink_name: str - name of the drink.
    :param drink_ingredients: list - ingredients in the drink.
    :return: str - drink_name appended with "Mocktail" or "Cocktail".

    The function should return the name of the drink followed by "Mocktail" (non-alcoholic) and drink
    name followed by "Cocktail" (includes alcohol).

    """
    drink_name = drink_name.strip()

    if set(drink_ingredients).intersection(ALCOHOLS):
        return f"{drink_name} Cocktail"
    else:
        return f"{drink_name} Mocktail"

def categorize_dish(dish_name, dish_ingredients):
    """Categorize `dish_name` based on `dish_ingredients`.

    :param dish_name: str - dish to be categorized.
    :param dish_ingredients: set - ingredients for the dish.
    :return: str - the dish name appended with ": <CATEGORY>".

    This function should return a string with the `dish name: <CATEGORY>` (which meal category the dish belongs to).
    `<CATEGORY>` can be any one of  (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).
    All dishes will "fit" into one of the categories imported from `sets_categories_data.py`
    """
    dish_name = dish_name.strip()
    dish_ingredients = set(dish_ingredients)

    categories = {
        "VEGAN": VEGAN,
        "VEGETARIAN": VEGETARIAN, 
        "PALEO": PALEO,
        "KETO": KETO,
        "OMNIVORE": OMNIVORE
    }
    
    for category_name, category_set in categories.items():
        if dish_ingredients.issubset(category_set):
            return f"{dish_name}: {category_name}"
            
    raise ValueError(f"Dish '{dish_name}' does not fit into any category.")

def tag_special_ingredients(dish):
    """Compare `dish` ingredients to `SPECIAL_INGREDIENTS`.

    :param dish: tuple - of (dish name, list of dish ingredients).
    :return: tuple - containing (dish name, dish special ingredients).

    Return the dish name followed by the `set` of ingredients that require a special note on the dish description.
    For the purposes of this exercise, all allergens or special ingredients that need to be tracked are in the
    SPECIAL_INGREDIENTS constant imported from `sets_categories_data.py`.
    """
    dish_name, dish_ingredients = dish # unpack the tuple into dish_name and dish_ingredients
    dish_name = dish_name.strip()
    dish_ingredients = set(dish_ingredients)

    special_ingredients = dish_ingredients.intersection(SPECIAL_INGREDIENTS)
    return dish_name, special_ingredients

def compile_ingredients(dishes):
    """Create a master list of ingredients.

    :param dishes: list - of dish ingredient sets.
    :return: set - of ingredients compiled from `dishes`.

    This function should return a `set` of all ingredients from all listed dishes.
    """
    master_ingredients = set()

    for dish in dishes:
        dish_ingredients = dish # unpack the tuple into dish_ingredients
        master_ingredients.update(dish_ingredients)

    return master_ingredients

def separate_appetizers(dishes, appetizers):
    """Determine which `dishes` are designated `appetizers` and remove them.

    :param dishes: list - of dish names.
    :param appetizers: list - of appetizer names.
    :return: list - of dish names that do not appear on appetizer list.

    The function should return the list of dish names with appetizer names removed.
    Either list could contain duplicates and may require de-duping.
    """
    dishes = set(dishes)
    appetizers = set(appetizers)

    # Remove duplicates from dishes
    non_appetizer_dishes = list(dishes - appetizers)

    return non_appetizer_dishes

def singleton_ingredients(dishes, intersection):
    """Determine which `dishes` have a singleton ingredient (an ingredient that only appears once across dishes).

    :param dishes: list - of ingredient sets.
    :param intersection: constant - can be one of `<CATEGORY>_INTERSECTIONS` constants imported from `sets_categories_data.py`.
    :return: set - containing singleton ingredients.

    Each dish is represented by a `set` of its ingredients.

    Each `<CATEGORY>_INTERSECTIONS` is an `intersection` of all dishes in the category. `<CATEGORY>` can be any one of:
        (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).

    The function should return a `set` of ingredients that only appear in a single dish.
    """
    # Create a set with all ingredients from all dishes
    all_ingredients = set()
    
    for dish in dishes:
        all_ingredients.update(dish)
    
    # Find the singleton ingredients (appear exactly once)
    singletons = set()

    for ingredient in all_ingredients:
        # Count in how many dishes this ingredient appears
        count = sum(1 for dish in dishes if ingredient in dish)
        if count == 1:
            singletons.add(ingredient)
    
    # Remove any common ingredients that appear in all dishes
    singletons = singletons - intersection
    
    return singletons
