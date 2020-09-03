-- Calling DB schema
use trc;

-- Creating the Bus Schedule table
DROP TABLE IF EXISTS BusSchedule;

CREATE TABLE BusSchedule (
Bus_Number INT,
station VARCHAR(50) NOT NULL,
Stop_Time TIME NOT NULL
);

-- Data entry into BusSchedule table
INSERT INTO BusSchedule values
(1, 'Sacramento', '08:00'),
(1, 'Elk Grove', '08:35'),
(1, 'Lodi', '09:00'),
(1, 'Stockton', '09:25'),
(1, 'Manteca', '09:45'),
(1, 'Modesto', '10:20'),
(2, 'Sacramento', '08:00'),
(2, 'Stockton', '09:05'),
(2, 'French Camp', '09:25'),
(2, 'Lathrop', '09:40'),
(2, 'Tracy', '10:00')
;

-- Checking the table to make sure if data has been entered correctly
SELECT * FROM BusSchedule;


DROP PROCEDURE IF EXISTS get_bus_schedule;

-- Creating Stored Procedure that takes in the bus number and returns the schedule table for that bus

DELIMITER //
CREATE PROCEDURE get_bus_schedule ( IN bus_num INT)
BEGIN
	SELECT b1.Bus_Number, b1.station, 
		-- Using TIMEDIFF to find elapsed time from start of the trip from Sacramento. 
		-- The start_time comes from the subquery below the JOIN statement
        IFNULL(TIMEDIFF(b1.Stop_Time, b2.Start_Time), 0)  as 'Total_Travel_Time',
		-- Using LAG and Partition by functionality to find the time difference between 2 consecutive time stamps. 
		IFNULL(TIMEDIFF(Stop_Time, LAG(Stop_Time) OVER (partition by Bus_Number)), '00:00:00') as 'Time_to_Next_Station'
        
	-- The BusSchedule is joined by a subquery table derived from BusSchedule
	FROM BusSchedule b1
		JOIN 
		(
		SELECT MIN(Stop_Time) as 'Start_Time' FROM BusSchedule WHERE Bus_Number = bus_num
		) b2
		WHERE Bus_Number = bus_num;
END //
DELIMITER ;


CALL get_bus_schedule(1); -- Pass in the bus number













