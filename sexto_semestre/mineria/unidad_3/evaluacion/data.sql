CREATE TABLE IF NOT EXISTS recorrido(
    empresa text NOT NULL,
    fecha timestamp NOT NULL,
    estudiantes smallint NOT NULL CHECK(estudiantes >= 0),
    adultos smallint NOT NULL CHECK (adultos >= 0),
    capacidad smallint NOT NULL CHECK (capacidad >= 0)
);
