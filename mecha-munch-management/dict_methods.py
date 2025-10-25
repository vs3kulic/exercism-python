"""This module contains dictionary manipulation methods for Mecha Munch."""

def add_item(current_cart: dict, items_to_add: list[str]) -> dict:
    """Add items to shopping cart.
    
    :param current: the current shopping cart dict.
    :type current: dict
    :param items_to_add: iterable of items to add to cart.
    :type items_to_add: list[str]
    :return: updated shopping cart dictionary.
    """
    # Copy the current cart
    updated_cart = current_cart.copy()

    # Modify the cart by adding items
    for item in items_to_add:
        updated_cart[item] = updated_cart.setdefault(item, 0) + 1

    return updated_cart

def read_notes(notes: list[str]) -> dict:
    """Create the user cart from their notes.

    :param notes: the user notes listing items to add to cart.
    :type notes: list[str]
    :return: the resulting shopping cart.
    :rtype: dict
    """
    # Create a new cart dictionary
    new_cart = {}

    # Populate the cart based on the notes
    for item in notes:
        new_cart[item] = new_cart.setdefault(item, 0) + 1

    return new_cart

def update_recipes(ideas: dict, recipe_updates: dict) -> dict:
    """Update the recipe ideas dictionary.

    :param ideas: current recipe ideas, with str keys and list[str] values.
    :type ideas: dict
    :param recipe_updates: updates to apply to the recipe ideas; may be a dict
        or a tuple of (key, value) tuples as provided by some test data.
    :type recipe_updates: dict | tuple[tuple[str, list[str]], ...]
    :return: updated recipe ideas.
    :rtype: dict
    """
    # Copy the current ideas
    new_ideas = ideas.copy()

    # Convert recipe_updates to a dict (shallow copy - to accommodate test data)
    recipe_updates_dict = dict(recipe_updates)

    # Update the ideas with the recipe updates
    for key, value in recipe_updates_dict.items():
        new_ideas[key] = value

    return new_ideas

def sort_entries(cart: dict) -> dict:
    """Sort a users shopping cart in alphabetically order.

    :param cart: users shopping cart.
    :type cart: dict
    :return: sorted shopping cart.
    :rtype: dict
    """
    # Create an empty dictionary
    sorted_cart = {}

    # Iterate over the keys in the cart and sort them
    for key in sorted(cart):
        sorted_cart[key] = cart[key]

    return sorted_cart

def send_to_store(cart: dict, isle_mapping: dict) -> dict:
    """Combine users cart with isle and refrigeration information.
 
    :param cart: users shopping cart with item names as keys and quantities as values.
        Example: {'apple': 5, 'banana': 3}
    :type cart: dict[str, int]
    :param isle_mapping: isle and refrigeration info.
        Example: {'apple': ['Aisle 1', False]}
    :type isle_mapping: dict[str, list[str, bool]]
    :return: fulfillment dictionary.
        Example: {'apple': [5, 'Aisle 1', False]}
    :rtype: dict[str, list[int, str, bool]]
    """
    # Create an empty fulfillment dictionary
    fulfill_cart = {}

    # Iterate over the cart and concatenate values with the isle mapping
    for key in sorted(cart, reverse = True):
        fulfill_cart[key] = [cart[key]] + isle_mapping[key]

    return fulfill_cart


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment_cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    # Create a copy of the store inventory
    update_inventory = store_inventory.copy()

    # Iterate over the fulfillment cart and update the inventory
    for key, values in fulfillment_cart.items():
        update_inventory[key][0] -= values[0]

    # Check if the inventory level is zero or below and update accordingly
        if update_inventory[key][0] <= 0:
            update_inventory[key][0] = "Out of Stock"

    return update_inventory


def main():
    """Main function to demonstrate dictionary methods."""
    # Demonstrate recipe update
    ideas = {'salad': ['lettuce', 'tomato'], 'sandwich': ['bread', 'ham']}
    recipe_updates = (
        ('salad', ['lettuce', 'tomato', 'cucumber']),
        ('sandwich', ['bread', 'turkey'])
    )
    updated_ideas = update_recipes(ideas, recipe_updates)
    print(f"Updated Recipe Ideas: {updated_ideas}")
    
    # Demonstrate sending to store
    cart = {"apple": 5, "steak": 3}
    isle_mapping = {
        "apple": ["Aisle 1", False],
        "steak": ["Aisle 3", True]
    }
    fulfillment_cart = send_to_store(cart, isle_mapping)
    print(f"Fulfillment cart: {fulfillment_cart}")
    
    # Demonstrate updating store inventory
    fulfill_cart = {
        "apple": [5, "Aisle 1", False],
        "steak": [3, "Aisle 3", True]
    }
    store_inventory = {
        "apple": [10, "Aisle 1", False],
        "steak": [2, "Aisle 3", True],
    }
    updated_inventory = update_store_inventory(fulfill_cart, store_inventory)
    print(f"Updated Store Inventory: {updated_inventory}")

if __name__ == "__main__":
    main()
