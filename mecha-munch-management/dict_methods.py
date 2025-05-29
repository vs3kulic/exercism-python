"""Functions to manage a users shopping cart items."""

def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    # Create a copy of the current cart to avoid side effects
    updated_cart = current_cart.copy()
    
    # Iterate over the items to add and update the cart
    for item in items_to_add:
        if item in updated_cart:
            updated_cart[item] += 1
        else:
            updated_cart[item] = 1
    
    return updated_cart

def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    # Create a new cart dictionary
    cart = {}
    
    # Iterate over the notes and add items to the cart
    for item in notes:
        if item in cart:
            cart[item] += 1
        else:
            cart[item] = 1

    return cart

def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict or iterable - updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    # Create a copy of the ideas dictionary to avoid side effects
    new_ideas = ideas.copy()
    
    # Ensure new_ideas and recipe_updates are dictionaries or convert them
    try:
        new_ideas = dict(new_ideas)
        recipe_updates = dict(recipe_updates)
    except (TypeError, ValueError) as exc:
        raise TypeError("Both 'ideas' and 'recipe_updates' must be dictionaries or convertible to dictionaries.") from exc
    
    # Iterate over the recipe updates and replace the values in new_ideas
    for key, value in recipe_updates.items():
        new_ideas[key] = value  # Replace the entire recipe with the updated one
    
    return new_ideas

def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    # Create an empty dictionary to hold the sorted cart
    sorted_cart = {}

    # Iterate over the keys in the cart and sort them
    for key in sorted(cart):
        sorted_cart[key] = cart[key]

    return sorted_cart

def send_to_store(cart, isle_mapping):
    """Combine users order to isle and refrigeration information.
 
    :param cart: dict - users shopping cart dictionary.
    :param isle_mapping: dict - isle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    # Create an empty fulfillment dictionary
    fulfillment = {}

    # Iterate over the cart and combine it with the isle mapping
    for key in cart.keys():
        fulfillment[key] = [cart[key]] + isle_mapping[key]

    return dict(sorted(fulfillment.items(), reverse=True))


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment_cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    # Create a copy of the store inventory to avoid side effects
    updated_inventory = store_inventory.copy()

    # Iterate over the fulfillment cart and update the inventory
    for key, values in fulfillment_cart.items():
        updated_inventory[key][0] = updated_inventory[key][0] - values[0]

    # Check if the inventory level is zero or below and update accordingly
        if updated_inventory[key][0] <= 0:
            updated_inventory[key][0] = "Out of Stock"

    return updated_inventory
