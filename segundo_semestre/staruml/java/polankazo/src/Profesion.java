public class Profesion {
    private String nombre;
    private String codigo;

    // Constructores
    Profesion() {

    }
    Profesion(String nombre, String codigo) {
        this.nombre = nombre;
        this.codigo = codigo;
    }

    // Getters
    public String getNombre() {
        return nombre;
    }
    public String getCodigo() {
        return codigo;
    }

    // Setters
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public void setCodigo(String codigo) {
        this.codigo = codigo;
    }

    public String infoProfesion() {
        // Cambiar
        return String.format("Hola, mi profesión es %s", nombre);
    }
}