# Banking Widget

## Description:

This is a widget that shows a customer's last few successful banking transactions. At the moment, a function has been
implemented that masks card and account numbers entered by the user into the terminal and a function that sorts the list
by key and date.
A tool has been created to efficiently work with large volumes of transaction data, using Python's capabilities to
process data through generators. The
log
decorator has been developed, which automatically logs the details of function execution, such as the call time, the
function name, the arguments passed, the execution result, and error information. This allows for deeper control and
analysis of the program's behavior during its execution.

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

### To run the function decorator:
1. [Сlick here](src/decorators.py)
2. Add examples of using the decorator to the end of the code.

This block of code will show in the console that the decorator is running.
```python
@log()
def my_function(x, y):
    return x + y

my_function(1, 2)
```
This block of code will show in the console that the decorator throws a divide by zero error, which we can track down.
```python
@log()
def my_function(x, y):
    return x / y

my_function(1, 0)
```
3. Right click anywhere
4. From the context menu select "run decorators.py"
5. For the testing to work correctly, you need to remove all changes to the code that you have entered.

## Tests:

Testing of all available application functions has been carried out.
Test coverage is 99%. To test, enter in the terminal command ```pytest```.
To check the coverage percentage, enter the command in the terminal ```pytest --cov```
or open ```./htmlcov/index.html```
Before entering the ```pytest``` command, make sure that the ```decorators.py``` module has removed examples of decorator usage, for example:
```python
@log()
def my_function(x, y):
    return x + y

my_function(1, 2)
```
```python
@log()
def my_function(x, y):
    return x / y

my_function(1, 0)
```
This is necessary for the tests to work correctly.
## Documentation:

information about the project structure [here](README.MD)

## Feedback:

Please send your feedback and suggestions by email taifyn932802@gmail.com

## Developer:

Artem Lemur Stytsko on instructions from [SkyPro](https://sky.pro/)

## License:

Not yet
