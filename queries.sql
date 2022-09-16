-- mysql -u root -p
-- Password#123

-- MySql DATETIME format: YYYY-MM-DD HH:MM:SS

-- Queries used to do tests
INSERT INTO administrators (administrator_name, administrator_password_hash) 
VALUES ('admtest', 'admpassword');

INSERT INTO administratorlogs (administratorlogs_type, administratorlogs_administrator_id, administratorlogs_action) 
VALUES ('CREATE', 1, 'CREATE A EMPLOYEE <EMPLOYEE_NAME>');

INSERT INTO employees (employee_cpf, employee_email, employee_name, employee_password_hash) 
VALUES ('12345678900', 'test@mail.com', 'test name', 'password');

INSERT INTO employeelogs (employeelogs_type, employeelogs_employee_id, employeelogs_action) 
VALUES ('CREATE', 1, 'CREATE A CLOCK');

INSERT INTO clocks (clock_employee_id, clock_input, clock_output, clock_extra) 
VALUES (1, '2022-08-31 12:00:00', '2022-08-31 18:00:00', 0);

INSERT INTO users (user_cpf, user_name, user_password, user_first_access, user_status, user_is_admin)
VALUES ('05653031127', 'joao', 'senha123', 0, 1, 1);

INSERT INTO users (user_cpf, user_name, user_password, user_first_access, user_status, user_is_admin)
VALUES ('12345678901', 'admin', 'senha123', 0, 1, 1);
