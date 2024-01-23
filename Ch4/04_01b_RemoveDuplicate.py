from collections import namedtuple, defaultdict
from pprint import pprint
  
# Function to return a default 
# value for keys that are not 
# present 
def MenuDict(menu_list):
    # Dictionary where the default is a set
    menu = defaultdict(lambda: set())
    # Iterate over each item in the list, and categorise as starter, salad, entree, or dessert
    for item in menu_list:
        # Starters
        if item.identifier[0:3] == "STA":
                menu["starter"].add(item)
        # Beverages
        elif item.identifier[0:3] == "BEV":
                menu["beverage"].add(item)
        # Salads
        elif item.identifier[0:3] == "SAL":
            menu["salad"].add(item)
        # Entrees
        elif item.identifier[0:3] == "ENT":
                menu["entree"].add(item)
        # Desserts
        elif item.identifier[0:3] == "DES":
                menu["dessert"].add(item)
    # Return the menu dictionary
    return menu


def main():
    # Named tuple template
    Food = namedtuple("Food", ["identifier", "name"])
    
    # List of items
    nadias_list = [
        Food("STA001",  "Panko Stuffed Mushrooms"),
        Food("BEV003",	"Cafe Latte"),
        Food("STA002",	"Mini Cheeseburgers"),
        Food("STA003",	"French Onion Soup"),
        Food("STA004",	"Artichokes with Garlic Aioli"),
        Food("STA005",	"Parmesan Deviled Eggs"),
        Food("SAL001",	"Garden Buffet"),
        Food("SAL002",	"House Salad"),
        Food("SAL003",	"Chefs Salad"),
        Food("SAL004",	"Quinoa Salmon Salad"),
        Food("ENT001",	"Classic Burger"),
        Food("ENT002",	"Tomato Bruschetta Tortellini"),
        Food("ENT003",	"Handcrafted Pizza"),
        Food("ENT004",	"Barbecued Tofu Skewers"),
        Food("ENT005",	"Fiesta Family Platter"),
        Food("DES001",	"Creme Brulee"),
        Food("ENT001",	"Classic Burger"),
        Food("DES002",	"Cheesecake"),
        Food("DES003",	"Chocolate Chip Brownie"),
        Food("DES004",	"Apple Pie"),
        Food("STA001",	"Panko Stuffed Mushrooms"),
        Food("DES005",	"Mixed Berry Tart"),
        Food("DES005",	"Mixed Berry Tart"),
        Food("BEV001",	"Tropical Blue Smoothie"),
        Food("BEV002",	"Pomegranate Iced Tea"),
        Food("DES005",	"Mixed Berry Tart"),
        Food("BEV003",	"Cafe Latte"),
        Food("DES005",	"Mixed Berry Tart"),
        Food("BEV003",	"Cafe Latte"),
    ]

    # Sort the food into dictionary, removing duplicates
    pprint(MenuDict(nadias_list))


if __name__ == "__main__":
    main()