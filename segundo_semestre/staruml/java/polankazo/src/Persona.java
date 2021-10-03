abstract class Persona {
    private String run;
    private String nombre;
    private String direccion;

    // Constructores
    Persona() {

    }
    Persona(String run, String nombre, String direccion) {
        this.run = run;
        this.nombre = nombre;
        this.direccion = direccion;
    }

    // Getters
    public String getRun() {
        return run;
    }
    public String getNombre() {
        return nombre;
    }
    public String getDireccion() {
        return direccion;
    }

    // Setters
    public void setRun(String run) {
        this.run = run;
    }
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public void setDireccion(String direccion) {
        this.direccion = direccion;
    }

    public String infoPersona() {
        return String.format("Hola, mi run es %s, y mi nombre es %s.", run, nombre);
    }
}