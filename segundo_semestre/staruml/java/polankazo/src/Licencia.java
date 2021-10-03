public class Licencia {
    private int codigo;
    private String tipo;
    private String detalle;

    // Constructores
    Licencia() {

    }
    Licencia(int codigo, String tipo, String detalle) {
        this.codigo = codigo;
        this.tipo = tipo;
        this.detalle = detalle;
    }

    // Getters
    public int getCodigo() {
        return codigo;
    }
    public String getTipo() {
        return tipo;
    }
    public String getDetalle() {
        return detalle;
    }

    // Setters
    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }
    public void setTipo(String tipo) {
        this.tipo = tipo;
    }
    public void setDetalle(String detalle) {
        this.detalle = detalle;
    }

    public String infoLicencia() {
        // Cambiar
        return String.format("Mi licencia de conducir es %s", codigo);
    }
}