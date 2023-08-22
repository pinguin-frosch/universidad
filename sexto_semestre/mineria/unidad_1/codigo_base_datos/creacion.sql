CREATE TABLE Venta(
  id INT PRIMARY KEY IDENTITY,
  fecha date
)

CREATE TABLE Compra(
  id INT PRIMARY KEY IDENTITY,
  fecha DATE
)

CREATE TABLE Categoria(
  id INT PRIMARY KEY IDENTITY,
  nombre VARCHAR(50)
)

CREATE TABLE Producto(
  id INT PRIMARY KEY IDENTITY,
  precio_unitario INT,
  categoria_id INT FOREIGN KEY REFERENCES Categoria(id)
)

CREATE TABLE Marca(
  id INT PRIMARY KEY IDENTITY,
  nombre VARCHAR(50)
)

CREATE TABLE Proveedor(
  id INT PRIMARY KEY IDENTITY,
  nombre VARCHAR(50)
)

CREATE TABLE Lote(
  id INT PRIMARY KEY IDENTITY,
  fecha_vencimiento DATE,
  fecha_elaboracion DATE,
  producto_id INT FOREIGN KEY REFERENCES Producto(id),
  marca_id INT FOREIGN KEY REFERENCES Marca(id),
  proveedor_id INT FOREIGN KEY REFERENCES Proveedor(id)
)

CREATE TABLE Cupon(
  id INT PRIMARY KEY IDENTITY,
  descuento VARCHAR(15),
  fecha_vencimiento DATE,
  descripcion VARCHAR(150)
)

CREATE TABLE Vendedor(
  id INT PRIMARY KEY IDENTITY,
  nombre VARCHAR(50)
)

CREATE TABLE MedioPago(
  id INT PRIMARY KEY IDENTITY,
  nombre VARCHAR(30)
)

CREATE TABLE Cliente(
  id INT PRIMARY KEY IDENTITY,
  rut VARCHAR(12),
  nombre VARCHAR(50),
  fecha_nacimiento DATE,
  genero VARCHAR(50)
)

CREATE TABLE Region(
  id INT PRIMARY KEY IDENTITY,
  nombre VARCHAR(50)
)

CREATE TABLE Provincia(
  id INT PRIMARY KEY IDENTITY,
  nombre VARCHAR(50),
  region_id INT FOREIGN KEY REFERENCES Region(id)
)

CREATE TABLE Ciudad(
  id INT PRIMARY KEY IDENTITY,
  nombre VARCHAR(50),
  provincia_id INT FOREIGN KEY REFERENCES Provincia(id)
)

CREATE TABLE Local(
  id INT PRIMARY KEY IDENTITY,
  nombre VARCHAR(50),
  direccion VARCHAR(50),
  ciudad_id INT FOREIGN KEY REFERENCES Ciudad(id)
)

CREATE TABLE VentaProducto(
  precio INT,
  cantidad INT,
  venta_id INT FOREIGN KEY REFERENCES Venta(id),
  producto_id INT FOREIGN KEY REFERENCES Producto(id),
  PRIMARY KEY(venta_id, producto_id)
)

CREATE TABLE VentaCupon(
  venta_id INT FOREIGN KEY REFERENCES Venta(id),
  cupon_id INT FOREIGN KEY REFERENCES Cupon(id),
  PRIMARY KEY(venta_id, cupon_id)
)

CREATE TABLE CuponProducto(
  cupon_id INT FOREIGN KEY REFERENCES Cupon(id),
  producto_id INT FOREIGN KEY REFERENCES Producto(id),
  PRIMARY KEY(cupon_id, producto_id)
)

CREATE TABLE VentaMedioPago(
  monto INT,
  venta_id INT FOREIGN KEY REFERENCES Venta(id),
  medio_pago_id INT FOREIGN KEY REFERENCES MedioPago(id),
  PRIMARY KEY(venta_id, medio_pago_id)
)

CREATE TABLE CompraLote(
  cantidad INT,
  precio INT,
  compra_id INT FOREIGN KEY REFERENCES Compra(id),
  proveedor_id INT FOREIGN KEY REFERENCES Proveedor(id),
  lote_id INT FOREIGN KEY REFERENCES Lote(id),
  PRIMARY KEY(compra_id, proveedor_id, lote_id)
)

CREATE TABLE VendedorLocal(
  vendedor_id INT FOREIGN KEY REFERENCES Vendedor(id),
  local_id INT FOREIGN KEY REFERENCES Local(id),
  PRIMARY KEY(vendedor_id, local_id)
)