from collections import namedtuple, defaultdict
from pprint import pprint
import csv

# Function to count the number of sold items
def CountItems(csv_file):
    # Dictionary where the default is an integer
    order_count = defaultdict(int)

    # Read in the csv data
    with open(csv_file, "r") as f:
        # Read the csv file
        reader = csv.reader(f)
        # Get the column names from the first row
        for n, row in enumerate(reader):
            if n == 0:
                Order = namedtuple("Order", row)
            # For all other rows, add the number of items to the dictionary
            else:
                # row is a list object. * does argument unpacking (i.e. feeds in the strings one at a time rather than as a list)
                this_order = Order(*row)
                # Add the number of items sold to that entry in the dictionary
                order_count[this_order.ProductID] += int(this_order.Quantity)
        return order_count

def main():
    pprint(CountItems('data/OrderItems.csv'))

    return

if __name__ == "__main__":
    main()