-- Calling DB schema
use trc;

DROP TABLE IF EXISTS Employees;

-- Creating Employees table
CREATE TABLE Employees (
EmployeeId INTEGER PRIMARY KEY,
ManagerId INTEGER NULL,
FirstName VARCHAR(20) NOT NULL,
LastName VARCHAR(20) NOT NULL
);

-- Data entry into Employees table
INSERT INTO Employees values
(1 , NULL, 'Margo', 'Stephenson'),
(2 , 1, 'Armani', 'Blundell'),
(5 , 1, 'Melvin', 'Sadler'),
(12 , 2, 'Aalia', 'Smyth'),
(15, 2, 'Brook', 'Sanford'),
(17 , 5, 'Corinne', 'Barclay'),
(19 , 5, 'Charlie', 'Ball'),
(22 , 2, 'Aarav', 'Mason'),
(27 , 2, 'Ebrahim', 'Vazquez'),
(31 , 22, 'Calista', 'Seymour')
;


-- Checking the table to make sure if data has been entered correctly
select * from employees;


DROP PROCEDURE IF EXISTS get_employees_under_manager;

-- The main idea of executing the requirement is to create a query using recursive Common Table Expression (CTE)
-- The query can be executed using a stored procedure
-- User can call the stored procedure and pass in the employee ID to query all employees under him/her
-- Below is a walkthrough on how it works

DELIMITER //
CREATE PROCEDURE get_employees_under_manager ( IN emp_id INT)
BEGIN
	-- Creating a CTE called EmployeeTree
	WITH RECURSIVE EmployeeTree AS
	(
		-- This query finds the employee with the passed in employee ID and sets him/her as the root 
		SELECT EmployeeId, FirstName, LastName FROM Employees WHERE EmployeeId = emp_id
        
        -- Union ALL stacks the root employee with all the child node employees found from the recursion
		UNION ALL
        
        -- This query joins the exisitng Employee table with the CTE table to find employees working under that employee ID
        -- This is where the recursion happens as the CTE is being used inside the CTE
        -- With every recursion step it goes down 1 level until it has found all the child node employees
		SELECT e.EmployeeId, e.FirstName, e.LastName
		FROM EmployeeTree et
		JOIN
		Employees e
		ON et.EmployeeId = e.ManagerId
	) 
    -- This final query returns all the employees from the CTE except the root employee
	SELECT * FROM EmployeeTree WHERE EmployeeId <> emp_id ORDER BY EmployeeId
	;
	
END //
DELIMITER ;get_employees_under_managerget_employees_under_manager


CALL get_employees_under_manager(2); -- Pass in the employee ID
