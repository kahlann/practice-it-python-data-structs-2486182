from collections import namedtuple
import csv

def getCustomer(csv_file):
    # Get the column names from the csv file
    with open(csv_file, newline='') as f:
        # Read the csv file
        reader = csv.reader(f)
        # Get the column names from the first row
        for n, row in enumerate(reader):
            if n == 0:
                Customer = namedtuple("Customer", row)
            # For all other rows, instantiate the customer namedtuple and print dome details
            else:
                # row is a list object. * does argument unpacking (i.e. feeds in the strings one at a time rather than as a list)
                this_customer = Customer(*row)
                print(f"ID: {this_customer.CustomerID}")
                print(f"Name: {this_customer.FirstName} {this_customer.LastName}\n")
    
def main():
    #add code here
    #print the customer ID and name for each customer in the csv file
    getCustomer('data/Customer.csv')

    return

if __name__ == "__main__":
    main()