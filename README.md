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

#### Problem Statement

Using the bus schedule above, write a SQL statement (query, stored procedure, or function) to calculate the time between each stop and total elapsed
time since leaving the Sacramento station. Partial sample output below.

#### Solution
Wrote a stored procedure ```get_bus_schedule``` that takes in the bus number and returns the schedule table for that bus along with time between each stop and total elapsed time
- Used ```LAG``` and ```PARTITION BY``` functionality to find the time difference between 2 consecutive stops.
- Used ```TIMEDIFF``` and ```PARTITION BY``` to find elapsed time from start of the trip from Sacramento. 

The procedure can be called as shown:
``` CALL get_bus_schedule(bus_number); ``` where bus number can 1 or 2 as per the ```BusSchedule``` table

#### Tools: 
- MySQL
- MySQL Workbench 8.0 CE

### Employees

<br>
<hr>
<br>


## JS CSS Dynamic Todo List





