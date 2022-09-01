-- mysql -u root -p

-- MySql DATETIME format: YYYY-MM-DD HH:MM:SS

-- Queries used to do tests

INSERT INTO employees (employee_cpf, employee_email, employee_name, employee_password_hash) 
VALUES ('12345678900', 'test@mail.com', 'test name', 'password');

INSERT INTO clocks (clock_employee_id, clock_input, clock_output) 
VALUES (1, '2022-08-31 12:00:00', '2022-08-31 18:00:00');