DELIMITER //
SET SQL_SAFE_UPDATES = 0;


#CALL SalaryStatus(3,@sal_status)//
SELECT @sal_status;




#set @emp_id = '3';
#CALL SalaryStatus(@emp_id ,@sal_status)//
#select @SalaryStatus as 'Salary Satus of Employee';