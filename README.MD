# Banking Widget
## Description: 
This is a widget that shows a customer's last few successful banking transactions. At the moment, a function has been implemented that masks card and account numbers entered by the user into the terminal and a function that sorts the list by key and date.
A tool has been created to efficiently work with large volumes of transaction data, using Python's capabilities to process data through generators. Added a function that takes a path to a JSON file as input and returns a list of dictionaries with financial transaction data.
If the file is empty, does not contain a list, or is not found, the function returns an empty list.A function has been added that accepts a transaction as input and returns the transaction amount (amount) in rubles, data type — float USD or EUR, an external API is called 
to obtain the current exchange rate and convert the transaction amount into rubles. Implemented logging of two functions into files. Implemented reading of financial transactions from CSV and XLSX files.A function has been implemented that accepts a list of dictionaries with
data on banking transactions and a search string, and returns a list of dictionaries that have this string in their description, and a function that accepts a list of dictionaries with data on banking transactions and a list of transaction categories, and returns a dictionary 
in which the keys are the names of the categories, and the values ​​are the number of transactions in each category. The function , which is responsible for the main logic of the project and connects the functionalities between themselves, has been implemented.
## Installation:
1. Clone the repository:
[GitHub](https://github.com/Lemur946/HomeWork)
2. Install dependencies:
``pip install -r requirements.txt``
## Usage:
### To start the project
1. [Сlick here](src/main.py)
2. Scroll to the end of the file
3. Click on the green triangle next to the line "if __name__ == "__main__":"
4. To interact with the program, use the terminal
### To run the account or card number masking function:
1. [Сlick here](src/widget.py)
2. Right click anywhere
3. From the context menu select "run widget.py"

### To run the function to sort data by key or date:
1. [Сlick here](src/processing.py)
2. Right click anywhere
3. From the context menu select "run processing.py"

### To run functions and generators that implement data processing:
1. [Сlick here](src/generators.py)
2. Right click anywhere
3. From the context menu select "run processing.py"
### To launch functions that allow you to convert currency into rubles and withdraw the amount:
#### ATTENTION! Before starting, do not forget to read the hints in the .env.example file
1. [Сlick here](src/__init__.py)
2. Right click anywhere
3. From the context menu select "run __init__.py"
### To launch functions for reading financial transactions from a CSV file:
1. [Сlick here](src/read_operations_csv.py)
2. Right click anywhere
3. From the context menu select "run read_operations_csv.py"
### To launch functions for reading financial transactions from a Excel file:
1. [Сlick here](src/read_operations_xlsx.py)
2. Right click anywhere
3. From the context menu select "run read_operations_xlsx.py"
## Tests:
Testing of all available application functions has been carried out. 
Test coverage is 99%. To test, enter in the terminal command ```pytest```. 
To check the coverage percentage, enter the command in the terminal ```pytest --cov``` 
or open ```./htmlcov/index.html```
## Documentation:
information about the project structure [here](README.MD)
## Feedback:
Please send your feedback and suggestions by email taifyn932802@gmail.com
## Developer:
Artem Lemur Stytsko on instructions from [SkyPro](https://sky.pro/)
## License:
Not yet
