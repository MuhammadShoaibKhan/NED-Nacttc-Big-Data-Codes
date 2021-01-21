DELIMITER //

CREATE PROCEDURE proc2(IN X INT, IN tname VARCHAR(255))

BEGIN
	SELECT * FROM teacher_table
	WHERE teacher_id=X AND teacher_name=tname;
	END//

DELIMITER ;