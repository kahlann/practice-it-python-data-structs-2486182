import collections

def main():
    #add code here
    # Instantiate an empty deque with maximum lenth 5
    prev_orders = collections.deque([], 5)

    # Order some food
    prev_orders.extend(["Starter 1", "Main 1", "Dessert 1"])
    print("After first order:")
    print(prev_orders)

    # Order some more food
    prev_orders.append("Set Meal 2")
    print("After second order:")
    print(prev_orders)

    # Order some more food
    prev_orders.extend(["Starter 3", "Main 3", "Dessert 3"])
    print("After second order:")
    print(prev_orders)

    return

if __name__ == "__main__":
    main()