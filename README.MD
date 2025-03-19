# Banking Widget
## Description: 
This is a widget that shows a customer's last few successful banking transactions. At the moment, a function has been implemented that masks card and account numbers entered by the user into the terminal and a function that sorts the list by key and date.
A tool has been created to efficiently work with large volumes of transaction data, using Python's capabilities to process data through generators. Added a function that takes a path to a JSON file as input and returns a list of dictionaries with financial transaction data.
If the file is empty, does not contain a list, or is not found, the function returns an empty list.A function has been added that accepts a transaction as input and returns the transaction amount (amount) in rubles, data type — float USD or EUR, an external API is called 
to obtain the current exchange rate and convert the transaction amount into rubles.
## Installation:
1. Clone the repository:
[GitHub](https://github.com/Lemur946/HomeWork)
2. Install dependencies:
``pip install -r requirements.txt``
## Usage:
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
