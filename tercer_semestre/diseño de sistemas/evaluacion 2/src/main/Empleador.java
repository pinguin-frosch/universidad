package main;

import java.util.Date;

public class Empleador extends Persona {
    private String telefono;

    public String getTelefono() {
        return telefono;
    }

    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }

    // public void entregarBoleta(Dueño dueño, Boleta boleta) {
    //     String.format("Entregando boleta %s a usuario %s", "<Rellenar boleta>", "<Rellenar usuario>");
    // }

    public Cobro hacerMedicion(int montoMedicion) {
        int montoCobro = montoMedicion * precioAguaConsumida;
        return new Cobro("Consumo mensual", new Date(), montoCobro);
    }

    Empleador(String run, String nombre, String apellido, String telefono) {
        super(run, nombre, apellido);
        this.telefono = telefono;
    }
}
