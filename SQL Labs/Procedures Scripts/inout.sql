DELIMITER //

CREATE PROCEDURE proc4(IN name VARCHAR(255), OUT totalTeachers INT, INOUT salary INT)

BEGIN
SELECT * FROM teacher_table
WHERE name=teacher_name;
UPDATE teacher_table
SET teacher_salary=salary
WHERE name=teacher_name;
SELECT COUNT(teacher_id) INTO totalTeachers FROM teacher_table;


END//




DELIMITER ;