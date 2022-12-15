# ------------------------------------------------------------------------ #
# Title: Assignment 08 - Final
# Description: Working with classes
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# JShin,12.14.2022,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Declare variables and constants
file_name_str = 'products.txt'  # The name of the data file
row_of_object = {}    # A row of data separated into elements of a dictionary {Name,Price}
list_of_objects = []    # A list that acts as a 'table' of rows
choice_str = ""  # Captures the user option selection
name_str = ""   # Captures the name input from functions to be processed in main body
price_flt = 0.0 # Captures the price input from functions to be processed in main body


# Data -------------------------------------------------------------------- #
class Product:
    """Stores data about a product:
    properties:
        product_name: (string) with the product's  name
        product_price: (float) with the product's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        JShin,12.14.2022,Modified code to complete assignment 8
    """

    # -- Constructor --
    def __init__(self, product_name: str, product_price: float):
        self.product_name = product_name
        self.product_price = product_price

    # -- Properties --
    @property
    def product_name(self):     # Getter
        return str(self.__product_name).title()

    @product_name.setter
    def product_name(self, value):    # Setter
        if str(value).isnumeric() == False:     # Checks for errors in name input
            self.__product_name = value
        else:
            raise Exception("Names cannot be numbers")

    @property
    def product_price(self):    # Getter
        return float(self.__product_price)

    @product_price.setter
    def product_price(self, value):     # Setter
        if str(value).isalpha() == False:   # Checks for errors in price input
            self.__product_price = value
        else:
            raise Exception("Prices cannot be letters")

    # -- Methods --
    def to_string(self):
        """  Returns object data in a comma separated string of values
        :return: (string) CSV data
        """
        product_data_csv = self.product_name + ',' + str(self.product_price)
        return product_data_csv

    def __str__(self):
        """  Overrides Python's built-in method to
             return object data in a comma separated string of values
        :return: (string) CSV data
        """
        return self.to_string()
# --End of class--
# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:
    methods:
        save_data_to_file(file_name, list_of_objects):
        read_data_from_file(file_name): -> (a list of objects)
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        JShin,12.14.2022,Modified code to complete assignment 8
    """

    # -- Methods --
    @staticmethod
    def save_data_to_file(file_name: str, list_of_rows: list):
        """ Write data to a file from a list of object rows
        :param file_name: (string) with name of file
        :param list_of_rows: (list) of objects data saved to file
        :return: (bool) with status of success status
        """
        success_status = False
        try:
            file = open(file_name, "w")     # Open file with wb mode; w for write
            for row in list_of_rows:
                file.write(row["Task"] + "," + row["Priority"] + "\n")
            file.close()
            success_status = True
        except Exception as e:      # Checks for file access errors
            print("There was a general error!")
            print(e, e.__doc__, type(e), sep='\n')
        return success_status

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of object rows
        :param file_name: (string) with name of file
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of object rows
        """
        list_of_rows.clear()
        try:
            file = open(file_name, "r")     # open file with r mode
            for line in file:
                product, price = line.split(",")
                row = {"Name": product.strip(), "Price": price.strip()}
                list_of_rows.append(row)
            file.close()
        except Exception as e:      # Checks for file access errors
            print("There was a general error!")
            print(e, e.__doc__, type(e), sep='\n')
        return list_of_rows
# --End of class--
# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """  A class for performing Input and Output
    methods:
        print_menu_items():
        print_current_list_items(list_of_rows):
        input_product_data():
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class:
        JShin,12.14.2022,Modified code to complete assignment 8
    """

    @staticmethod
    def print_menu_items():
        """  Display a menu of choices to the user
        :return: nothing
        """
        print('''
        Menu of Options
        1) Show current data
        2) Add a new item
        3) Save Data to File
        4) Exit Program
        ''')
        print()  # Add an extra line for looks in the terminal window

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user
        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_list_items(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows
        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current products and prices are: *******")
        print("Name" + "\t" + "Price")
        for row in list_of_rows:
            print(row["Name"] + "\t" + "$" + row["Price"])
        print("****************************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_product_data():
        """  Gets product and price values to be added to the list
        :return: (string, float) with product and price
        """
        name = input("Enter a product: ").strip()
        price = input("Enter the price: ")
        return name, price
# --End of class--
# Presentation (Input/Output)  -------------------------------------------- #


# Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of product objects when script starts
list_of_objects = FileProcessor.read_data_from_file(file_name_str,list_of_objects)

while (True):
    # Show user a menu of options
    IO.print_menu_items()

    # Get user's menu option choice
    choice_str = IO.input_menu_choice()

    # Show user current data in the list of product objects
    if choice_str.strip() == '1':
        IO.print_current_list_items(list_of_objects)
        continue    # to show the menu

    # Let user add data to the list of product objects
    elif choice_str.strip() == '2':
        name_str, price_flt = IO.input_product_data()
        Product(name_str, float(price_flt))
        row_of_object = {"Name": name_str.strip(), "Price": price_flt.strip()}
        list_of_objects.append(row_of_object)
        continue    # to show the menu

    # let user save current data to file and exit program
    elif choice_str.strip() == '3':     # Save Data to File
        FileProcessor.save_data_to_file(file_name_str,list_of_objects)
        continue    # to show the menu

    # let user save current data to file and exit program
    elif choice_str.strip() == '5':     # Save Data to File
        csv_str = Product.to_string
        print(csv_str)
        continue    # to show the menu

    elif choice_str == '4':     # Exit Program
        print("Goodbye!")
        break  # by exiting loop

# Main Body of Script  ---------------------------------------------------- #