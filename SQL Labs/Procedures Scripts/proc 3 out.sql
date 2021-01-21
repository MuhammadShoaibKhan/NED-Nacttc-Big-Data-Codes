DELIMITER //

CREATE PROCEDURE proc3(OUT totalTeachers INT)

BEGIN
SELECT COUNT(teacher_id) INTO totalTeachers FROM teacher_table;
END//


DELIMITER ;