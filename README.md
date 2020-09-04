# TRC-Coding-Assignment

1. [Python Cash Registry Program](#Python-Cash-Registry-Program)
2. [SQL](#SQL)
    * [Bus Schedule](#Bus-Schedule)
    * [Employees](#Employees)
3. [JS CSS Dynamic Todo List](#JS-CSS-Dynamic-Todo-List)


## Python Cash Registry Program

#### Problem Statement

<img src="https://github.com/shafin071/TRC-Coding-Assignment/blob/master/Assets/Python/cash_reg.gif" width="420" height="300">

Write a cash register program that:
- Allows you to scan items and then computes the total at checkout. 
- Provide support for volume discounts.

A string of IDs represents multiple items. For example:
- the string ABCD represents 1 soda, 1 apple, 1 jelly, and 1 kleenex and the total at checkout would be $10.45. 
- The string DCCBAABB represents 1 kleenex, 2 jelly, 3 apple and 2 soda and the total at checkout would be $15.00.

Demonstrate that your program works using the strings ABCD and DCCBAABB.

Bonus Points: The code for each item should be model-driven. For example, define the map from letter to grocery item with a JSON file so more grocery
items can be added

<img src="https://github.com/shafin071/TRC-Coding-Assignment/blob/master/Assets/Python/table.JPG" width="400" height="280">

#### Approach:

- Solved the problem with a modular approach with Python OOP. 
- Inventory data stored in a JSON file. 

**Python_assignment/data/inventory.json**

```
{
    "A": {
		"Item": "Soda",
		"Cost": "1.0",
		"Volume": "4",
		"Discount": "3.0"
			},

	"B": {
		"Item": "Apple",
		"Cost": "0.45",
		"Volume": "3",
		"Discount": "1.0"
		},

	"C": {
		"Item": "Jelly",
		"Cost": "3.0"
		},

	"D": {
		"Item": "Kleenex",
		"Cost": "6.0"
		}
}
```

- Wrote 2 classes ```CashRegister```, ```DataServices``` and a function ```run_cash_register```
- ```CashRegister``` : Calculates total bill and applies discount if applicable
- ```DataServices``` : Prepares data needed for ```CashRegister``` to calculate the bill. Inherited by ```CashRegister``` 
- ```run_cash_register```: 
	- Sets up the program by passing all the args (```barcodes, data_file_path, object_cols, output_file_path```) to ```CashRegister```
	- For ```barcodes```, it can pass multiple shopping codes 
- Output was printed to console as well as stored in a newly created json file in data folder.
- An order number was added to the JSON file to avoid conflict in same code orders. Multiple people can buy the same combination of items

**Python_assignment/data/output.json**
```
{"1": {"order_code": "ABCD", "order_total": 10.45}, "2": {"order_code": "DCCBAABB", "order_total": 15.0}}
```

#### Solution:
**Demo:**
<img src="https://github.com/shafin071/TRC-Coding-Assignment/blob/master/Assets/Python/demo.gif" width="1100" height="650">
- The program calculated:
   - A bill of **$10.45** for order **ABCD** . No volume discount applicable
   - A bill of **$15.0** for order **DCCBAABB** . ```CashRegister``` applied the *3 for $1* volume discount for item B which brought the price down from *$15.35* to *$15.0*

#### Testing:
- The program also comes with a unittest module to verify the calculated total for different cases
- Test results are stored in a newly created .txt file in test folder.

**Python_assignment/test/test_results/results.txt**
```
----------------------------------------------------------------------
Ran 3 tests in 0.084s

OK
```

#### Installation:
- ```git clone``` or download zip the entire assignment
- Open the *Python_assignment* folder in your preferable IDE (I used PyCharm for this project)
- Create a virtual environment. Run: ```python3 -m venv <name_of_virtualenv>```
- Install the dependencies by going to the project root directory *Python_assignment/*  and run: ```pip install -r requirements.txt```


#### How to run the program:
- Go to root directory *Python_assignment/* and run: ```python run.py```
- The results will be printed as well saved in a newly created json file in data folder *Python_assignment/data/output.json:*

#### How to run tests:
- Go to root directory *Python_assignment/* and run: ```python test/test_cash_reg.py```
- Test results will be stored in a newly created .txt file in test folder *Python_assignment/test/test_results/results.txt*
- If you wish to see the test results in console instead, simply change the following code in the bottom section of *Python_assignment/test/test_cash_reg.py*

Replace:
```
if __name__ == '__main__':
    """
    Save result output in a text file in test/test_results folder
    """
    with open(test_result_file, "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)

```

with:
```
if __name__ == '__main__':
    unittest.main()
```


#### Important notes about output data files generated by the program:
- On the very fist run, the output files will be created
- On recurring runs, if file already exists, it'll be overwirtten.

#### Interpreter: 
- ```Python 3.7```

#### Packages: 
- ```numpy==1.19.1```
- ```pandas==1.1.1```
- ```python-dateutil==2.8.1```
- ```pytz==2020.1```
- ```six==1.15.0```


<br>
<hr>
<br>

## SQL

This section of the assignments consists of two tasks: Bus Schedule & Employees

### Bus Schedule

<img src="https://github.com/shafin071/TRC-Coding-Assignment/blob/master/Assets/SQL/bus_stop.gif" width="450" height="300">

#### Problem Statement

<img src="https://github.com/shafin071/TRC-Coding-Assignment/blob/master/Assets/SQL/original_table.JPG" width="400" height="400">

Using the bus schedule above, write a SQL statement (query, stored procedure, or function) to calculate the time between each stop and total elapsed
time since leaving the Sacramento station. Partial sample output below.

<img src="https://github.com/shafin071/TRC-Coding-Assignment/blob/master/Assets/SQL/example_result_table.JPG" width="440" height="140">

#### Solution
Wrote a stored procedure ```get_bus_schedule``` that takes in the bus number and returns the schedule table for that bus along with time between each stop and total elapsed time
- Used ```LEAD``` and ```PARTITION BY``` functionality to find the time difference between 2 consecutive stops.
- Used ```TIMEDIFF``` and ```PARTITION BY``` to find elapsed time from start of the trip from Sacramento. 

The procedure can be called as shown:
``` CALL get_bus_schedule(bus_number); ``` where bus number can 1 or 2 as per the ```BusSchedule``` table

![Result](https://github.com/shafin071/TRC-Coding-Assignment/blob/master/Assets/SQL/result_table.JPG)

#### Tools: 
- MySQL
- MySQL Workbench 8.0 CE



### Employees

<img src="https://github.com/shafin071/TRC-Coding-Assignment/blob/master/Assets/SQL/employee-hierarchy.gif" width="600" height="360">

#### Problem Statement

<img src="https://github.com/shafin071/TRC-Coding-Assignment/blob/master/Assets/SQL/employee_table.JPG" width="460" height="360">

Using the list of employees above, write a SQL statement (query, stored procedure, or function) to return all the employees in the organization below a
specified manager, which may include multiple levels of employees.

Note: A sample run using Margo, EmployeeId=1 would return the entire dataset.

Sample Run using: Armani, EmployeeID=2

<img src="https://github.com/shafin071/TRC-Coding-Assignment/blob/master/Assets/SQL/employee_result_example.JPG" width="360" height="200">

#### Solution
Wrote a stored procedure ```get_employees_under_manager``` that takes in the employee ID and returns ALL the employees working under him/her. The solution achieved using the following SQL commands
- ```WITH RECURSIVE``` on Common Table Expression (CTE)
- ```UNION ALL``` 
- ```JOIN```

The combination of these commands created a recursive query that starts from the root (employee ID arg of stored procedure) and traverses down the hierarchy of employees in a breadth-first search manner to find all node employees
 
The procedure can be called as shown:
``` CALL get_employees_under_manager(employee_ID); ``` 

![Result](https://github.com/shafin071/TRC-Coding-Assignment/blob/master/Assets/SQL/my_employee_result.JPG)

#### Tools: 
- MySQL
- MySQL Workbench 8.0 CE

<br>
<hr>
<br>



## JS CSS Dynamic Todo List

<img src="https://github.com/shafin071/TRC-Coding-Assignment/blob/master/Assets/JS_CSS/todo.gif" width="460" height="360">

#### Problem Statement

Given the HTML below of a todo list implementation, write a javascript and CSS source so that

- the user can add new tasks using the input field and add button.
   - The complete checkbox must also be added as well as the task name to the table row.
   - Pressing the enter key on the keyboard should
   - Empty task names should not be added.
   
- the user can complete tasks by selecting the checkbox for the task.
   - Completing the task crosses (strikethrough) out the name of the task and adds a value for time completed (browser's local timezone is fine)
   - The format of the timestamp must be "Month Day, Year, Hour:Minutes AM/PM". For example:
      - Feb 20, 2020, 1:37 PM
 
 - Style the table as follows:
   - Add borders for the cells
   - Cells are evenly aligned and spaced.
   - The rows alternate colors: #ced4ff, #fbffe6
 
Modify the HTML to include a header section linking the JS and CSS files. Feel free to use jQuery. Submit the 3 files.

**index.html**

   ```
   <h2>My Task List</h2>
   <table id="todo">
      <tr>
         <th>Task Name</th>
         <th>Time Completed</th>
         <th></th>
      </tr>
      <tr class="row">
         <td>Get groceries</td>
         <td class="t_completed"></td>
         <td class="item_complete"> <input type="checkbox"> </td>
      </tr>
      <tr class="row">
         <td>Take out trash</td>
         <td class="t_completed"></td>
         <td class="item_complete"> <input type="checkbox"> </td>
      </tr>
   </table>
   <div id="TodoAdd">
      <input type="text" id="myInput" placeholder="Next Task">
   <button>Add</button>
   </div>
   ```

**Unmodified Preview:**

<img src="https://github.com/shafin071/TRC-Coding-Assignment/blob/master/Assets/JS_CSS/unmod.JPG" width="360" height="200">

#### Solution
- Applied several trigger events, DOM and CSS manipulations to meet the functional requirements
- All the styling requirements were met using CSS 
- User can add tasks with either the ```Add``` button or ```Enter``` key
- Attempting to enter a blank task will result in an alert
- Checking a task will cross out the task and add the current timestamp
- Unchecking a task will remove the strike-through and timestamp

**Demo:**

<img src="https://github.com/shafin071/TRC-Coding-Assignment/blob/master/Assets/JS_CSS/demo.gif" width="640" height="450">

#### Tools: 
- JQuery http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js
- CSS
- Chrome Browser




