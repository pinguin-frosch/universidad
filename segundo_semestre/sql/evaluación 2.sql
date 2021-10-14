1. Cree una consulta que muestre el nombre, color, longitud de todos los materiales que existen, ordenados alfabéticamente.
SELECT nombre_material, longitud_material, color_material FROM materiales ORDER BY nombre_material ASC;

2. Cree una consulta que muestre el nombre del tipo de material, y el nombre del color del material disponible.
SELECT tipomaterial.nombre_tipo_material, materiales.color_material FROM tipomaterial INNER JOIN materiales ON tipomaterial.codigo_tipo_material = materiales.fk_codigo_tipo_material;

3. Cree una consulta que muestre el color y longitud de los materiales que sean metales.
SELECT color_material, longitud_material FROM materiales WHERE nombre_material = 'METAL';

4. Cree una consulta que muestre el nombre del proveedor, nombre del tipo de impresora y el nombre de todas las impresoras existentes en la base de datos.
SELECT proveedor.nombre_proveedor, tipoimpresora.nombre_tipo_impresora, impresora3d.nombre_impresora FROM proveedor INNER JOIN impresora3d ON proveedor.codigo_proveedor=impresora3d.fk_codigo_proveedor INNER JOIN tipoimpresora ON impresora3d.fk_codigo_tipo_impresora=tipoimpresora.codigo_tipo_impresora;

5. Cree una consulta que muestre el nombre de la impresora y el nombre de los materiales que puede utilizar cada una de las impresoras.
SELECT DISTINCT impresora3d.nombre_impresora, materiales.nombre_material FROM impresora3d INNER JOIN impresoramateriales ON impresora3d.codigo_impresora = impresoramateriales.fk_codigo_impresora INNER JOIN materiales ON materiales.codigo_material = impresoramateriales.fk_codigo_material;