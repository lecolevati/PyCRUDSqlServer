CREATE TABLE pessoa(
id INT NOT NULL PRIMARY KEY,
nome VARCHAR(30),
salario DECIMAL(7,2))

DECLARE @id INT,
		@nome VARCHAR(30),
		@salario FLOAT
SET @id = 1
WHILE (@id < 40)
BEGIN
	SET @nome = 'Pessoa '+CAST(@id AS VARCHAR(2))
	SET @salario = RAND() * 5000 + 1000
	INSERT INTO pessoa VALUES (@id, @nome, @salario)
	SET @id = @id + 1
END

SELECT * FROM pessoa
