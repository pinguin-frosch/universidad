package main;

public class Dueño extends Persona {
    private String direccion;

    public String getDireccion() {
        return direccion;
    }

    public void setDireccion(String direccion) {
        this.direccion = direccion;
    }

    Dueño(String run, String nombre, String apellido, String direccion) {
        super(run, nombre, apellido);
        this.direccion = direccion;
    }

    // public void pagarBoleta(Medidor medidor) {
    //     medidor.registro
    // }
}
