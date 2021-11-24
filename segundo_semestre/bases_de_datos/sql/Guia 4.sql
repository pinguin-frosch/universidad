-- Cree una consulta que muestre el nombre y el nombre del día de nacimiento de todos los alumnos.
SELECT nombre_alumno AS "Nombre estudiante", LOWER(TO_CHAR(fecha_nacimiento_alumno, 'DAY', 'NLS_DATE_LANGUAGE = spanish')) AS "Fecha de nacimiento" FROM alumno;

-- Cree una consulta que muestre el nombre de la asignatura, el nombre del mes de inicio y el nombre de fin de todas las asignaturas.
SELECT DISTINCT asignatura.nombre_asignatura AS "Nombre asignatura", LOWER(TO_CHAR(cursa_asignatura.fecha_inicio, 'MONTH', 'NLS_DATE_LANGUAGE = spanish')) AS "Mes de inicio", LOWER(TO_CHAR(cursa_asignatura.fecha_fin, 'MONTH', 'NLS_DATE_LANGUAGE = spanish')) AS "Mes final" FROM asignatura INNER JOIN cursa_asignatura ON asignatura.codigo_asignatura = cursa_asignatura.fk_codigo_asignatura;

-- Cree una consulta que muestre el nombre de la asignatura y el nombre del mes del fin de todas las asignaturas de un estudiante en específico.
SELECT asignatura.nombre_asignatura AS "Nombre Asignatura", LOWER(TO_CHAR(cursa_asignatura.fecha_fin, 'MONTH', 'NLS_DATE_LANGUAGE = spanish')) AS "Mes final" FROM asignatura INNER JOIN cursa_asignatura ON asignatura.codigo_asignatura = cursa_asignatura.fk_codigo_asignatura WHERE cursa_asignatura.fk_rut_alumno = '21.234.653-9';

-- Cree una consulta que muestre el nombre de los estudiantes concatenado con nombre del mes de nacimiento de todos los estudiantes inscritos en una asignatura en específico.
SELECT alumno.nombre_alumno || ' - ' || LOWER(TO_CHAR(alumno.fecha_nacimiento_alumno, 'MONTH', 'NLS_DATE_LANGUAGE = spanish')) AS "Alumnos con mes de nacimiento" FROM alumno INNER JOIN cursa_asignatura ON alumno.rut_alumno = cursa_asignatura.fk_rut_alumno WHERE cursa_asignatura.fk_codigo_asignatura = '0000';