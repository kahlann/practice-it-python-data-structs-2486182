from collections import namedtuple

# Named tuple template: Driver, Vehicle, capacity
Driver = namedtuple('Driver', ['Name', 'Vehicle', 'Capacity'])

# Function to check if a driver can take the order
def canCarryOrder(driver, n_items):
    if driver.Capacity >= n_items:
        print(f"{driver.Name} ({driver.Vehicle}) can take this order ({n_items} items)")
        return True
    else:
        print(f"{driver.Name} ({driver.Vehicle}) cannot take this order ({n_items} items)")
        return False

def main():
    #add code here
    #create a driver with a name, car type, and car capacity
    #an example you can use to practice: "Iris", "Toyota Prius", 7
    #check if they can take a certain order, given their car's capacity.

    # Make a few drivers
    iris = Driver("Iris", "Toyota Prius", 10)
    jake = Driver("Jake", "VW Polo", 7)

    # Test whether they can take an order of a given size
    canCarryOrder(jake, 10)
    canCarryOrder(iris, 10)

    return

if __name__ == "__main__":
    main()