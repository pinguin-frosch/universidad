package main;

abstract class Persona {
    private String run;

    public String getRun() {
        return run;
    }

    public void setRun(String run) {
        this.run = run;
    }

    private String nombre;

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    private String apellido;

    public String getApellido() {
        return apellido;
    }

    public void setApellido(String apellido) {
        this.apellido = apellido;
    }

    // Constructor completo
    Persona(String run, String nombre, String apellido) {
        this.run = run;
        this.nombre = nombre;
        this.apellido = apellido;
    }
}
