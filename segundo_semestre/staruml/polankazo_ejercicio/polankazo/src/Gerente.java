public class Gerente extends Persona {
    private String telefono;
    private String email;
    private String clave;
    private Profesion profesion;

    // Constructores
    Gerente() {

    }
    Gerente(String run, String nombre, String direccion, String telefono, String email, String clave, Profesion profesion) {
        super(run, nombre, direccion);
        this.telefono = telefono;
        this.email = email;
        this.clave = clave;
        this.profesion = profesion;
    }

    // Getters
    public String getTelefono() {
        return telefono;
    }
    public String getEmail() {
        return email;
    }
    public String getClave() {
        return clave;
    }
    public Profesion getProfesion() {
        return profesion;
    }

    // Setters
    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }
    public void setEmail(String email) {
        this.email = email;
    }
    public void setClave(String clave) {
        this.clave = clave;
    }
    public void setProfesion(String nombre, String codigo) {
        this.profesion = new Profesion(nombre, codigo);
    }

    public String infoProfesion() {
        return String.format("Mi profesión es %s.", profesion.getNombre());
    }
}