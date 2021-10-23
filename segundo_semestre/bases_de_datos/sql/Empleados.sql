INSERT INTO ciudad VALUES
(1, 'Santa Bárbara');

INSERT INTO ciudad VALUES
(2, 'Los Ángeles');

INSERT INTO ciudad VALUES
(3, 'Concepción');

INSERT INTO ciudad VALUES
(4, 'Santiago');

INSERT INTO ciudad VALUES
(5, 'Valdivia');

----------------------------------------------------------------

INSERT INTO empleado VALUES
('10.760.697-1', 'Juan Villa', 38, 'masculino', 541452, 1);

INSERT INTO empleado VALUES
('13.449.429-8', 'María Inostroza', 26, 'femenino', 632454, 1);

----------------------------------------------------------------

INSERT INTO empleado VALUES
('17.992.162-6', 'Florin Navarro', 40, 'masculino', 123454, 2);

INSERT INTO empleado VALUES
('19.597.872-7', 'Aida Calleja', 21, 'femenino', 541413, 2);

----------------------------------------------------------------

INSERT INTO empleado VALUES
('22.926.291-2', 'Casimiro Arjona', 33, 'masculino', 545313, 3);

INSERT INTO empleado VALUES
('19.490.799-0', 'Evangelina Cerezo', 31, 'femenino', 551464, 3);

----------------------------------------------------------------

INSERT INTO empleado VALUES
('16.444.446-5', 'Ayman Tirado', 29, 'masculino', 203978, 4);

INSERT INTO empleado VALUES
('21.866.939-5', 'Adelina Taboada', 40, 'femenino', 375922, 4);

----------------------------------------------------------------

INSERT INTO empleado VALUES
('19.743.346-9', 'Ayman Ali', 59, 'masculino', 172708, 5);

INSERT INTO empleado VALUES
('20.461.019-3', 'Vicenta Corral', 28, 'femenino', 340650, 5);

----------------------------------------------------------------

SELECT sexo_empleado AS SEXO, COUNT(sexo_empleado) AS TOTAL
FROM empleado GROUP BY sexo_empleado;

----------------------------------------------------------------

SELECT sexo_empleado AS SEXO, COUNT(sexo_empleado) AS TOTAL FROM
empleado WHERE edad > 18 GROUP BY sexo_empleado HAVING sexo_empleado = 'femenino';

----------------------------------------------------------------