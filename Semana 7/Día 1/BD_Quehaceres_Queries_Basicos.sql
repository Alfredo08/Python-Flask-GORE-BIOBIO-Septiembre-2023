
INSERT INTO usuarios(nombre, apellido, password, correo)
VALUES ('Alex', 'Miller', 'pass1234', 'alex@miller.com');

INSERT INTO usuarios(nombre, apellido, password, correo)
VALUES ('Martha', 'Gómez', 'pass1234', 'martha@gomez.com'),
	   ('Roger', 'Anderson', 'pass1234', 'roger@anderson.com'),
       ('Alan', 'Martínez', 'pass1234', 'alan@martinez.com'),
       ('Alex', 'Morales', 'pass1234', 'alex@morales.com');
       
INSERT INTO usuarios(nombre, apellido, password, correo)
VALUES ('Alfredo', 'Salazar', 'pass1234', 'alfredo@salazar.com');

SELECT *
FROM usuarios; 

SELECT nombre, apellido, correo
FROM usuarios;

SELECT *
FROM usuarios
WHERE nombre = 'Alex';

SELECT *
FROM usuarios
WHERE id > 3;

SELECT CONCAT(nombre, ' ', apellido) AS 'Nombre Completo', correo AS Email
FROM usuarios;

UPDATE usuarios
SET apellido = 'Salazar'
WHERE id = 6;

DELETE FROM usuarios
WHERE id = 4;

INSERT INTO usuarios(nombre, apellido, password, correo)
VALUES ('Julieta', 'González', 'pass1234', 'julieta@gonzalez.com');

