DELIMITER //

CREATE PROCEDURE SalaryStatus(IN emp_id INT, OUT sal_status VARCHAR(255))
BEGIN
DECLARE curr_sal DECIMAL(8,2);
DECLARE avrg_sal DECIMAL(8,2);
SELECT AVG(teacher_salary) INTO avrg_sal FROM teacher_table;
SELECT teacher_salary INTO curr_sal FROM teacher_table
WHERE  emp_id=teacher_id;
IF curr_sal < avrg_sal THEN
SET sal_status='Less than Average salary';
ELSEIF curr_sal=avrg_sal THEN
SET sal_status='Equal to average salary';
ELSEIF curr_sal>avrg_sal THEN
SET sal_status='Greater than average salary';
END IF;
END//

DELIMITER ;