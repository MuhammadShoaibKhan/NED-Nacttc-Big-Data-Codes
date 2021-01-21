DELIMITER //

create Procedure proc1()

begin
	DECLARE X INT;
	SET X=1;
	SELECT * FROM teacher_table
	WHERE teacher_id=X; 
END //


DELIMITER ;

