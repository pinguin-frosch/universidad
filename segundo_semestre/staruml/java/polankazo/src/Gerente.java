public class Gerente extends Persona {
    private String telefono;
    private String email;
    private String clave;

    // Constructores
    Gerente() {

    }
    Gerente(String run, String nombre, String direccion, String telefono, String email, String clave) {
        super(run, nombre, direccion);
        this.telefono = telefono;
        this.email = email;
        this.clave = clave;
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
}