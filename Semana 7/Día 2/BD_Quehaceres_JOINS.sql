SELECT *
FROM usuarios;

INSERT INTO quehaceres(descripcion, status, id_usuario)
VALUES('Aprender Python', 'completo', 1),
	  ('Aprender Programación Orientada a Objetos', 'en_progreso', 1),
      ('Aprender SQL', 'en_proceso', 2),
      ('Aprender Flask', 'pendiente', 3),
	  ('Aprender Fundamentos de la Web', 'completo', 7);
      
SELECT *
FROM quehaceres;

SELECT u.id AS Usuario_ID, nombre, apellido, password, correo, q.id AS Quehacer_ID, descripcion, status, id_usuario
FROM usuarios u JOIN quehaceres q
	ON u.id = q.id_usuario
WHERE status = 'completo';


SELECT u.id AS Usuario_ID, nombre, apellido, password, correo, q.id AS Quehacer_ID, descripcion, status, id_usuario
FROM usuarios u, quehaceres q
WHERE status = 'completo' AND u.id = q.id_usuario;


SELECT u.id AS Usuario_ID, nombre, apellido, correo, q.id AS Quehacer_ID, descripcion, status, id_usuario
FROM usuarios u LEFT JOIN quehaceres q
	ON u.id = q.id_usuario;