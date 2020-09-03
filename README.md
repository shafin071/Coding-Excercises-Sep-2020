# TRC-Coding-Assignment

1. [Python Cash Registry Program](#Python-Cash-Registry-Program)
2. [SQL](#SQL)
    * [Bus Schedule](#Bus-Schedule)
    * [Employees](#Employees)
3. [JS CSS Dynamic Todo List](#JS-CSS-Dynamic-Todo-List)


<!-- toc -->

## Python Cash Registry Program



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
``` CALL get_bus_schedule(bus_number); ``` where bus number can 1 or 2 as per the ```BusSchedule``` table

![Result](https://github.com/shafin071/TRC-Coding-Assignment/blob/master/Assets/SQL/my_employee_result.JPG)

#### Tools: 
- MySQL
- MySQL Workbench 8.0 CE

<br>
<hr>
<br>


## JS CSS Dynamic Todo List





