-- Hecho por Gabriel Barrientos

-- DELETE FROM area;
-- DELETE FROM modeloarea;
-- DELETE FROM modelos3d;
-- DELETE FROM marca;
-- DELETE FROM materiales;
-- DELETE FROM tipomaterial;
-- DELETE FROM modelosmateriales;
-- DELETE FROM impresoramateriales;
-- DELETE FROM ciudad;
-- DELETE FROM direccion;
-- DELETE FROM proveedor;
-- DELETE FROM impresora3d;
-- DELETE FROM impresoraboquilla;
-- DELETE FROM boquilla;
-- DELETE FROM tipoimpresora;
-- DELETE FROM impresoramodelo;

INSERT INTO area VALUES(
    1234, 'local', 'es un �rea local'
);
-- SELECT * FROM area;

INSERT INTO modelos3d VALUES(
    1234, 'modelo', 'sirve para modelar', 'peque�o', '15%', 'azul', 'veinte', 'recurso'
);
-- SELECT * FROM modelos3d;

INSERT INTO modeloarea VALUES(
    1234, 1234
);
-- SELECT * FROM modeloarea;

INSERT INTO marca VALUES(
    1234, 'tercera'
);
-- SELECT * FROM marca;

INSERT INTO tipomaterial VALUES(
    1234, 'acero', 'firme', '�tomos', 'r�pida'
);
-- SELECT * FROM tipomaterial;

INSERT INTO materiales VALUES(
    1234, 'acero', 'gris', '25cm', 'largo', 'd�bil', '80�', '54', 'ni idea', 'mucha', 'elevada', 'd�bil', 'poca', 'bastante', 'no mucha', 1234, 1234
);
-- SELECT * FROM materiales;

INSERT INTO modelosmateriales VALUES(
    1234, 1234
);
-- SELECT * FROM modelosmateriales;

INSERT INTO ciudad VALUES(
    1234, 'ciudad'
);
-- SELECT * FROM ciudad;

INSERT INTO proveedor VALUES(
    1234, 'ernesto', '956981294', 'email@email.com', 'www.pagina.com'
);
-- SELECT * FROM proveedor;

INSERT INTO direccion VALUES(
    1234, 'aqu�', '3425', '45100324', 1234, 1234
);
-- SELECT * FROM direccion;

INSERT INTO boquilla VALUES(
    1234, 'boquilla', 'grande'
);
-- SELECT * FROM boquilla;

INSERT INTO tipoimpresora VALUES(
    1234, 'magisk', 'muy �til', 'impecable', 'excelente'
);
-- SELECT * FROM tipoimpresora;

INSERT INTO impresora3d VALUES(
    1234, 1234, 1234, 'impresora', '2.0', 'muy r�pida', 'suficiente'
);
-- SELECT * FROM impresora3d;

INSERT INTO impresoramodelo VALUES(
    1234, 1234
);
-- SELECT * FROM impresoramodelo;  

INSERT INTO impresoramateriales VALUES(
    1234, 1234
);
-- SELECT * FROM impresoramateriales;

INSERT INTO impresoraboquilla VALUES(
    1234, 1234
);
-- SELECT * FROM impresoraboquilla;